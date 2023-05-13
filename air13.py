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
from air01 import fonction
from air02 import concat
from air03 import intru
from air04 import nonauxadjacants
from air05 import operation
from air06 import controlepasssanitaire
from air07 import insert_array
from air08 import sorted_fusion

##########################################################################""
import io
import sys
import unittest

class   TestMaFunction(unittest.TestCase):
    def test_split(self):
        self.assertEqual(air00.split("le champignon"," "),["le","champignon"])
        print("air00 (2/2) successfull(1/)")
class DeuxiemeTest(unittest.TestCase):
    def test_str(self):
        self.assertIsInstance("le champignon",str)
        print("air00 (1/2) successfull (2/)")
###################################################################
class air01(unittest.TestCase):
    def testcrevettemagique(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        fonction("coucou la crevette magique","la")
        sys.stdout = sys.__stdout__ # Reset stdout to its default value
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"coucou \n crevette magique")
        print("air01 (1/2) successfull (3/)")

    def testchouchoulebichon(self):
        captured_output= io.StringIO()
        sys.stdout = captured_output
        fonction("mon chien est beau, ma soeur est belle","est")
        sys.stdout= sys.__stdout__
        output= captured_output.getvalue().strip()
        self.assertEqual(output,"mon chien \n beau, ma soeur \n belle")
        print("air01 (2/2) successful (4/)")
###################################################################
class air02(unittest.TestCase):
    def testsalutlescopains(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        concat("salut les copains"," ")
        sys.stdout = sys.__stdout__ # Reset stdout to its default value
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"salutlescopains")
        print("air02 (1/2) successfull (5/)")

    def testegal(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        concat("coucou ça va"," ")
        sys.stdout = sys.__stdout__ # Reset stdout to its default value
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"coucouçava")
        print("air02 (2/2) successfull (6/)")
#########################################################################
class air03(unittest.TestCase):
    def testair031(self):
        captured_output= io.StringIO()
        sys.stdout= captured_output
        intru([0,1,2,3,4,5,4,3,2,1,0])
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"5")
        print("air03 (1/2) successful (7/)")
    def testair032(self):
        captured_output= io.StringIO()
        sys.stdout= captured_output
        intru(["bonjour","monsieur","bonjour"])
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"monsieur")
        print("air03 (1/2) successful (8/)")
#########################################################################
class air04(unittest.TestCase):
    def testair041(self):
            captured_output= io.StringIO()
            sys.stdout= captured_output
            nonauxadjacants("hello milady,   bien ou quoi??")
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            self.assertEqual(output,"helo milady, bien ou quoi?")
            print("air05 (1/2) successful (9/)")
#########################################################################
class air05(unittest.TestCase):    
    def testair051(self):
        captured_output= io.StringIO()
        sys.stdout= captured_output
        operation([1,2,3,4],"+1")
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"2 3 4 5")
        print("air03 (1/2) successful (10/")
    def testair052(self):
        captured_output= io.StringIO()
        sys.stdout= captured_output
        operation([1,2,3,4],"/0")
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"division par zero impossible")
        print("air05 (2/2) successful (11/)")
###########################################################################
class air06(unittest.TestCase):
    def testair061(self):
        self.assertEqual(controlepasssanitaire(["Michel","Albert","josé","mowgli","Timéon"],"t"),["Michel","josé","mowgli"])
        print(" air06 (1/1) successful(12/)")
###########################################################################
class air07(unittest.TestCase):
    def testair071(self):
        self.assertEqual(insert_array([1,2,3,4,5,8,9],7),[1,2,3,4,5,7,8,9])
        print("air 07 (1/1) successful(13/)")
########################################################################"#"
class air08(unittest.TestCase):
    def testair081(self):
        self.assertEqual(sorted_fusion([1,2,4,8,9],[3,5,10]),[1,2,3,4,5,8,9,10])
        print("air 08 (1/1) successful (14/)")

if __name__=="__main__":
    unittest.main()