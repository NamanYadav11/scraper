from src.scraper import scrape
from src.store import input_data
from src.crud import insert_property, delete_property, update_property, read_properties
from src.csv_gerator import file_genrate


def main():
    data=scrape()

    print(data)
    input_data(data)

    file_genrate()

    while True:
        print("\nCRUD Menu:")
        print("1. Insert Property")
        print("2. Update Property")
        print("3. Delete Property")
        print("4. Read Properties")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            property = {
                'name': input("Enter name: "),
                'mileage': input("Enter mileage: "),
                'price': input("Enter price: "),
            }
            insert_property(property)
            
        elif choice == '2':
            property = {
                'sr':input("Enter serial number:"),
                'name': input("Enter new name: "),
                'mileage': input("Enter new mileage: "),
                'price': input("Enter new price: "),
            }
            update_property(property)
            
        elif choice == '3':
            sr = input("Enter the ID of the property to delete: ")
            delete_property(sr)
            
        elif choice == '4':
            read_properties()
            
        elif choice == '5':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice, please try again.")

    

    
   

if __name__ == "__main__":
    main()