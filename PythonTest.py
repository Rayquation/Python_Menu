Items=[("Hamburger",10),("Sandwich",5),("Soup",5),("Turkish Kebab",10),("Dry Bean",5),("Rice",5),("Chicken",5),("Doner",10)]
Orders=[]
choice="y"
Value=[]
i=1
for x in Items:
    print("%-15s %-5s %4s"%(x[0],"Tryk på "+str(i),str(x[1])+" Kr")),
    i+=1

while(choice=="y"):
    print("Vælg noget for menuen"),
    answer=int(input())
    print("Hvor mange ting"),
    answer2=int(input())
    saldo=Items[answer-1][1]*answer2
    Value.append(saldo+saldo*0.25)
    Orders.append((Items[answer-1][0],answer2))
    print("Tilvalgte mad: "+Items[answer-1][0])
    print("Pris med moms: "+str(saldo+saldo*0.25)+" Kr")
    print("Vil du fortsætte y/n"),
    choice=input()
val=0
if (choice=="n"):
    for x in Orders:
        print(x[0],x[1],str(Value[val])+" Kr")
        val+=1
    print("Din saldo er på : "+str(sum(Value))+" Kr")