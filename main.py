# This program will help us make decision about whether one is adult or child
name = str(input("Tell us your name: "))

age = int(input("Hello "+name.upper()+" "+ "How old are you?: "))
if age <= 80 and age <=100:
    print ("hey! " + name.capitalize()+" "+ "you are older than your father")
elif age <= 79 and age >=40:
    print("Hurray! "+ name.upper() +" "+ "life has just begun," + " "+"welcome to adulthood")
elif  age <=39 and age  >=18:
    print("Hello "+ name.upper()+" "+ "you are still in your youthful age")
elif age <1:
    print("Hi " + name.capitalize()+" "+ "no wonder you are in your mum's womb" )
else:
    print("Hello "+ name.upper()+" "+ "you are still  a child of your father")


