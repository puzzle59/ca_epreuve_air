#fusionner deux tableaux triés
#######################################################
import sys
def position_elt_array(array,element):
    for i in range(len(array)):
        # print(f"element<=array[i]{element<=array[i]}")
        # print(f"array[i]:{array[i]}")
        # print(f"le type d'élements est.... str ? {type(element)}")
        if element<=array[i]:
            return i
    print(f"ce n'est pas entré dans la boucle, ça doit se mettre à la fin")
    return len(array)

def insert_array(array,new_element):
    if new_element in array:
        return array
    # print(f"array:{array}")
    i=position_elt_array(array,new_element)
    # print(f"position à insérer{i}")
    array=array[:i]+[new_element]+array[i:]
    return array

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
         print(array3)
    return array3
#je rencontre un problème , je ne vois pas comment utiliser mon programme précédent
#peutêtre le moment de faire une pause
#j'ai le problème quand j'importe la function, que ça gère les arguments
#du coup la flemme je vais faire moins classe et juste recopier la function
big_array=sys.argv[1:]
index=big_array.index("fusion")
array1=big_array[:index]
for i  in range(len(array1)):
    array1[i]=int(array1[i])

array2=big_array[index+1:]
for i  in range(len(array2)):
    array2[i]=int(array2[i])
print(type(array1[2]))
print(array2)
print(sorted_fusion(array1,array2))
