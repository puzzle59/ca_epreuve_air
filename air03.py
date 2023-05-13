#air03 chercher l'intrus
import sys
def intru(tableau):

    # print(tableau)
    # for item in tableau:
    #     print(f"{item}:{tableau.count(item)}")
    #     print("1" in tableau)
    #     if tableau.count(str(item))%2==0:
    #         tableau.remove(str(item))
    #         tableau.remove(str(item))
        
    # for i in tableau:
    #     print(i)
    tableaubis=[]
    for item in tableau:
        if tableau.count(item)%2==1:
            tableaubis.append(item)
    for item in tableaubis:
        print(item,end=" ")
if __name__=="__main__":
    tableau=sys.argv[1:]
    for item in tableau:
        item=str(item)
    intru(tableau)
############ je ne comprends pas il me dit que 1 n'est pas dans le tableau 