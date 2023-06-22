import getpass
dataBase = {
    "beto.gaytan": "123456",
    "karla.guevara": "987654"
}

userName = input("Enter your Username: ")
pwd = getpass.getpass("Enter Your Password: ")

for user in dataBase.keys():
    if userName == user:
        while pwd != dataBase.get(user):
            pwd = getpass.getpass("Enter Your Password Again: ")
        break

print("Verified")