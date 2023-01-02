

def view():
    with open('passwords.txt','r') as f:
        for line in f.readline():
                data = line.rstrip()
                user, pas = data.split("|")
                print("user:", user, "password:",pas)

def add():
    name =input("account name: ")
    pwd = input(" Enter password: ")

    with open('passwords.txt','a') as f:
        f.write(name + "|" + pwd + "\n" )



def login(a):
    password = "cenation"

    if a != password:
        print("Wrong password")
    else:
        print("welcome")
        while True:

            mode= input("To add details enter add, view details enter view and to quit enter q ")

            if mode =="q":
                break

            if mode == "add":
                add()
            elif mode =="view":
                view()
            else:
                print(" Invalid entry")
                continue

    
passw = input("Input login password ")
login(passw)


