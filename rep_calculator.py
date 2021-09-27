from prettytable import PrettyTable
r = 12
w = 275

#epley formula
epley = w * (1 +(r/30))

#brzycki
brzycki = w * (36 / (37-r))

#lombardi
lombardi = w*(r**0.10)

#oconner
oconnor = w * (1 + (r/40))

def percentages(max_rep):
    list=[]
    for i in range(1, 11, 1):
#        x = int(i*max_rep*0.1)
        list.append(i*max_rep*0.1)
    return list
#print(epley)
#print(percentages(epley))

myTable = PrettyTable()
#myTable = PrettyTable(["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
for title in range (1,11,1):
    myTable.add_column(title*0.1, [])

for per in percentages(epley):
#    print(per)
    myTable.add_row(per)
print(myTable)