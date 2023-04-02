#ROTATION VERS LA GAUCHE
import sys
def rotation_gauche_tab(array):
    if len(array)<=1:
        return array
    new_array=array[1:]
    new_array.append(array[0])
    return new_array
tableau=[]
for item in sys.argv[1:]:
    tableau.append(item)
print(rotation_gauche_tab(tableau))
