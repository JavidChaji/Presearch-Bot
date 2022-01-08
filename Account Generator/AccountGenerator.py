import random
import string


f = open("Accounts.txt", "a")

accountNumberFile = open("Count.txt", "r")

accountNumber = int(accountNumberFile.readline())

accountNumberFile.close()
characters = string.ascii_letters + string.digits + string.punctuation



for s in range(0, accountNumber) :
    emailPart1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(10, 15)))
    emailPart2 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(7, 11)))
    f.write(emailPart1 + str(s) + emailPart2 + '@gmail.com\n')
    password = ''.join(random.choice(characters) for i in range(16))
    f.write(password +'\n')
    f.write('############  ' + str(s) + '  ############' + '\n')
            
f.close()

#open and read the file after the appending:
f = open("Accounts.txt", "r")
print(f.read())
input()