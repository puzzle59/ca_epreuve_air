#11 AFFICHER UNE PYRAMIDE
import sys
def pyramide(charac,n_etages):
    total_fin_de_ligne=2*n_etages-1
    tableau=[[ " " for i in range(total_fin_de_ligne)] for j in range(n_etages)]
    milieu=(total_fin_de_ligne)//2
    for i in range(n_etages):
        for j in range(total_fin_de_ligne):
            for k in range(milieu -i,milieu +1+i):
                tableau[i][k]=charac

    for item in  tableau:
        for element in item:
            print(element,end="")
        print("",end="\n")
if __name__=="__main__":
    charac=sys.argv[1]
    n_etages=int(sys.argv[2])
    pyramide(charac,n_etages)
#éventuellement pourquoi espace entre les lignes ?
#comprends pas car \n est le retour à la ligne classique, pas deux . donc sais pas
