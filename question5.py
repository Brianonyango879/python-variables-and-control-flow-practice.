def age_checker():
    age = int(input("Enter your age: "))
# Determine the category based on age
    if age < 0:
        return "Age Invalid!"
    elif age < 18:
        return "You are a Minor"
    elif age <= 65:
        return "You are an Adult"
    else:
        return "You are a Senior"
# Print the category
print(age_checker())
