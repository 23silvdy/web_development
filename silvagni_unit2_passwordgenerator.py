import random

web = input("Enter a  website: ").replace("a", "@")
num = random.randint(0, 34534)
second_varible = input("What do you use the website for?: ").replace(" ", "")
print(f"{web}{num}{second_varible[0:5]}")