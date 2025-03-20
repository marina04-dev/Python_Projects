import json


def add_person():
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    return person



def delete_contact(people):
    display_people(people)
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid Number! Out Of Range!")
            else:
                break
        except:
            print("Invalid Number!")
    people.pop(number-1)
    print("Person Deleted Successfully!")



def search(people):
    search_name = input("Enter a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)


def display_people(people):
    for i, person in enumerate(people):
        print(i+1, '-', person["name"], '|', person["age"], '|', person["email"])


with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    print("\t\tWelcome To The Contact Management System!")
    print("Menu:")
    print("1. Add")
    print("2. Delete")
    print("3. Search")
    print("4. Contact List Display")
    print("5. Contact List Size")
    print("0. Quit")

    command = input("Enter your choice: ").strip()

    if command.isdigit():
        if command == "1":
            person = add_person()
            people.append(person)
            print("Person Added Successfully!")
        elif command == "2":
            delete_contact(people)
        elif command == "3":
            search(people)
        elif command == "4":
            display_people(people)
        elif command == "5":
            print("Contact List Size: ", len(people))
        elif command == "0":
            print("Exit Of The Program!")
            break
    else:
        print("Invalid Input!")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
