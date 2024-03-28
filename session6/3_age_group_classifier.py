age = int(input("Your age:"))

if (age <= 12):
    print("child")
elif(age <= 19):
    print("Teenager")
elif(age >= 20):
    print("Adult")
elif(age < 0 and age > 150):
    print("yang bener aja, input yang ebner!")
else:
    print("meninggal aja")
