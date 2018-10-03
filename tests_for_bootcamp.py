import pytest
import unittest
from LF import LF

class TestRatings(unittest.TestCase):

#    def setUp(self):
#       register = Register()
#       register.register_user()
#      login= Login()
#      bootcampers = [1,2,3,4,5,6,8]
#     lf  = LF()
    
    
    def test_registration(self):
        
        user_notHin = ["my_name","password"]
        user_lfa = ["lfa_name","lfa_password","LFA"]
        user_lf = ["lf_name","lf_password","LF"]
        self.assertEqual("User Registered", Register())

    def test_empty registration(self):
        empty_user = []
        self.assertEquals("Please Enter Information",Register([]))

    def 

        
