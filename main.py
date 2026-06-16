from database import (
    create_database,
    add_duty,
    view_duties,
    update_duty,
    delete_duty,
    search_officer
)

create_database()

print("===== Police Duty Management System =====")

print("1. Add Duty")
print("2. View Duties")
print("3. Update Duty")
print("4. Delete Duty")
print("5. Search Officer")

choice = input("Enter Choice: ")

if choice == "1":

    name = input("Enter Officer Name: ")
    location = input("Enter Duty Location: ")
    date = input("Enter Duty Date (DD-MM-YYYY): ")

    add_duty(name, location, date)

    print("Duty added successfully!")

elif choice == "2":

    duties = view_duties()

    print("\n===== Duty Records =====")

    for duty in duties:
        print(duty)

elif choice == "3":

    duty_id = int(input("Enter Duty ID: "))
    name = input("New Officer Name: ")
    location = input("New Duty Location: ")
    date = input("New Duty Date: ")

    update_duty(duty_id, name, location, date)

    print("Duty updated successfully!")

elif choice == "4":

    duty_id = int(input("Enter Duty ID to delete: "))

    delete_duty(duty_id)

    print("Duty deleted successfully!")

elif choice == "5":

    name = input("Enter Officer Name: ")

    results = search_officer(name)

    print("\n===== Search Results =====")

    for officer in results:
        print(officer)

else:

    print("Invalid Choice")