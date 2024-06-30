# Define the Allowed Vehicles List
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to display the menu and handle user input
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

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

# Main program loop
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_authorized_vehicle()
        elif choice == '3':
            print("Exiting CarFinder. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
