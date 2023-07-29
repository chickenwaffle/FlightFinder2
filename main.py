import requests
from bs4 import BeautifulSoup
import re

def get_flight_cost(site_url):
    try:
        response = requests.get(site_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # You need to inspect the website's HTML to find the appropriate tags and classes
        # for extracting the flight cost information.
        # Replace 'YOUR_FLIGHT_COST_PARSER' with the correct parsing logic.
        flight_cost = "PUT LOGIC HERE"
        
        return flight_cost
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {site_url}: {e}")
        return None

def compare_flight_costs(travel_sites):
    for site_name, site_url in travel_sites.items():
        print(f"Fetching data from {site_name}...")
        flight_cost = get_flight_cost(site_url)
        if flight_cost is not None:
            print(f"Flight cost on {site_name}: {flight_cost}")
            print("=" * 40)

def main():
    travel_sites = {
        "Travel Site 1": "https://www.google.com/travel/flights/",
        "Travel Site 2": "https://www.expedia.com",
        "Travel Site 3": "https://www.kayak.com",
        # Add more travel sites and their URLs as needed.
    }
    
    print("Flight Cost Comparison Tool")
    while True:
        print("\nOptions:")
        print("1. Compare flight costs")
        print("2. Add a new travel site")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            compare_flight_costs(travel_sites)
        elif choice == "2":
            site_name = input("Enter the name of the new travel site: ")
            site_url = input("Enter the URL of the new travel site: ")
            travel_sites[site_name] = site_url
            print(f"{site_name} has been added to the comparison list.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()