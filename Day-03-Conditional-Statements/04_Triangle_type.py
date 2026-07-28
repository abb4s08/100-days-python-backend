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