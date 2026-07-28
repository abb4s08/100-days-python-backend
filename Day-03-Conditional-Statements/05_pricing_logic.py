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
