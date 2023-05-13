import sys
def split(string_to_separate,separator):
    piece=""
    tableau=[]
    n=len(string_to_separate)
    i=0
    for letter in string_to_separate:
        piece+=letter
        if letter == separator:
            tableau.append(piece[:-1])
            piece=""
        i+=1
        if i==n:
            tableau.append(piece)
    return tableau# else:
if __name__ == '__main__' :
    
    string_to_separate= sys.argv[1]
    string_to_separate=sys.argv[1]
    if len(sys.argv)>2:
        separator=sys.argv[2]
    else:
        separator=" "

    for item in split(string_to_separate," "):
        print(item)
# pb quand 2 séparateurs à la suite , affiche un chiffre..
