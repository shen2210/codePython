def enter_price_fruit(name_fruit):
    weight_fruit = float(input(f"Enter weigth {name_fruit} : "))
    return weight_fruit

def calculate_total_price(weight_fruit,FRUIT_PRICE):
    return weight_fruit*FRUIT_PRICE

def calculate_money_return(total_price,money_given):
    if total_price <= money_given :
        return money_given - total_price
    else:
        return -1

def print_return_info(money_return):
    kinds = [500, 200, 100, 20, 20, 10, 1]
    for kind in kinds:
        count_kind = int(money_return / kind)
        money_return -= kind*count_kind
        if count_kind != 0:
            print(f"{kind}k VND : {count_kind}")
        if money_return < 1:
            print(f"Amount left over : {int(money_return*1000)} VND")

def menu_fruits():
    print(f"-"*18)
    print("|Id: 1  | Apple  |")
    print("|Id: 2  | Banana |")
    print("|Id: 3  | Kiwi   |")
    print("|Id: 4  | Mango  |")
    print("|Id: 0  | Exit   |")
    print(f"-"*18)

def get_choice_id(choice):
    if choice == 1:
        return "Apple"
    elif choice == 2:
        return "Banana"
    elif choice == 3:
        return "Kiwi"
    elif choice == 4:
        return "Mango"
    
def main():
    APPLE_PRICE = 23    # 23k VND/1kg
    BANANA_PRICE = 15   # 15k VND/1kg
    KIWI_PRICE = 30     # 30k VND/1kg
    MANGO_PRICE = 20    # 20k VND/1kg
    total_price = 0.0

    while True:
        ids = [1,2,3,4]
        menu_fruits()
        try:
            choice_id = int(input("Enter id fruit : "))
            if choice_id == 0:
                print(f"Total fruits price: {total_price}")                
                money_given = float(input("Total money customer give you : ")) # k VND
                money_return = calculate_money_return(total_price,money_given)
                
                if money_return == -1:
                    print("Not enough cash")
                else:
                    print(f"You need to return to customer: {money_return}")
                    print_return_info(money_return)
                return 0

            elif choice_id not in ids:
                print("Not a valid choice")
                
            else:
                for id in ids : 
                    if choice_id == id:
                        choice = get_choice_id(choice_id)
                        weight = enter_price_fruit(choice)
                        if id == 1:
                            price = calculate_total_price(weight,APPLE_PRICE)
                            price = round(price,2)
                            total_price += price
                            print(f"Total apple price : {price}")
                        elif id == 2:
                            price = calculate_total_price(weight,BANANA_PRICE)
                            price = round(price,2)
                            total_price += price
                            print(f"Total banana price : {price}")
                        elif id == 3:
                            price = calculate_total_price(weight,KIWI_PRICE)
                            price = round(price,2)
                            total_price += price
                            print(f"Total kiwi price : {price}")
                        elif id == 4:
                            price = calculate_total_price(weight,MANGO_PRICE)
                            price = round(price,2)
                            total_price += price
                            print(f"Total mango price : {price}")
                    
        except:
            print("ValueError !! ")
            
if __name__ == "__main__":
    main()