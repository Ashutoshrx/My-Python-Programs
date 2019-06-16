
def reverse(a):
    b = ""
    for i in a:
       b=i+b
    print(b)
    if a == b:
        print("It's is in palindrome")
    else:
        print("NOT palindrome")

a=input("Enter the string:")
reverse(a)

