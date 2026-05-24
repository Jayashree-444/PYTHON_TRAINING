
n=int(input("enter the amount:"))
notes=[100,50,20,5,2,1]
print("Mininum number of notes")
for note in notes:
    count=n//note
    if count>0:
        print(note,":",count)
        n=n%note

