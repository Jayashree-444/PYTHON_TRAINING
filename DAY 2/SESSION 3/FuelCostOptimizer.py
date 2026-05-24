distance=int(input("enter the distance:"))
millage=int(input("enter the km per liter:"))
fprice=int(input("enter the price: "))
charges=int(input("enter the amount,one way: "))
wage=int(input("enter the wages per day: "))
budget=int(input("enter the budget: "))
Nd=int(input("enter the days number: "))
Fuelc=(distance/millage)*fprice
dc=wage*Nd
tc=Fuelc+charges+dc
if tc>budget:
    print(tc-budget)
    print("OVER BUDGET")
else:
    print("Within budget")
