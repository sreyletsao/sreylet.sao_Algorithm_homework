# Ex5 - String 
# Q1 - Count odd and even number in text
# text = "454639"
# count_odd=0
# count_even=0
# for i in range(len(text)):
#     if int(text[i])%2==1:
#         count_odd+=1
#     if int(text[i])%2==0:
#         count_even+=1
# print(count_even)
# print(count_odd)


# Q2 - Sum all number 
# text = "454639"
# sum=0
# for i in range(len(text)):
#     sum+=int(text[i])
# print(sum)


# Q3 - Sum only even number
# text = "454639"
# sum_even=0
# for i in range(len(text)):
#     if int(text[i])%2==0:
#         sum_even+=int(text[i])
# print(sum_even)


# Q4 - Reverse
text = "454639"
result = " "
for i in range (len(text)):
    result +=(text[len(text)-1-i])
print(result)

