#mock behavior of django db function- simulate db available and not available
from unittest.mock import patch
from django.core.management import call_command
#operation error when db unavailable
from django.db.utils import OperationalError
from django.test import TestCase

#see commands folder in core
class CommandTests(TestCase):
    #what happens when command called and db is already available
    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        #override behavior of connection handler, and make it return True everytime called
        #func is getitem to retreive the db, which behavior is mocked using patch
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #when called, return True INSTEAD of executing
            gi.return_value = True
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 1)

    #patch passess in arg ts. Replaces behavior of time.sleep with returning True. Doing this will speed up the test.
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        #if connection handler receives an operational error, wait and try again
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #set a side effect- raise error 5 times, and continues at 6th time and not raise the error 
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 6)


