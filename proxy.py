"""proxy service
"""

import sys
# import time
# from concurrent import futures
# import grpc

sys.path.append("./proto")
# import proxy_pb2
# import proxy_pb2_grpc

PROXY_BASE_PORT = 23001
#_SESSION_PORT_START = 23002
#_SESSION_PORT_END   = 23005
STARTING_GLOBAL_UNIQUE_ID = 12345


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
    # proxy_pb2_grpc.SessionDispatcherServicer

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
        """method
        """
        if session_id in self._session_id_dict:
            return self._session_id_dict[session_id]
        return None

    def delete_session(self, session_id):
        """method
        """
        if session_id in self._session_id_dict:
            del self._session_id_dict[session_id]
            return True
        return False

    def _get_next_available_port(self):
        if len(self._session_id_dict) > 0:
            # sort the sessions on port number
            sorted_dict = dict(sorted(self._session_id_dict.items(), key=lambda (ky, im): im.port))
            # the prev port initialized with the first one
            # to be returned incremented with one when a gap is found
            prev_port = sorted_dict.values()[0].port
            # exclude the first port out of all the other ones
            keyset_first = [sorted_dict.keys()[0]]
            keyset_others = sorted_dict.viewkeys() ^ keyset_first
            # iterate to find a gap
            for k in keyset_others:
                curr_sess = sorted_dict[k]
                if (curr_sess.port - prev_port) == 1:
                    # no gap, advance
                    prev_port = curr_sess.port
                else:
                    # gap found
                    break
            # if no gap found, return the one immediate after
            return prev_port + 1
        return PROXY_BASE_PORT


if __name__ == "__main__":
    pass
