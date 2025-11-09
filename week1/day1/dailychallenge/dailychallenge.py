#. **Ask for User Input:**
#- The string **must be exactly 10 characters long**.
#2. **Check the Length of the String:**
#- If the string is **less than 10 characters**, print: `"String not long enough."`
#- If the string is **more than 10 characters**, print: `"String too long."`
#- If the string is **exactly 10 characters**, print: `"Perfect string"`
#  and proceed to the next steps.

user_info = input('Please type your name ')
len(user_info)

if len(user_info) < 10:
    print("String not long enough.")

if len(user_info) > 10:
    print('String too long.')

if len(user_info) == 10:
    print('Perfect string.')