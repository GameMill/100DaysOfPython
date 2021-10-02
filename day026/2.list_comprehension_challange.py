number = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [num*num for num in number]# num**2 same as num*num

print(squared_numbers)


number = [1,1,2,3,5,8,13,21,34,55]

result = [num for num in number if num % 2 == 0]

print(result)