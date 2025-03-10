# PASSWORD STRENGTH CHECKER

# Description

This Python script provides a simple way to check the strength of a password. It assesses the strength based on the following criteria:
- Length of the password
- Presence of uppercase and lowercase letters
- Presence of numbers
- Presence of special characters

# How It Works

The script defines a function 'password_strength' that takes a password string as input. It checks the password against various criteria using regular expressions and length checks. If the password fails any of the checks, the function returns a message indicating what is missing. If the password passes all the checks, it returns a message saying that the password is strong.

# Code Structure

The code consists of a single function 'password_strength(password)'. This function uses the 're' module for regular expressions to check for the presence of uppercase letters, lowercase letters, numbers, and special characters in the password.

# Usage

To use this script, you need to have Python installed on your system. You can run the script using any Python interpreter. The function `password_strength` can be imported into other Python scripts or used standalone.

# Example

python
print(password_strength("YourPassword123!"))

Replace "YourPassword123!" with the password you want to check.
