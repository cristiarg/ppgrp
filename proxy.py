"""proxy service
"""

import sys
import time
import logging
# import time
from concurrent import futures
import grpc

sys.path.append("./proto")
import proxy_pb2
import proxy_pb2_grpc

PROXY_MAIN_PORT = 23000
PROXY_BASE_PORT = 23001
STARTING_GLOBAL_UNIQUE_ID = 12345

_ONE_DAY_IN_SECONDS = 60 + 60 * 24


class SessionId(object):
    """SessionId class
    TODO: merge into SessionDispatcherServiceHelper
    """

    _global_unique_id = -1

    def __init__(self):
        self._global_unique_id = STARTING_GLOBAL_UNIQUE_ID

    def get_next(self):
        """method
        """
        ret_val = self._global_unique_id
        self._global_unique_id += 1
        return ret_val


class Session(object):
    """Session class
    """

    def __init__(self, unique_id, port, service_name):
        self.unique_id = unique_id
        self.port = port
        self.service_name = service_name

    def __repr__(self):
        return "{{ unique_id:{}, port:{}, service_name:{} }}".format(
            self.unique_id, self.port, self.service_name)


class SessionDispatcherServiceHelper(object):
    """Internal object that helps map service_name's to session
    instances to port to session_id's
    """

    def __init__(self):
        self._session_id = SessionId()
        self._session_id_dict = {}

    def request_new_session(self, service_name):
        """method
        """
        next_unique_id = self._session_id.get_next()
        next_port = self._get_next_available_port()
        new_session = Session(next_unique_id, next_port, service_name)
        self._session_id_dict[next_unique_id] = new_session
        #resp_status = proxy_pb2.ResponseStatusEnum.SUCCESS
        #resp_endpoint_info = EndpointInfo(next_port)
        #resp_session_info = SessionInfo(next_unique_id, request.service_name, resp_endpoint_info)
        #return proxy_pb2.ServiceSessionResponse(resp_status , resp_session_info)
        return new_session

    def get_session(self, session_id):
        """retrieve session based on session id
        """
        if session_id in self._session_id_dict:
            return self._session_id_dict[session_id]
        return None

    def delete_session(self, session_id):
        """delete a session based on session id
        """
        if session_id in self._session_id_dict:
            del self._session_id_dict[session_id]
            return True
        return False

    def _get_next_available_port(self):
        if len(self._session_id_dict) > 0:
            # sort the sessions on port number into a list of tuples
            sorted_dict = sorted(self._session_id_dict.items(), key=lambda (ky, im): im.port)
            # the prev port initialized with the first one
            # to be returned incremented with one when a gap is found
            prev_port = sorted_dict[0][1].port
            # exclude the first port out of all the other ones
            tuple_rest = sorted_dict[1:]
            # iterate to find a gap
            for tup in tuple_rest:
                curr_sess = tup[1]
                if (curr_sess.port - prev_port) == 1:
                    # no gap, advance
                    prev_port = curr_sess.port
                else:
                    # gap found
                    break
            # if no gap found, return the one immediate after
            return prev_port + 1

        return PROXY_BASE_PORT


class SessionDispatcherService(proxy_pb2_grpc.SessionDispatcherServicer):
    def __init__(self):
        self._helper = SessionDispatcherServiceHelper()

    def Request(self, request, context):
        """Request a new session with the required service.
        """
        logging.debug("SessionDispatcherService.Request new session for service name '{}'".format(
            request.service_name))
        new_session = self._helper.request_new_session(request.service_name)
        logging.debug("SessionDispatcherService.Request new session with id {}".format(
            new_session.unique_id))

        new_endpoint_info = proxy_pb2.EndpointInfo(port=new_session.port)
        new_session_info = proxy_pb2.SessionInfo(session_id=new_session.unique_id,
                service_name=new_session.service_name, endpoint_info=new_endpoint_info)

        return proxy_pb2.RequestSessionResponse(session_info=new_session_info)

    def Release(self, request, context):
        """Release a session with the specified session id.
        """
        logging.debug("SessionDispatcherService.Release session with id '{}'".format(
            request.session_id))
        session_id = request.session_id
        # logging.debug("BEFORE")
        # logging.debug(self._helper._session_id_dict)
        session_delete_result = self._helper.delete_session(session_id)
        # logging.debug("AFTER")
        # logging.debug(self._helper._session_id_dict)
        if session_delete_result:
            return proxy_pb2.ReleaseSessionResponse()
        else:
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details("A session with id {} does not exist".format(session_id))
            return None



def _serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    logging.debug("server created")
    servicer = SessionDispatcherService()
    logging.debug("servicer created")
    proxy_pb2_grpc.add_SessionDispatcherServicer_to_server(servicer, server)
    logging.debug("added proxy servicer")
    insecure_port = server.add_insecure_port("[::]:{}".format(PROXY_MAIN_PORT))
    if insecure_port == PROXY_MAIN_PORT:
        logging.debug("added insecure port")
        server.start()
        logging.info("server started..")
        try:
            time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt as ex:
            # TODO: stop specific servicers

            logging.debug("server stopping..")
            server.stop(0)
            logging.info("server stopped")
    else:
        logging.critical("adding insecure port failed")
        logging.critical("bailing out..")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    _serve()
