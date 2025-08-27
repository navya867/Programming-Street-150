input_string=input("")
input_string=input_string.lower()
# vowels,consonents=0,0
# if not input_string:
#     print("invalid input")
# for char in input_string:
#     if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
#         vowels+=1
#     elif(char!=" "):
#         consonents+=1
# print(f'vowels is {vowels} consonents is {consonents}')
vowels=sum(1 for char in input_string if char in "aeiou")
print(vowels)