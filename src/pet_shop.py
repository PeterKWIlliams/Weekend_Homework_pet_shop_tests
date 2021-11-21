# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(data):
    
    return data["name"]
    
def get_total_cash(data):
    
    return data["admin"]["total_cash"]

def add_or_remove_cash(data,cash):
    
    data["admin"]["total_cash"] += cash 
    
def get_pets_sold(data):
    
    return data["admin"]["pets_sold"]

def increase_pets_sold(data, pets_sold_new):
    
    data["admin"]["pets_sold"] = pets_sold_new

def get_stock_count(data):
   
     return len(data["pets"])

def get_pets_by_breed(data,breed):
    
    pets_breed_count =[]
    
    for pets in data["pets"]:
        if pets["breed"] == breed: 
          pets_breed_count.append(pets["breed"])
    
    return pets_breed_count

def find_pet_by_name(data,pet_name):
    for pets in data["pets"]:
      if pet_name == pets["name"]:
        return pets
             
    
def remove_pet_by_name(data,pet_name):
    for index_num in range(len(data["pets"])):
      if data["pets"][index_num]["name"] == pet_name: 
        (data["pets"]).pop(index_num)
        break
        

def add_pet_to_stock(data,new_pet):

    return data["pets"].append(new_pet)

def get_customer_cash(data):
    return data["cash"]

def remove_customer_cash(data,amount):
    data["cash"] -= amount 

def get_customer_pet_count(data):
    return len(data["pets"])

def add_pet_to_customer(data,new_pet):

    data["pets"].append(new_pet)

def customer_can_afford_pet(data,new_pet):
    if data["cash"] >= new_pet["price"]:
        return True
    return False    

def sell_pet_to_customer(data,pet,customer):
    if pet is None:
      return  
    elif customer["cash"] <= pet["price"]:
        return
    else: 
        data["admin"]["total_cash"] += pet["price"]
        data["admin"]["pets_sold"]  += 1 
        data["pets"].remove(pet)
        customer["pets"].append(pet) 
        customer["cash"] -= pet["price"]
    

        
          
           
        
        
    
    

        
# for index_num in range(len(data["pets"])):
#         if data["pets"][index_num]["name"] == pet_name: 
#           del data["pets"][index_num]
#           break
