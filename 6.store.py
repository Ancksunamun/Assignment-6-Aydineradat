import qrcode

def show_menu():
    print(' 1-Add product \n 2-Edit product \n 3-Delete product \n 4-search \n 5-Show list \n 6-Buy\n 7-Creat Qrcode \n 8-Exit ')

PRODUCTS = []

def load():
    myfile = open('database.txt','r')
    data = myfile.read()
    product_list = data.split('\n')

    for i in range(len(product_list)):
        product_info= product_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = int(product_info[2])
        mydict['amount'] = int(product_info[3])
        PRODUCTS.append(mydict)

load()
def edit_product():
    name=input("Please enter the name of product you want to edit:")
    correctchoice=0
    for i in range (len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name:
            correctchoice == 1


            editchoice = int(input("For editing id plz enter 1 for pass enter 2"))
            if editchoice ==1:
                editid= int(input("Please enter new id:"))
                PRODUCTS[i]['id']=editid
            if editchoice==2:
                pass
            editchoice = int(input("For editing price plz enter 1 for pass enter 2"))
            if editchoice == 1:
                editprice = int(input("Please enter new price:"))
                PRODUCTS[i]['price'] = editprice
            if editchoice == 2:
                pass
            editchoice = int(input("For editing amount plz enter 1 for pass enter 2"))
            if editchoice == 1:
                editamount = int(input("Please enter new amount:"))
                PRODUCTS[i]['amount'] = editamount
            if editchoice == 2:
                pass
    if correctchoice==0:
        print('That item is not inventory')

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
def add_list():
    new_id=int(input("Please enter new id:"))
    new_name=input("Please enter the name of product:")
    new_price=int(input("Please enter the price of product:"))
    new_amount=int(input("Please enter the amount of product:"))
    new_item = {}
    new_item['id'] = new_id
    new_item['name'] = new_name
    new_item['price'] = new_price
    new_item['amount'] = new_amount
    PRODUCTS.append(new_item)
def delete_product():
    correctchoice=0
    delete=input("Please enter the name of product you want to delete:")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==delete:
            PRODUCTS[i]= delete
            correctchoice=1
            PRODUCTS.pop(i)
            break
    if correctchoice==0:
        print("that item is not inventory")
def search():
    searchh=input("Please enter the name of product you are looking for:")
    correctchoice=0
    for i in range(len (PRODUCTS)):
        if PRODUCTS[i]['name']== searchh:
            print(PRODUCTS[i])
            correctchoice=1

    if correctchoice==0:
        print("That item is not in inventory")
def buy():
    bill = []
    while True:
        buyname=input("Please enter id or name of product you want to buy:(if you are done with buying enter exit)")
        correctchoice=0


        for i in range(len(PRODUCTS)):
            if str(PRODUCTS[i]['id'])==buyname or PRODUCTS[i]['name']==buyname:
                correctchoice=1
                howmany=int(input("how many do you want to buy?"))
                if howmany <= PRODUCTS[i]['amount']:
                    PRODUCTS[i]['amount']=int(PRODUCTS[i]['amount']) - howmany
                    buylist = {}
                    buylist['id']=PRODUCTS[i]['id']
                    buylist['name']=PRODUCTS[i]['name']
                    buylist['price']=PRODUCTS[i]['price']
                    buylist['howmany']=howmany
                    bill.append(buylist)

                else:
                    print("that amount of product is not available")
        if buyname == 'exit':

            break
        if correctchoice==0:
            print("product is not in inventory")
    total=0
    for i in range(len(bill)):
        total += bill[i]['price'] * bill[i]['howmany']
    for j in range(len(bill)):
        print(bill[j])
    print('Your total price:',total)


def exit1():
    myfile = open('database.txt', 'w')
    for i in range(len(PRODUCTS)):
        ids= str(PRODUCTS[i]['id'])
        name=str(PRODUCTS[i]['name'])
        price=str(PRODUCTS[i]['price'])
        amount=str(PRODUCTS[i]['amount'])
        if i == (len(PRODUCTS)-1):
            changes = ids+','+name+','+price+','+amount
        else:
            changes = ids+','+name+','+price+','+amount+"\n"
        myfile.write(changes)
    exit()
def qr_code():
    correct_choice=0
    userchoice=input("Please enter the name or id of product you want to make QRcode:")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == userchoice :
            correct_choice=1
            img = qrcode.make(PRODUCTS[i]['id'])
            img.save('qrcode' + PRODUCTS[i]['id'] + '.png')
    if correct_choice==0:
        print("product not found")





while True:
    show_menu()
    choice = int(input("Please enter your choice:"))
    if choice==1:
        add_list()
        choice = 9
    elif choice==2:
        edit_product()
        choice = 9
    elif choice==3:
        delete_product()
        choice = 9
    elif choice==4:
        search()
        choice = 9
    elif choice==5:
        show_list()
        choice = 9
    elif choice==6:
        buy()
        choice = 9
    elif choice==7:
        qr_code()
        choice = 9
    elif choice==8:
        exit1()
        choice = 9
    else:
        pass

