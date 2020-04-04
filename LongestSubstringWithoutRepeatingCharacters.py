input1 = "abcabcbb"
input1Set = set(input1)
input2 = "bbbbb"
input2Set = set(input2)
input3 = "pwwkew"
input3Set = set(input3)


def displayAnwser(setStr) :
    return 'The answer is "%s" with the length of %s' %("".join(sorted(setStr)), len(setStr))
    

print(displayAnwser(input1Set))
print(displayAnwser(input2Set))
print(displayAnwser(input3Set))



