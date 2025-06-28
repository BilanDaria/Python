# Function with Outputs

def format_name(name, surname):
    """Convert 2 strings into a title case version."""
    return f"{name.title()} {surname.title()}"


f_name = input("What is your first name? : ")
l_name = input("What is your last name? : ")
print(format_name(f_name, l_name))

