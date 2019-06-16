#for i in range(1,5):
 #   for j in range(i):
  #      print("*",end="")
   # print()

i=1
j=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1