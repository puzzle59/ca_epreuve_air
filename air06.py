#controle pass sanitaire
import sys
tableau=[]
for i in sys.argv[1:-1]:
    tableau.append(i.lower())
    if i.count(sys.argv[-1].lower())<1:
            tableau.remove(i)
print(tableau)
