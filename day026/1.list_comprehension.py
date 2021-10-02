
number = [1,2,3]
new_list = []
for n in number:
    new_list.append(n+1)

print(new_list)

new_list = [n+1 for n in new_list]
print(new_list)


name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_list = [num*2 for num in range(1,5)]
print(new_list)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
new_list = [name for name in names if len(name) < 5]
print(new_list)

new_list = [name.upper() for name in names if len(name) >= 5]
print(new_list)
