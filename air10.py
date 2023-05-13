#10 Afficher le contenu
#Fichier à afficher : jedanselemia.txt
#################################"
import sys
def ouvrir(url):
    try: fichier=open(url,"r")
    except FileNotFoundError:
        quit("Le fichier n'existe pas")
    print(fichier.read())
    fichier.close()
if __name__=="__main__":

    url=sys.argv[1]
    ouvrir(url)