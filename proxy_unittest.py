"""proxy service unit test
"""

import sys
import unittest

from proxy import SessionId, Session, SessionDispatcherServiceHelper
from proxy import PROXY_BASE_PORT, STARTING_GLOBAL_UNIQUE_ID


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

        # requesting a new session should result in recycling an older session port
        sess5 = helper.request_new_session(self.service_name)
        self.assertEqual(sess5.unique_id, STARTING_GLOBAL_UNIQUE_ID + 4)
        self.assertEqual(sess5.port, sess3_port_saved_for_later)
        self.assertEqual(sess5.service_name, self.service_name)


if __name__ == "__main__":
    unittest.main(verbosity=0)
