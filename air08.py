#fusionner deux tableaux triés
#######################################################
import sys
from air07 import insert_array

def sorted_fusion(array1,array2):
    #je suppose que c'est bien des entiers , que ces tableaux sont triés
    #je mettrais la ligne après
    if array1[-1]>=array2[-1]:
        array3=array1
        smaller_array=array2
    else:
        array3=array2
        smaller_array=array1
#je pensais que c'était un problème de taille de tableau mais je crois que je me suis trompé
#c'est une histoire de plus grand élement vu comment j'ai codé la function insertion

#en fait avec comment c'est codé, ça part d'une bonne idée mais il faut modifier la fonction insert
    for item in smaller_array:
         array3=insert_array(array3,item)
        
    return array3
#je rencontre un problème , je ne vois pas comment utiliser mon programme précédent
#peutêtre le moment de faire une pause
#j'ai le problème quand j'importe la function, que ça gère les arguments
#du coup la flemme je vais faire moins classe et juste recopier la function
if __name__=="__main__":
    big_array=sys.argv[1:]
    index=big_array.index("fusion")
    array1=big_array[:index]
    for i  in range(len(array1)):
        array1[i]=int(array1[i])

    array2=big_array[index+1:]
    for i  in range(len(array2)):
        array2[i]=int(array2[i])
# print(type(array1[2]))
# print(array2)
    for item in sorted_fusion(array1,array2):
        print(item,end=" ")
