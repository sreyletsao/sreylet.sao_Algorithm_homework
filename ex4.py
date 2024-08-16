# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# text = "3 4 5 6"
# count=0
# for i in range(len(text)):
#     if text[i]!= " ":
#         count+=len(text[i])
# print(count)

# Q2 - Sum all number (Total: 18)
text = "3 4 5 6"
sum=0
for i in range(len(text)):
    if text[i]!=" ":
        sum+=int(text[i])
print(sum)
