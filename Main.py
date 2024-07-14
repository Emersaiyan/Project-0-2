## Define the Allowed Vehicles List
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T']

# Function to display the menu and handle user input
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD a Vehicle to Allowed List (Sales Manager)")
    print("4. REMOVE a Vehicle from Allowed List (Sales Manager)")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

# Function to print all allowed vehicles
def print_allowed_vehicles():
    print("\nList of Authorized Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to search for an authorized vehicle
def search_authorized_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an Authorized Vehicle.")
    else:
        print(f"{vehicle_name} is not found in the list of Authorized Vehicles.")

# Function to add a vehicle to the Allowed Vehicles List
def add_vehicle():
    if input("\nAre you sure you want to add a vehicle? Type 'yes' to proceed: ").lower() == 'yes':
        new_vehicle = input("Enter the name of the new vehicle to add: ")
        AllowedVehiclesList.append(new_vehicle)
        print(f"{new_vehicle} has been added to the Allowed Vehicles List.")
    else:
        print("Cancelled adding a new vehicle.")

# Function to remove a vehicle from the Allowed Vehicles List
def remove_vehicle():
    vehicle_name = input("\nEnter the full Vehicle name to remove: ")
    if vehicle_name in AllowedVehiclesList:
        confirm = input(f"Are you sure you want to remove {vehicle_name}? Type 'yes' to proceed: ").lower()
        if confirm == 'yes':
            AllowedVehiclesList.remove(vehicle_name)
            print(f"{vehicle_name} has been removed from the Allowed Vehicles List.")
        else:
            print(f"Cancelled removing {vehicle_name}.")
    else:
        print(f"{vehicle_name} is not found in the list of Authorized Vehicles.")

# Main program loop
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_authorized_vehicle()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            remove_vehicle()
        elif choice == '5':
            print("Exiting CarFinder. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
