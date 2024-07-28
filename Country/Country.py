# Kyle Stewart CIS261 Country

def display_menu():
    print("Menu:")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")

def display_countries(country_dict):
    print("\nCountry Keys:")
    for key in country_dict:
        print(key)
    country_key = input("Enter a country key: ")
    if country_key in country_dict:
        print(f"The country for key '{country_key}' is {country_dict[country_key]}")
    else:
        print("Invalid key. Please try again.")

def add_country(country_dict):
    country_key = input("Enter the key for the country: ")
    if country_key in country_dict:
        print("This key already exists. Please try again.")
    else:
        country_name = input("Enter the name of the country: ")
        country_dict[country_key] = country_name
        print(f"Country '{country_name}' has been added with key '{country_key}'.")

def delete_country(country_dict):
    country_key = input("Enter the key of the country you want to delete: ")
    if country_key in country_dict:
        print(f"Country '{country_dict[country_key]}' has been deleted.")
        del country_dict[country_key]
    else:
        print("Invalid key. Please try again.")

def main():
    country_dict = {"US": "United States", "UK": "United Kingdom", "JP": "Japan"}  # Prepopulate the dictionary with 3 countries

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_countries(country_dict)
        elif choice == "2":
            add_country(country_dict)
        elif choice == "3":
            delete_country(country_dict)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")

        print()

if __name__ == "__main__":
    main()
