username = input("Enter username: ")

length = len(username)

has_space = False
has_digit = False
has_special = False

special_characters = "@#$%^&*!"

# Check username length
if length < 5:
    print("Username is too short")
    
elif length > 15:
    print("Username is too long")

else:

    # Check each character
    for ch in username:

        # Check spaces
        if ch == " ":
            has_space = True

        # Check digits
        if ch.isdigit():
            has_digit = True

        # Check special characters
        if ch in special_characters:
            has_special = True

    # Validation results
    if has_space:
        print("Username should not contain spaces")

    elif has_special:
        print("Username should not contain special characters")

    elif not has_digit:
        print("Username should contain at least one number")

    else:
        print("Valid username")
        print("Username accepted successfully")
