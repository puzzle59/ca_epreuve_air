#un seul à la fois
import sys
def nonauxadjacants(string):
#     tableau=[]
#     for i in string:
#         if i!=" ":
#             tableau.append(i)
#     print(tableau)
#     tableau_bis=tableau.copy()
#     for t in tableau:
#         if tableau_bis[tableau.index(t):tableau.index(t)+3].count(t)>=2:
#             tableau_bis.remove(t)
#     string=""
#     print(tableau_bis)
#     for t in tableau_bis:
#         string+=t
#     print(string)
    res=string[0]

    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            res+=string[i]
    print(res)
if __name__=="__main__":
    string=sys.argv[1]
    nonauxadjacants(string)
