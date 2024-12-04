import json

context_list = []
analitic_dict = {}

with open("data.txt", "r") as file:
    for line in file:
        context_list.append(line.split(","))
        
def max_amount_user(info):
    _max = max(int(elem[2]) for elem in info)
    users = [elem[0] for elem in info if int(elem[2]) == _max]
    return users

def max_total_purchase(info):
    _max = max(int(elem[2])*int(elem[3]) for elem in info)
    users = [elem[0] for elem in info if int(elem[2])*int(elem[3]) == _max]
    return users

def price_everage(info):
    _sum = sum(int(elem[3]) for elem in info)
    return round(_sum/len(info),2)

def amount_everage(info):
    _sum = sum(int(elem[2]) for elem in info)
    return round(_sum/len(info),2)

def max_amount_prodact(info):
    _max = max(int(elem[2]) for elem in info)
    users = [elem[1] for elem in info if int(elem[2]) == _max]
    return users

def main():
    analitic_dict["max_amount_user"] = max_amount_user(context_list)
    analitic_dict["max_total_purchase"] = max_total_purchase(context_list)
    analitic_dict["price_everage"] = price_everage(context_list)
    analitic_dict["amount_everage"] = amount_everage(context_list)
    analitic_dict["max_amount_prodact"] = max_amount_prodact(context_list)

    with open("json_for_Test_18_2.json", "w") as file:
        json.dump(analitic_dict, file, indent=4)

if __name__ == "__main__":
    main()