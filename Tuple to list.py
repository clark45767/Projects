# Store personal details in a tuple
personal_details = (
    "Clark",    # First Name
    "Garma",    # Last Name
    "Ibsen" ,   # Middle Name
    "Moscoso",  # Middle Initial
    16,         # Age
    170,        # Height (in cm)
    63,         # Weight (in kg)
    "Coding"    # Favourite Subject
)
# Print each detail clearly
print("Last Name:", personal_details[0])
print("First Name:", personal_details[1])
print("Middle Name:", personal_details[2])
print("Middle Initial:", personal_details[3])
print("Age:", personal_details[4])
print("Height:", personal_details[5], "cm")
print("Weight:", personal_details[6], "kg")
print("Favourite Subject:", personal_details[7])

# Convert tuple to list
personal_list = list(personal_details)

print("\nConverted List:", personal_list)
