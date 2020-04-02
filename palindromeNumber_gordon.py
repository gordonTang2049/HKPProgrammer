def palindromeNum(input) :
    strNum = str(input)
    numList = [num for num in strNum]  
    return numList == numList.reverse()


print(palindromeNum(123))





