import os
import json

grocery_list = []#creating a empty list to c

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def to_create():
    with open("grocery_data.json",'w')as file:
        json.dump(grocery_list,file,indent = 4)
    
def to_read():
    global grocery_list
    if os.path.exists("grocery_data.json"):
        with open("grocery_data.json",'r')as file:
            grocery_list = json.load(file)
    
def add_product():
    clear()
    prd_id = int(input("1.Enter the product id:- "))           
    name = str(input("2.Enter the name of the product:- "))           
    uom = str(input("3.Enter the 'Unit of measurement' :- "))           
    price = float(input("4.Enter the price of the product(per UOM):- "))            
    currency = str(input("5.Specifies the currency:- "))           
    quantity = int(input("6.Enter the quantity:- "))           
    weight = float(input("7.Enter the minimum weight:- "))            
    N_price = float(input("8.Enter the normalized price:- "))            
    N_measure = str(input("9.Enter the minimum Unit of measurement:- "))           
    variety = str(input("10.Enter the specific variety:- "))           
    origin = str(input("11.Enter the country of origin:- "))           
    S_tt_quantity = int(input("12.Enter the total number of units available:- "))           
    S_weight = float(input("13.Enter the total weight:- "))
    brand_name = str(input("14.Enter the brand name:- "))
    categories = str(input("15.Enter the specific categories:- "))

    grocery_dict = {
            'id':prd_id,
            'name':name,
            'uom':uom,
            'price':price,
            'currency':currency,
            'quantity':quantity,
            'weight':weight,
            
            'normaliz':{
            'Normalized Price':N_price,
            'Normalized Measurement':N_measure,
            },
            
            'variety':variety,
            'origin':origin,
            
            'stock':{
            'Total Quantity':S_tt_quantity,
            'Total Weight':S_weight,
            },
            
            'brand_name':brand_name,
            'categories':[categories]
            
        }
        
    grocery_list.append(grocery_dict)
    
    to_create()
    
    print(grocery_dict)


def display_stock():
    clear()
    print("\n\t===SOCK DETAILS===")
    
    prd_name = str(input("\nEnter the name of product to search:- "))
    
    flag =False
    
    for G in grocery_list:
        if G['name'].lower() == prd_name.lower():
            
            flag =True
            
            print(f"\n.Product ID: {G['id']},\n.Product Name: {G['name']}, \n.Unit of Measurement: {G['uom']}, \n.Product Price: {G['price']}")
            print(f".Currency: {G['currency']} \n.Produt Quantity: {G['quantity']}, \n.Product Minimum Weight: {G['weight']}")
            
            for key_1, value_1 in G['normaliz'].items():
                print(f"{key_1} : {value_1}")
                
            print(f".Variety: {G['variety']} \n.Origin: {G['origin']} ")
            
            for key_2, value_2 in G['stock'].items():
                print(f"{key_2} {value_2}")
                
            print(f".Brand Name: {G['brand_name']} \n.Categorie: {G['categories']}")
        
    if not flag:
        clear()
        print(f"\n Product | {prd_name} | not in the STOCK")
    
    to_read()    

def all_list():
    clear()
    print("\n\t---Displaying List---")
    print(f"\n{grocery_list}")
    

def category_list():
    clear()
    for list in grocery_list:
        for data in list['categories']:
            print(data)

def main():
    clear()
    to_read()
    while True:
        print("\n\t-----| GROCERY STORE |-----\n \n1.Add Product \n2.Search Specific Stock \n3.Category \n4.Display all list \n0.EXIT ")

        try:
            user_input = int(input("\nEnter the choice (0/1/2/3/4)::- "))
            
            if user_input == 1:
                clear()
                add_product()
                
            elif user_input == 2:
                clear()
                display_stock()
                
            elif user_input == 3:
                clear()
                category_list()
                
            elif user_input == 4:
                clear()
                all_list()

            elif user_input == 0:
                clear()
                user_input_2 = str(input("Would you like to Exit ? |(Y/N)|:- "))
                try:
                    clear()
                    if user_input_2.lower() == 'y':
                        print("\n\tExiting from the program |HAND|")
                        break
                    elif user_input_2.lower() == 'n':
                        print("\n\t| Welcome Back USER |")
                        continue
                    else:
                        print(f"\n\t--- {user_input_2} INVALID ---")
                    
                except AttributeError:
                    print("Invalid input! Please enter a valid string.")
            else:
                print(f"\n | {user_input} |Invalid input! Please enter a valid integer.")

        except ValueError:
            print("\nInvalid input! Please enter a valid integer.")
            continue 
                
         
            
if __name__ == "__main__":
    main()
    
    
    