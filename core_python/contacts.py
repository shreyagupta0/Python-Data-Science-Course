from pprint import pp

contacts = {'emergency':112 }
while True:
    #menu
    print('1.Add contact')
    print('2.View contact')
    print('3.Delete contact')
    print('4.exit')
    print("select a number")
    ch = int(input("enter your choice: "))
    if ch == 1:
        name = input('enter name')
        number = input('enter number')
        contacts[name] = number
        print("contact saved")
    elif ch==2:
         pp(contacts,width=1)
    elif ch == 3:
        name=input('enter name')
        if name in contacts:
            contacts.pop(name)
            print('contact deleted')
    elif ch == 4:
        break
    else:
        print('invalid choice')             




