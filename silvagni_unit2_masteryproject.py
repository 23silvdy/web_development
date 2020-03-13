first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
stid = input("Student ID: ")
n = 0
print("*************************************************")
print("*                                               *")
print(f"*\t{last_name},{first_name}\t\tID: {stid}\t*")
print("*                                               *")
print("*************************************************")

while (n != 6):
    class1 = input("Enter the next class, STOP to end: ")
    if class1 == "STOP":
        break
    classroom1 = input("Enter the room number: ")
    n = n+1
    print(f"* \tBlock {n}: {class1}\tRoom: {classroom1}\t*")