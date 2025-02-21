# The Allotment Crop Planner

In this challenge, we will work with a dataset containing detailed information about crops that can be grown in an allotment. The dataset includes, soil types, watering needs, and more.

Your task is to write a Python program that helps an allotment gardener by answering specific questions about what they can grow and when.

Below you will find:

1. [The Dataset](#the-dataset) - to be used in completion for this project.
2. [The Challenges](#the-challenges) - steps to complete the project.

> **You will find some starter code in file [main.py](main.py)**

## Learning Objectives

By completing this challenge you will improve your python skills and learn to:

- Work with nested data.
- Use loops on lists and dictionaries data structures to filter crops based on user input.
- Convert user input (month, soil type, etc.) to a standard format to avoid case-sensitivity issues.

## The Dataset

```python
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
```

## The Challenges

### ***Challenge 1: Crops to Plant This Month***

The aim of this first challenge is to write a Python function that asks the user for the current month and displays all the crops that can be planted in that month.

**Example Input/Output:**

```shell
Enter the current month: April
Crops you can plant in April:
- Carrot
- Tomato
```

### ***Challenge 2: Crops to Harvest This Month***

Reusing similar code to the code provided to solve challenge 1, write another function Python function that asks the user for the current month and displays all the crops that can be harvested in that month.

**Example Input/Output:**

```shell
Enter the current month: September
Crops you can harvest in September:
- Carrot
- Tomato
```

### ***Challenge 3: Container-Friendly Crops***

Some gardeners have limited space and need to grow crops in pots. Write a function that lists all crops that can be grown in containers.

**Example Output:**

```shell
Container-friendly crops:
- Carrot
- Tomato
```

### ***Challenge 4: Best Crops for Your Garden***

Modify your program to ask the user about their soil type and sunlight conditions and then recommend crops that match their garden environment.

**Example Input/Output:**

```shell
Enter your soil type: Sandy
Enter your sunlight condition (Full sun/Partial shade): Full sun

Crops suitable for your garden:
- Carrot
```

### ***Challenge 5: Interactive Crop Assistant***

Enhance your program by allowing users to search for a specific crop and view detailed growing advice, including watering needs and best companion plants.

**Example Input/Output:**

```shell
Enter a crop name: Tomato

Tomato (Fruit)
- Planting season: March - April - May
- Harvest season: July - August - September
- Soil type: Rich, well-drained
- Sunlight: Full sun
- Watering needs: Moderate
- Container-friendly: Yes
```

### Bonus challenges

1. Make the program run until the user decides to exit
2. Optimise challenge 5 to simplify the solution
3. Add recommendations for crops that can be planted alongside the chosen crop in challenge 5