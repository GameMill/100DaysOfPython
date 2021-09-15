
print("#"*50)
print(" Order a Pizza ".center(50,"#"))
print("#"*50)
print("")

your_name = input("What is your name? ")
their_name = input("What is their name? ") 

true = ["t","r","u","e"]
love = ["l","o","v","e"]

part1 = 0
for i in range(4):
    part1 += your_name.lower().count(true[i])
    part1 += their_name.lower().count(true[i])

part2 = 0
for i in range(4):
    part2 += your_name.lower().count(love[i])
    part2 += their_name.lower().count(love[i])

total_precentage = int(str(part1)+str(part2))

if total_precentage < 10 or total_precentage > 90:
    print(f"You score is {total_precentage}%, you go together like coke and mentos.")
elif total_precentage > 40 and total_precentage < 50:
    print(f"You score is {total_precentage}%, you are alright together.")
else:
    print(f"Your score is {total_precentage}%")

