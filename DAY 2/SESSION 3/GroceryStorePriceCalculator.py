item=input("name the item:")
quantity=int(input("enter the quantity: "))
price=float(input("enter perice per unit:"))
member=int(input("enter 1 for membership or 0: "))
subTotal=quantity*price
print("sub Total: ",subTotal)
discount=0
if member==1:
    discount=subTotal*0.10
subTotal=subTotal-discount
if subTotal>500:
    gst=subTotal*0.05
else:
    gst=subTotal*0.12
total=subTotal+gst
print("Item name",item)
print("sub Total: ",subTotal)
print("discount:",discount)
print("Gst",gst)
print("Total",total)