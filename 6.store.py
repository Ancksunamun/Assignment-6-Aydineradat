



def show_menu():
    print( ' 1-Add product \n 2-Edit product \n 3-Delete product \n 4-search \n 5-Show list \n 6-Buy\n 7-Creat Qrcode \n 8-Exit ')
show_menu()
choice= int (input("Please enter your choice:"))
PRODUCTS=[]
def load():
    myfile= open('database.txt','r')
    data=myfile.read()
    product_list=data.split('\n')

    for i in range(len(product_list)):
        product_info= product_list[i].split(',')
        mydict = {}
        mydict['id']=product_info[0]
        mydict['name']=product_info[1]
        mydict['price']=product_info[2]
        mydict['amount']=product_info[3]
        PRODUCTS.append(mydict)

load()
def edit_product():
    name=input("Please enter the name of product you want to edit:")
    correctchoice=0
    for i in range (len(PRODUCTS)):
        if PRODUCTS[i]['name']==name:
            correctchoice==1


            editchoice= int(input("For editing id plz enter 1 for pass enter 2"))
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
            if editchoice == 1:
                editamount = int(input("Please enter new amount:"))
                PRODUCTS[i]['amount'] = editamount
            if editchoice == 2:
                pass
    if correctchoice==0:
        print('That item is not inventory')
    print(PRODUCTS)

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
    del delete
    if correctchoice==0:
        print("that item is not inventory")
    print(PRODUCTS)
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
    while True:
        buyname=int(input("Please enter id of product you want to buy:"))
        correctchoice=0
        for i in range(len(PRODUCTS)):
            if buyname==PRODUCTS[i]['id']:




if choice==1:
    add_list()
elif choice==2:
    edit_product()
elif choice==3:
    delete_product()
elif choice==4:
    search()
elif choice==5:
    show_list()
elif choice==6:
    pass
elif choice==7:
    pass
elif choice==8:
    pass

