import json

recipes_dict = {
    "Classic Margherita Pizza" : ["flour","tomato","mozzarella","basil","oil","salt","pepper"],
    "Vegetarian Stir-Fry" : ["tofu","broccoli","carrots","pepper","soy","ginger","garlic","oil","rice"],
    "Chocolate Chip Cookies" : ["flour","butter","sugar","eggs","vanilla","soda","salt","chocolate"],
    "Chicken Alfredo Pasta" : ["pasta","chicken","cream","parmesan","garlic","butter","salt","pepper","parsley"],
    "Mango Salsa Chicken" : ["chicken","mango","onion","cilantro","lime","jalapeño","salt","pepper","rice"],
    "Quinoa Salad with Avocado" : ["quinoa","avocado","tomato","cucumber","pepper","cheese","lemon","salt","pepper"],
    "Tomato Basil Bruschetta" : ["baguette","tomato","basil","garlic","glaze","oil","salt","pepper"],
    "Beef and Broccoli Stir-Fry" : ["beef","broccoli","soy","oyster","oil","garlic","ginger","cornstarch","rice"]
}

shops_dict = {
    "Deili" : ["flour","carrots","pepper","soy","ginger","garlic","oil","rice"],
    "Nikora" : ["tomato","mozzarella","pepper","rice"],
    "2X2" : ["basil","lime","jalapeño","salt",],
    "Spar" : ["oil","salt","pepper","tofu","broccoli","chicken","mango","onion","cilantro"]
}

with open("recipes.json", "w") as file:
    json.dump(recipes_dict, file, indent=4)
    
with open("shops.json", "w") as file:
    json.dump(shops_dict, file, indent=4)
    
