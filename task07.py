email = input("Email kiriting: ")

if email.startswith("eldorjon") and "@" in email and "." in email and " " not in email:
    print("Email to'g'ri")
else:
    print("Email noto'gri")



# eldorjon@gmail.com degan email to'g'ri bitta qolgan qanaqa email kiritilsa ham noto'g'ri.
