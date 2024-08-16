#Ex3 - String
#Enter text and check if it contains capital letter or not
user_input = input("Input text: ")
is_capital = False
for i in range(len(user_input)):
    if user_input[i]==user_input[i].upper():
        is_capital = True
if is_capital:
    print("Yes")
else:
    print("No")
