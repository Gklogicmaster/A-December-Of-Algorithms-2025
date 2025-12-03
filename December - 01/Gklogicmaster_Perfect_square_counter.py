a=int(input(""))
count = 0
for i in range (1,a):
    if((i**2)<=a):
        print(i**2,end=" ")
        count +=1
print("\n")
print(count)