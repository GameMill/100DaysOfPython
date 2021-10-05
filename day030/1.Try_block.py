# try:
#     file = open("a_file.exe")
#     # a_dictionary = {"key":"value"}
#     # print(a_dictionary["error"])
# except FileNotFoundError:
#     file = open("a_file.exe","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

#     raise TypeError("This is an error that i made up")


height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")
weight = int(input("Weight: "))




bmi = weight / height**2
print(bmi)