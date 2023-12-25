import getpass

# asks for input which don't show up on console. Password or anything else.
password = getpass.getpass(prompt='Enter your password: ')
print(password)

# Looks for "Username..." variable in the current system.
user_name = getpass.getuser()
print(user_name)