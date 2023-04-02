#air03 chercher l'intrus
import sys
tamere=[]
for i in sys.argv :
    tamere.append(i)
for i in tamere:
    if tamere.count(i)%2==0:
        tamere.remove(i)
        tamere.remove(i)

for i in tamere:
    print(i)
