#  Split en fonction
import sys
#
def fonction(string,separator):
    tableau=[]
    piece=""
    i=0
    while i< len(string):
        if string[i:i+len(separator)]!=separator:
            piece+=string[i]
            i+=1
        else:
#Problème de si le séparateur est en fin de phrase
#affiche un blanc , pas de blanc ..

            tableau.append(piece)
            piece=""
            i+=len(separator)

    if i!= len(string)+1:
        tableau.append(piece)
    for item in tableau:
        print(item)
fonction(sys.argv[1],sys.argv[2])






























#
