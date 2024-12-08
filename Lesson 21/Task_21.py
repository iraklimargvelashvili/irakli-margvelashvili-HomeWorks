import json

try:
    with open("data.json", "r") as file :
        department_info = json.load(file)
except FileNotFoundError :
    print("This file isn't exsist!")
    
class Department:
    def __init__(self, name: str, description: str, employees: list = None):
        self.name = name
        self.description = description
        self.employees = employees if employees is not None else []

    def __repr__(self):
        return f"Department(name='{self.name}', description='{self.description}', employees={self.employees})"
    
    def add_employ(self,empl) :
        self.employees.append(empl)
    
    def average(self) :
        salary_sum = 0
        for emp in self.employees:
            try:
                salary_sum += int(emp.salary)
            except ValueError :
                print("The data type is invalid")
        try:
            return salary_sum/len(self.employees)
        except ZeroDivisionError :
                print("Can not divide by 0")
    
    def maximum(self) :
        try:
            return max(int(emp.salary) for emp in self.employees)
        except :
            print("unable to perform the requested operation")
    
    def minimum(self) :
        try:
            return min(int(emp.salary) for emp in self.employees)
        except :
            print("unable to perform the requested operation")
    
    def positions(self) :
        result_dict = {}
        for emp in self.employees :
            if result_dict.get(emp.position) :
                result_dict[emp.position] += 1
            else :
                result_dict[emp.position] = 1
        return result_dict        
    
class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', position='{self.position}', salary={self.salary})"

def main() :
    departments = []
    for dept_key, dept_info in department_info.items():
        employees = [
            Employee(emp["name"], emp["position"], int(emp["salary"]))
            for emp in dept_info.get("employees", [])
        ]
        department = Department(dept_info["name"], dept_info["description"], employees)
        departments.append(department)


    employ_1 = Employee('Ciu Ri','Architect','100')
    employ_2 = Employee('Lama Ra','Architect','200')

    departments[2].add_employ(employ_1)
    departments[2].add_employ(employ_2)

    print(departments[0].average())
    print(departments[1].maximum())
    print(departments[2].minimum())
    print(departments[0].positions())
    print(departments[1].positions())
    print(departments[2].positions())
    print(departments[0].description)
    print(departments[1].name)
    print(departments[2].employees)


if __name__ == "__main__" :
    main()