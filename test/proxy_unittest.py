"""proxy service unit test
"""

from os import path as ospath
from sys import path as syspath

import uuid
import unittest
import grpc

_UPPER_MODULE_PATH = ospath.abspath(ospath.dirname(ospath.dirname(__file__)))
syspath.append(_UPPER_MODULE_PATH)

from proxy import SessionId, Session, SessionDispatcherServiceHelper
from proxy import PROXY_MAIN_PORT, PROXY_BASE_PORT, STARTING_GLOBAL_UNIQUE_ID

import proxy_pb2
import proxy_pb2_grpc

_PROXY_SERVER_ADDRESS = 'localhost'


class SessionIdTest(unittest.TestCase):
    def test_01(self):
        sess_id = SessionId()
        self.assertEqual(sess_id.get_next(), STARTING_GLOBAL_UNIQUE_ID)
        self.assertEqual(sess_id.get_next(), STARTING_GLOBAL_UNIQUE_ID + 1)
        self.assertEqual(sess_id.get_next(), STARTING_GLOBAL_UNIQUE_ID + 2)


class SessionTest(unittest.TestCase):
    def test_01(self):
        sess_id = SessionId()
        curr_session_id = sess_id.get_next()
        sess = Session(curr_session_id, PROXY_BASE_PORT + 1, "dummy_service_name")
        self.assertEqual(sess.unique_id, curr_session_id)


class SessionDispatcherServiceHelperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service_name = 'dummy_service_name'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        helper = SessionDispatcherServiceHelper()

        # # request a session for a nonexistent service
        # sess_non_existent = helper.request_new_session(str(uuid.uuid4()))
        # self.assertIsNone(sess_non_existent)

        # request a session
        sess1 = helper.request_new_session(self.service_name)
        self.assertEqual(sess1.unique_id, STARTING_GLOBAL_UNIQUE_ID)
        self.assertTrue(sess1.port == PROXY_BASE_PORT)
        self.assertEqual(sess1.service_name, self.service_name)

        # retrieve requested session
        sess1_retr = helper.get_session(sess1.unique_id)
        self.assertIsNotNone(sess1_retr)

        self.assertIsNone(helper.get_session(sys.maxint))

        # request another session
        sess2 = helper.request_new_session(self.service_name)
        self.assertEqual(sess2.unique_id, STARTING_GLOBAL_UNIQUE_ID + 1)
        self.assertTrue(sess2.port == PROXY_BASE_PORT + 1)
        self.assertEqual(sess2.service_name, self.service_name)
        sess2_port_saved_for_later = sess2.port

        sess2_retr = helper.get_session(sess2.unique_id)
        self.assertIsNotNone(sess2_retr)

        self.assertTrue(helper.delete_session(sess2.unique_id))
        self.assertIsNone(helper.get_session(sess2.unique_id))
        self.assertFalse(helper.delete_session(sess2.unique_id))
        del sess2

        # request yet another session - the 'middle' session
        sess3 = helper.request_new_session(self.service_name)
        self.assertEqual(sess3.unique_id, STARTING_GLOBAL_UNIQUE_ID + 2)
        self.assertEqual(sess3.port, sess2_port_saved_for_later)
        self.assertEqual(sess3.service_name, self.service_name)
        sess3_port_saved_for_later = sess3.port

        # still yet another session
        sess4 = helper.request_new_session(self.service_name)
        self.assertEqual(sess4.unique_id, STARTING_GLOBAL_UNIQUE_ID + 3)
        self.assertTrue(sess4.port > sess2_port_saved_for_later)
        self.assertEqual(sess4.service_name, self.service_name)

        # delete a 'middle' session
        self.assertTrue(helper.delete_session(sess3.unique_id))
        self.assertIsNone(helper.get_session(sess3.unique_id))
        self.assertFalse(helper.delete_session(sess3.unique_id))

        # requesting a new session should result in recycling an older session port
        sess5 = helper.request_new_session(self.service_name)
        self.assertEqual(sess5.unique_id, STARTING_GLOBAL_UNIQUE_ID + 4)
        self.assertEqual(sess5.port, sess3_port_saved_for_later)
        self.assertEqual(sess5.service_name, self.service_name)

        self.assertTrue(helper.delete_session(sess1.unique_id))
        self.assertFalse(helper.delete_session(sess1.unique_id))

        self.assertTrue(helper.delete_session(sess4.unique_id))
        self.assertFalse(helper.delete_session(sess4.unique_id))

        self.assertTrue(helper.delete_session(sess5.unique_id))
        self.assertFalse(helper.delete_session(sess5.unique_id))


class SessionDispatcherServiceHelperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service_name = 'dummy_service_name'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        # helper = SessionDispatcherServiceHelper()
        try:
            insec_channel = grpc.insecure_channel("{}:{}".format(
                _PROXY_SERVER_ADDRESS, PROXY_MAIN_PORT))
            self.assertIsNotNone(insec_channel)

            session_dispatcher = proxy_pb2_grpc.SessionDispatcherStub(insec_channel)
            self.assertIsNotNone(session_dispatcher)

            resp_sess1 = session_dispatcher.Request(
                    proxy_pb2.RequestSessionRequest(
                        service_name="dummy_serv_name"))
            self.assertIsNotNone(resp_sess1)
            print(resp_sess1)

            resp_sess2 = session_dispatcher.Request(
                    proxy_pb2.RequestSessionRequest(
                        service_name="dummy_serv_name"))
            self.assertIsNotNone(resp_sess2)
            print(resp_sess2)

            resp_sess3 = session_dispatcher.Request(
                    proxy_pb2.RequestSessionRequest(
                        service_name="dummy_service_name"))
            self.assertIsNotNone(resp_sess3)
            print(resp_sess3)

            resp_release_sess2 = session_dispatcher.Release(
                    proxy_pb2.ReleaseSessionRequest(
                        session_id=resp_sess2.session_info.session_id))
            self.assertIsNotNone(resp_release_sess2)
            
        finally:
            session_dispatcher = None
            insec_channel = None


if __name__ == "__main__":
    unittest.main(verbosity=0)
