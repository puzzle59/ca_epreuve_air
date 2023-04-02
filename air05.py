#opérations sur une chaine de caractèrevie
import sys
tableau=[]
for i in sys.argv[1:-1]:
    try: i=int(i)
    except ValueError:
        quit("et vas y met des chiffres stp")
    tableau.append(i)
last_element=sys.argv[-1]
liste=last_element.split()
number="".join(liste[0][1:])
for t in tableau:
    tableau[tableau.index(t)]=int(t)
if number!='':
    number=int(number)
if liste[0][0]=="+":
    for i in range(len(tableau)):
        tableau[i]+=number
if liste[0][0]=="-":
    for i in range(len(tableau)):
        tableau[i]-=number
if liste[0][0]=="*":
    for i in range(len(tableau)):
        tableau[i]*=number
if liste[0][0]=="/":
    try: 15/number
    except ZeroDivisionError:
        print("nique ta mere ")
    else:
        for i in range(len(tableau)):
            tableau[i]/=number


print(tableau)
