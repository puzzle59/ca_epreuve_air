import sys
def concat(array_string,separator):
    for item in array_string[:-1]:
        print(f"{item}{separator}",end="")
    print(f"{array_string[-1]}",end="")
array_string=[]
for element in sys.argv[1:-1]:
    if isinstance(element,str):
        array_string.append(element)
separator=sys.argv[-1]
concat(array_string,separator)
