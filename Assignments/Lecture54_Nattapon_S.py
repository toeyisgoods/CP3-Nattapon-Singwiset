def Login():
    username=str(input("Username : "))
    password=str(input("Password : "))
    if username == "Admin" and password == "1234":
        return True
    else:
        return Login()
def ShowMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def MenuSlect():
    UserSlect=int(input(">>>"))
    return UserSlect
def VatCalculator(TotalPrice):
    vat = 7
    result = (TotalPrice * vat / 100)
    print(TotalPrice,"+ Vat ",result," ฿")
def PriceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return VatCalculator(price1 + price2)

if Login() == True:
    ShowMenu()
    if MenuSlect()==1:
        print(VatCalculator(int(input("Input total price : "))))
    else:
        print(PriceCalculator())