age = input ("How old are you?")
try:
    output = int(age)/2
except:
    print("You didnt use a number")
else:
    print(f"Half your age is {int(age)/2}")