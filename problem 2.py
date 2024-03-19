import os
def add_employee(code, name, salary, allowance):
    with open("input.txt", "a") as file:
        file.write(f"{code},{name},{salary},{allowance}\n")
def read_data():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            code, name, salary, allowance = line.strip().split(",")
            data.append((code, name, float(salary), float(allowance)))
    return data
def binary_search(data, target_name):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid][1] == target_name:
            return data[mid]
        elif data[mid][1] < target_name:
            low = mid + 1
        else:
            high = mid - 1
    return None


def remove_employee(code):
    data = read_data()
    with open("input.txt", "w") as file:
        for entry in data:
            if entry[0] != code:
                file.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]}\n")


def sort_and_save():
    data = read_data()
    sorted_data = sorted(data, key=lambda x: x[2] + x[3], reverse=True)
    with open("result.txt", "w") as file:
        for entry in sorted_data:
            file.write(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]}\n")


def main():
    while True:
        print("=====Menu=====")
        print("\n1. Add Employee")
        print("2. Find Employee by Name")
        print("3. Remove Employee")
        print("4. Print List in Descending Order of Salary + Allowance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = input("Enter employee salary: ")
            allowance = input("Enter employee allowance: ")
            add_employee(code, name, salary, allowance)
            print("Employee added successfully.")
        
        elif choice == "2":
            target_name = input("Enter employee name to search: ")
            data = read_data()
            result = binary_search(data, target_name)
            if result:
                print("Employee found:")
                print(f"Code: {result[0]}")
                print(f"Name: {result[1]}")
                print(f"Salary: {result[2]}")
                print(f"Allowance: {result[3]}")
            else:
                print("Employee not found.")
        
        elif choice == "3":
            code = input("Enter employee code to remove: ")
            remove_employee(code)
            print("Employee removed successfully.")
        
        elif choice == "4":
            sort_and_save()
            print("List printed in descending order of Salary + Allowance and saved to result.txt.")
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

