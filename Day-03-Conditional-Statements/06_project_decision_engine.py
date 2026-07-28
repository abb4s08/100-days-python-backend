print("===== Decision Engine =====\n1. Leap Year Checker\n2. Grade Classifier\n3. Largest of Three Numbers\n4. Triangle Type Checker\n5. Pricing Calculator\n6. Exit")
choice=int(input("Enter your choice: "))
if choice==1:
    year=int(input("Enter the year: "))
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f"The {year} is leap year")
    else:
        print(f"The {year} is not a leap year")
elif choice==2:
    mark=int(input("Enter the marks: "))
    if mark < 0 or mark > 100:
        print("Invalid Marks")
    elif 90<=mark<=100:
        print("A")
    elif 80<=mark<=89:
        print("B")
    elif 70<=mark<=79:
        print("C")
    elif 60<=mark<=69:
        print("D")
    else:
        print("F")
elif choice==3:
        n1=int(input("Enter the number1: "))
        n2=int(input("Enter the number2: "))
        n3=int(input("Enter the number3: "))
        if n1>=n2 and n1>=n3:
            print(f"Largest: {n1}")
        elif n2>=n3 and n2>=n1:
            print(f"Largest: {n2}")
        else:
            print(f"Largest: {n3}") 
elif choice==4:
    s1=int(input("Enter the side1: "))
    s2=int(input("Enter the side2: "))
    s3=int(input("Enter the side3: "))
    if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
        if s1==s2==s3:
            print("Equilateral Triangle")
        elif s1==s2 or s2==s3 or s3==s1:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Invalid Triangle")
elif choice==5:
    org=float(input())
    if org>=5000:
        dis=org*(20/100)
        fin=org-dis
    elif 3000<=org<=4999:
        dis=org*(15/100)
        fin=org-dis
    elif 1000<=org<=2999:
        dis=org*(10/100)
        fin=org-dis
    else:
        dis=org*(0/100)
        fin=org-dis
    print(f"Original Amount: {org}\nDiscount: {dis}\nFinal Amount: {fin}")
elif choice == 6:
    print("Exiting Decision Engine")
else:
    print("Invalid choice")