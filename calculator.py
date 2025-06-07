import requests

bodyweight = float(input("Enter your bodyweight in lbs: "))

while True:
    activity_level = input("Enter your activity level (1-5): ")
    if activity_level in ['1', '2', '3', '4', '5']:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

activity_multiplier = {
    '1': 0.36,  # Sedentary
    '2': 0.45,  # Lightly active
    '3': 0.59,  # Moderately active
    '4': 0.82,  # Very active
    '5': 1.0   # Extremely active
}
protein_recommendation = bodyweight * activity_multiplier[activity_level]
print(f"Your recommended protein value is {protein_recommendation} grams.")

baseurl = "https://fruityvice.com/"

def get_fruits(name):
    url = f"{baseurl}api/fruit/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        fruits = response.json()
        return fruits
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

eaten_fruits_today = []
protein_intake = 0

while True:
        fruit_name = input("Enter the name of the fruit(s) eaten today (q to quit): ").strip().lower()
        if fruit_name == 'q':
            break
        try:
            get_fruits(fruit_name)  # Just to test if it exists
            eaten_fruits_today.append(fruit_name)
        except Exception:
            print("Fruit not found. Please try again.")

for fruit in eaten_fruits_today:
    fruit_info = get_fruits(fruit)
    protein_intake += fruit_info['nutritions']['protein']

print(f"Total protein from fruits: {protein_intake:.2f} grams.")
percentage_of_recommendation = (protein_intake / protein_recommendation) * 100
if percentage_of_recommendation > 100:
    print("You have exceeded your recommended protein intake today through fruits.")
else:
    print(f"You have consumed {percentage_of_recommendation:.2f}% of your recommended protein intake today through fruits.")
