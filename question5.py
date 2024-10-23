# Ask the user age
age = int(input("Enter your age: "))
# Determine the category based on age
if age < 18:
    category = "Minor"
elif 18 <= age <= 65:
    category = "Adult"
else:
    category = "Senior"
# Print the category
print(f"You are a {category}.")
