#12 LE ROI DES TRIS
#pivot
#c'est d'une simplicité , efficace !
##############################################################################""
import sys
import random
def partition(array,pivot):
    array1=[]
    array2=[]
    for item in array:
        if item <= pivot:
            array1.append(item)
        else:
            array2.append(item)
    return (array1,array2)

def quick_sort(array):
    if len(array)==0:
        return []
    if len(array)==1:
        return array
    if len(array)<=2:
        if array[0]<=array[1]:
            return array
        else :
            c=array[0]
            array[0]=array[1]
            array[1]=c
            return array
    pivot=random.choice(array)
    c=partition(array,pivot)
    return quick_sort(c[0])+quick_sort(c[1])

array=[]
for i in sys.argv[1:]:
    array.append(int(i))
print(quick_sort(array))
