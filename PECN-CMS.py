import RegisterComplain
import ComplainUpdate
import PendingComplain
import SpecificComplain


def main():
    while True:
        print("Welcome to Priya Electronics & Cable Network \nComplaint Management System (PECN-CMS)")
        print("1. Register a new complaint")
        print("2. Update remarks for a complaint")
        print("3. View complaints with NULL remarks updation time")
        print("4. View details of a specific complaint")
        print("5. Exit")
        choice = input("Enter your choice: ")

        print('\n', "------------------------------------------------------------", '\n')

        if choice == "1":
            RegisterComplain.register_complaint()
        elif choice == "2":
            ComplainUpdate.update_remarks()
        elif choice == "3":
            PendingComplain.view_null_remarks_updation()
        elif choice == "4":
            SpecificComplain.view_complaint_details()
        elif choice == "5":
            print("Exiting the PriyaCable-CMS.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



