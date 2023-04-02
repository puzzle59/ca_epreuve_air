#insertion dans array trié
#######################################################""
#je me suis refait avoir à pas avoir converti les entiers...
import sys
def position_elt_array(array,element):
    for i in range(len(array)):
        print(f"element<=array[i]{element<=array[i]}")
        print(f"array[i]:{array[i]}")
        print(f"le type d'élements est.... str ? {type(element)}")
        if element<=array[i]:
            return i
    print(f"ce n'est pas entré dans la boucle, ça doit se mettre à la fin")
    return len(array)

def insert_array(array,new_element):
    if new_element in array:
        return array
    print(f"array:{array}")
    i=position_elt_array(array,new_element)
    print(f"position à insérer{i}")
    array=array[:i]+[new_element]+array[i:]
    return array

#Vérification du type d'argument
for integer in sys.argv[1:]:
    try: integer=int(integer)
    except ValueError:
        quit("merci de mettre des entiers")
array=[]
for i in sys.argv[1:-1]:
    array.append(int(i))

#Vérification que le tableau d'entrée est trié
if not array==sorted(array.copy()):
    quit("veuillez entrer un array trié svp")
new_element=int(sys.argv[-1])
print(insert_array(array,new_element))
