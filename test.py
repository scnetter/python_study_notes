user = input("What is your username?: ")
password = input("What is your password?:")
obscured_pw = "*" * len(password)

print(
    f"User {user} has a password of {obscured_pw} that is {len(password)} characters long."
)
