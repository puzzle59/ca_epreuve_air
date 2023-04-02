#fichier test
import sys,subprocess,os
# exec(air01.py)
# status=(subprocess.call("air00.py" +"salut les copains",shell=True))
# cmd="python3 air00.py None 'bonjour les gars'"
from air00 import split
try: assert(split("bonjour les gars"," ")=='bonjour\nles\ngars\n')
except AssertionError:
    test="failure"
else:
    test="success"
print(test)
