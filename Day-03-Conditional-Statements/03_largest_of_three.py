n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
n3=int(input("Enter the number3: "))
if n1>n2 and n1>n3:
    print(f"Largest: {n1}")
elif n2>n3 and n2>n1:
    print(f"Largest: {n2}")
else:
    print(f"Largest: {n3}")  
   