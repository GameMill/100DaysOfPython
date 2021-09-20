def safe_number_input_with_lenght(text,min,max,lenght):
    try:
        user_input = str(int(input(text).strip()))
        if(len(user_input) == lenght):
            for i in range(lenght):
                if int(user_input[i]) < min or int(user_input[i]) > max:
                    print("Invalid input")
                    return safe_number_input_with_lenght(text,min,max,lenght)  
            return user_input
        print("Invalid input")
        return safe_number_input_with_lenght(text,min,max,lenght)  
    except print(0):
        print("Invalid input")
        return safe_number_input_with_lenght(text,min,max,lenght)
    

row1 = ['⬜️','⬜️','⬜️']
row2 = ['⬜️','⬜️','⬜️']
row3 = ['⬜️','⬜️','⬜️']

board = [row1,row2,row3]

print(f"{board[0]}\n{board[1]}\n{board[2]}")

data = safe_number_input_with_lenght("Please input a space to put the Treasure: ",1,3,2)
board[int(data[0])-1][int(data[1])-1] = "X"
print(f"{board[0]}\n{board[1]}\n{board[2]}")