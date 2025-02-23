def check(str1):
    return str1 == str1[::-1]

str1 = input("enter the world")

result  = check(str1)


print(result)