file_name = "my_file.txt"

# Reading the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing to the file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#Opening a File that doesn't exit in write mode will create it from scratch
with open("new_file.txt", mode="w") as file:
    file.write("New file")