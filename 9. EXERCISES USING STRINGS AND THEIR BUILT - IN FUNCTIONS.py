def strlen(s):
    counter = 0
    for i in s:
        counter += 1
    return counter

def strrev(s):
    rstr = ""
    l = strlen(s)
    while l > 0:
        rstr = rstr + s[l-1]
        l -= 1
    return rstr

def strcat(st1, st2):
    return st1 + st2

def strcmp(st1, st2):
    if st1 == st2:
        print(st1 + " and " + st2 + " are same")
    elif st1 > st2:
        print(st1 + " comes after " + st2 + " in the Dictionary")
    else:
        print(st1 + " comes before " + st2 + " in the Dictionary")

print("""String Functions:
1.String Length
2.String Reverse
3.String Concatenation
4.String Comparison
5.Exit
""")

while True:
    n = int(input("Enter your choice: "))

    if n == 1:
        s = input("Enter a string: ")
        print("Length of the string is:", strlen(s))

    elif n == 2:
        s = input("Enter a string: ")
        print("Reversed string is:", strrev(s))

    elif n == 3:
        st1 = input("Enter the first string: ")
        st2 = input("Enter the second string: ")
        print("Concatenated string is:", strcat(st1, st2))

    elif n == 4:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        strcmp(str1, str2)

    elif n == 5:
        print("Exited")
        break

    else:
        print("Invalid choice")

