# #fichier test
# import sys,subprocess,os
# # exec(air01.py)
# # status=(subprocess.call("air00.py" +"salut les copains",shell=True))
# # cmd="python3 air00.py None 'bonjour les gars'"
# from air00 import split
# try: assert(split("bonjour les gars"," ")==["bonjour","les","gars"])
# # try: assert("bg"=="bg")
# except AssertionError:
#     test="failure"
# else:
#     test="success"
# print(test)

# try:assert(split("le champignon", "")==["lechampignon"])
# except AssertionError:
#     test2="success"
# else:
#     test2="failure"
# print(test2)
import unittest
import air00
from air02 import concat
# air03,air04,air05,air06,air07,air08,air09,air10,air11,air12

##########################################################################""
import io
import sys
import unittest

class TroisiemeTest(unittest.TestCase):
    def testttt(self):
        self.assertTrue(True)
        print("test air 00.py 3/3")
class TestMaFonction(unittest.TestCase):

    def test_split(self):
        self.assertEqual(air00.split("le champignon"," "),["le","champignon"])
        print("air00 (2/2) successfull")
class DeuxiemeTest(unittest.TestCase):
    def test_str(self):
        self.assertIsInstance("le champignon",str)
        print("air00 (1/2) successfull")
####################################################
class air02(unittest.TestCase):
    def testsalutlescopains(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        concat("salut les copains"," ")
        sys.stdout = sys.__stdout__ # Reset stdout to its default value
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"salutlescopains")
        print("air02 (1/2) successfull")

    def testegal(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        concat("coucou ça va "," ")
        sys.stdout = sys.__stdout__ # Reset stdout to its default value
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"coucouçava")
        print("air02 (2/2) successfull")
if __name__=="__main__":
    unittest.main()