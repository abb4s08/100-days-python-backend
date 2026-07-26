tsec=int(input("Enter the total number of seconds: "))
hour=tsec//3600
min=(tsec%3600)//60
sec=(tsec%3600)%60
print(f"{hour}:{min}:{sec}")

