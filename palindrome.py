str_in = input()

str_len = len(str_in)

is_pad = True
for i in range(str_len>>1):
	if str_in[i] != str_in[str_len-i-1]:
		is_pad = False
		
print("Is Palindrome?: ", is_pad)
