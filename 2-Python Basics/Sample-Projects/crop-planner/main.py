# --- Your Code Goes Here ---
data = {
  "crops": [
    {
      "name": "Carrot",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "June", "July"],
      "harvest_season": ["June", "July", "August", "September", "October"],
      "soil_type": "Light, sandy, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Moderate",
      "container_friendly": True
    },
    {
      "name": "Potato",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May"],
      "harvest_season": ["June", "July", "August", "September"],
      "soil_type": "Loamy, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Moderate",
      "container_friendly": True
    },
    {
      "name": "Tomato",
      "type": "Fruit",
      "planting_season": ["March", "April", "May"],
      "harvest_season": ["July", "August", "September"],
      "soil_type": "Rich, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Lettuce",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "June", "July", "August"],
      "harvest_season": ["May", "June", "July", "August", "September"],
      "soil_type": "Moist, well-drained",
      "sunlight": "Partial shade",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Strawberry",
      "type": "Fruit",
      "planting_season": ["March", "April", "August", "September"],
      "harvest_season": ["June", "July"],
      "soil_type": "Well-drained, slightly acidic",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Onion",
      "type": "Vegetable",
      "planting_season": ["March", "April", "September", "October"],
      "harvest_season": ["July", "August", "September"],
      "soil_type": "Well-drained, fertile",
      "sunlight": "Full sun",
      "watering_needs": "Moderate",
      "container_friendly": True
    },
    {
      "name": "Broccoli",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "July", "August"],
      "harvest_season": ["June", "July", "August", "September", "October"],
      "soil_type": "Fertile, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": False
    },
    {
      "name": "Peas",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "June"],
      "harvest_season": ["June", "July", "August"],
      "soil_type": "Well-drained, fertile",
      "sunlight": "Full sun",
      "watering_needs": "Moderate",
      "container_friendly": True
    },
    {
      "name": "Pumpkin",
      "type": "Vegetable",
      "planting_season": ["May", "June"],
      "harvest_season": ["September", "October"],
      "soil_type": "Rich, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": False
    },
    {
      "name": "Garlic",
      "type": "Vegetable",
      "planting_season": ["October", "November", "December"],
      "harvest_season": ["June", "July"],
      "soil_type": "Well-drained, fertile",
      "sunlight": "Full sun",
      "watering_needs": "Moderate",
      "container_friendly": True
    },
    {
      "name": "Radish",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "June", "July", "August"],
      "harvest_season": ["May", "June", "July", "August", "September"],
      "soil_type": "Light, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Cabbage",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "July", "August"],
      "harvest_season": ["June", "July", "August", "September", "October"],
      "soil_type": "Fertile, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": False
    },
    {
      "name": "Spinach",
      "type": "Vegetable",
      "planting_season": ["March", "April", "May", "August", "September"],
      "harvest_season": ["May", "June", "July", "September", "October"],
      "soil_type": "Moist, fertile",
      "sunlight": "Partial shade",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Beans (Runner Beans)",
      "type": "Vegetable",
      "planting_season": ["May", "June"],
      "harvest_season": ["July", "August", "September"],
      "soil_type": "Well-drained, fertile",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": True
    },
    {
      "name": "Courgette",
      "type": "Vegetable",
      "planting_season": ["May", "June"],
      "harvest_season": ["July", "August", "September"],
      "soil_type": "Rich, well-drained",
      "sunlight": "Full sun",
      "watering_needs": "Regular",
      "container_friendly": False
    }
  ]
}


# Challenge 1
def crops_to_plant_this_month():
    """ 
    function that asks the user for the current month and displays 
    all the crops that can be planted in that month.
    """
    print(" --- What to plant this month ---")
    # Ask the user to input a month
    month = input("Enter a month of the year: (e.g August) ").title()
    # Find crops that can planted in that month
    # Get list of crops
    crops = data["crops"]
    
    print(f"In {month}, you can plant the following crops:")
    # Loop over each crop
    for crop in crops:
        # Check if crop planting is equal to given month
        if month in crop["planting_season"]:
            # print plantable crops
            print(f"> {crop['name']}")


# Challenge 2
def crops_to_harvest_this_month():
    """ 
    asks the user for the current month and displays 
    all the crops that can be harvested in that month.
    """
    print(" --- What to harvest this month ---")
    # Ask the user to input a month
    month = input("Enter a month of the year: (e.g August) ").title()
    
    # Get list of crops
    crops = data["crops"]
    print(f"In {month}, you can harvest the following crops:")
    
    # Loop over each crop
    for crop in crops:
        # Check if crop harvest is equal to given month
        if month in crop["harvest_season"]:
            # print harvestable crops
            print(f"> {crop['name']}")


# --- Main Code Starts Here ---
print("##############################")
print("#         Allotment          #")
print("#     Crop Planner v1.01     #")
print("##############################")
print("")
print(" >>> Menu Options:")
print("  > Option 1: Find out what you can plant on a specific month of the year")
print("  > Option 2: Find out what you can harvest on a specific month of the year")
print("  > Option 3: Find out a list of crops that you can grow in a pot (container friendly crops)")
print("  > Option 4: Find out what crops to plant in your garden based on soil type and sunlight conditions")
print("  > Option 5: Find out all the information to grow a specific crop")

option = input("Enter your option (1 to 5):")

while option not in (["1", "2", "3", "4", "5"]):
    print(" > Invalid option, try again...")
    option = input(" > Enter your option (1 to 5):")

if option == "1":
    crops_to_plant_this_month()
elif option == "2":
    crops_to_harvest_this_month()
elif option == "3":
    print("This option is not available yet!")
elif option == "4":
    print("This option is not available yet!")
elif option == "5":
    print("This option is not available yet!")
