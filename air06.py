#controle pass sanitaire
import sys
def controlepasssanitaire(tableau,string):
    for i in tableau:
        if i.lower().count(string.lower())!=0:
            tableau.remove(i)
    return tableau
if __name__=="__main__":
    string=sys.argv[-1]
    tableau=[]
    for i in sys.argv[1:-1]:
        tableau.append(i)
    for item in controlepasssanitaire(tableau,string):
        print(item,end=" ")
    
