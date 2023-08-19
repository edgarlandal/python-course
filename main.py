# Comments
# Varibles
name = "Edgar"
last_name = "Landa"
age = 23
price = 12.33
found = False

print(name + " " + last_name)
print("My age is " + str(age))
print(price)
print(found)

# Conditional 

if (age < 100):
    print("Don't worry you are still")
    print("still inside the if")
elif (age == 100):
    print("Congratulation on the century!!!")
else:
    print("Sorry, you are getting old")

print("outside the if")

def say_hello():
    print("Hello from function")

say_hello()