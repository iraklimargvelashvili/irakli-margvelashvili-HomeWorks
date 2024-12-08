import json

try:
    with open("data.json", "r") as file :
        department_info = json.load(file)
except FileNotFoundError :
    print("This file isn't exsist!")
    
def average_salary(info_dict) :
    
    average_dict = {}
    for department in info_dict.keys() :
        salary_sum = 0
        for attribute in info_dict[department]["employees"] :
            try:
                salary_sum += int(attribute["salary"])
            except ValueError :
                print("The data type is invalid")
        try:
            average_dict[department] = salary_sum/len(info_dict[department]["employees"])
        except ZeroDivisionError :
            print("Can not divide by 0")
    
    #print(average_dict)
    return average_dict

def main() :
    result_dict = average_salary(department_info)
    print(result_dict)
    try:
        with open("avg_salary.json", "w") as file:
            json.dump(result_dict, file, indent=4)
    except:
        print("An error occurred while working with the file")
        
if __name__ == "__main__" :
    main()
