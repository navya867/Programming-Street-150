in_str=input()
in_string=in_str[::-1]   #string slicing
print(in_string)
in_str1=''.join([in_str[i] for i in range(len(in_str)-1,-1,-1)])
print(in_str1)
in_str2=''.join(reversed(in_str))
print(in_str2)

# time comp is o(n) for all 