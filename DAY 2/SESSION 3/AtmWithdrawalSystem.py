cb=int(input("enter the current balance:" ))
wa=int(input("enter the widthdrawal amount: "))
at=int(input("enter 1 for saving or 2 for cuurent: "))
if (at==1):
    print("saving account")
else:
    print("current account")
if wa>=50000:
    print("EXCEEDS MAXIMUM LIMIT")
    if wa//100==0:
      print("ITS NOT A MULTIPLE OF 100")


