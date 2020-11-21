# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
   return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, amount_sold):
    shop["admin"]["pets_sold"] += amount_sold

def get_stock_count(stock):
   return len(stock["pets"])

def get_pets_by_breed(shop, breed):
    pets = []
    for the_pet in shop['pets']:
        if the_pet['breed'] == breed :
            pets.append(the_pet)
    return pets

def find_pet_by_name(shop, name):
    for pet_name in shop['pets']:
        if pet_name['name'] == name:
            return pet_name

def remove_pet_by_name(shop, name):
    for pet_name in shop['pets']:
        if pet_name['name'] == name:
            shop['pets'].remove(pet_name)

def add_pet_to_stock(shop, new_pet):
    shop['pets'].append(new_pet)
            
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customers):
    count = 0

    for customer in customers['pets']:
        count = len(customers['pets'])
    
    return count

def add_pet_to_customer(customer, new_pet):
    
    customer['pets'].append(new_pet)
   




