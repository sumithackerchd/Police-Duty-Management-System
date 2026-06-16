from database import create_database, add_duty, view_duties

create_database()

print("===== Police Duty Management System =====")

print("1. Add Duty")
print("2. View Duties")

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

else:
    print("Invalid Choice")