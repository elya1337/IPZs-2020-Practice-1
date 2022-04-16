def isPalindrome(s):
    for i in range(len(s) // 2 + 1):
        if(s[i] != s[len(s) - 1 - i]):
            return False
    else:
        return True

str = input("Incoming data: ")
print("Palindroms: ")
for i in str.split():
    if (isPalindrome(i)):
        print(i)
