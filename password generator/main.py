import random

if __name__ == '__main__':

    while True:

        length = int(input("length: "))
        password = "" \
                   ""
        securityType = int(input("""
1 for numbers only 
2 for regular letters only 
3 for numbers and regular letters
4 for numbers and symbols and regular letters
5 for all unicode characters
type: """))

        if securityType == 1:
            for i in range(length):
                password += str(random.randint(0, 9))

        elif securityType == 2:
            for i in range(length):
                add = random.randint(65, 122)
                while 91 <= add <= 96:
                    add = random.randint(65, 122)
                password += str(chr(add))

        elif securityType == 3:
            for i in range(length):
                add = random.randint(48, 122)
                while 91 <= add <= 96 or 58 <= add <= 64:
                    add = random.randint(48, 122)
                password += str(chr(add))

        elif securityType == 4:
            for i in range(length):
                password += str(chr(random.randint(33, 126)))

        elif securityType == 5:
            for i in range(length):
                password += str(chr(random.randint(0, 10000)))

        else:
            password = "out of range"

        print(password)
