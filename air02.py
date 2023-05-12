import sys
def concat(array_string,separator):
    
    for item in array_string:
        if item!=separator:
            print(item,end="")
      
if __name__ == "__main__":
    array_string=[]
    for element in sys.argv[1]:
        if isinstance(element,str):
            array_string.append(element)

    separator=sys.argv[-1]
    concat(array_string,separator)
