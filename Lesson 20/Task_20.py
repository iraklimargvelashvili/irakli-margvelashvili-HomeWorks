import json

with open("recipes.json", "r") as file:
    recipes_dict = json.load(file)
    
with open("shops.json", "r") as file:
    shops_dict = json.load(file)
    
user_ingr = None
prefer_shop = []
check_step = 0
length_for_check = len(shops_dict.keys())


def find_shops(ingr_set):
    min_diff_dict = {}
    
    for shop,shop_ingr_set in shops_dict.items() :
        if ingr_set.issubset(shop_ingr_set) :
            prefer_shop.append(shop)
            return prefer_shop
        min_diff_dict[shop] = ingr_set.difference(shop_ingr_set)
        
    min = ingr_set
    
    most_relev_shop = None
    
    for shop,shop_ingr_set in min_diff_dict.items() : 
        if len(list(shop_ingr_set)) < len(list(min)) :
            min = shop_ingr_set   
            most_relev_shop = shop
    if most_relev_shop :
        prefer_shop.append(most_relev_shop)
                    
    if most_relev_shop :
        return find_shops(min_diff_dict[most_relev_shop])
    else :
        return "Sorry, you cannot prepare this dish in our city."
    
    check_step += 1
    
    if check_step == length_for_check :
        return "Sorry, you cannot prepare this dish in our city."

def main() :
    user_choice = input("Please choose the dish you want from the dishes listed below: Classic Margherita Pizza; Vegetarian Stir-Fry; Chocolate Chip Cookies; Chicken Alfredo Pasta; Mango Salsa Chicken; Quinoa Salad with Avocado; Tomato Basil Bruschetta; Beef and Broccoli Stir-Fry: ")
    
    user_ingr = recipes_dict.get(user_choice)
    print(find_shops(set(user_ingr)))
    

if __name__ == "__main__" :
    main()