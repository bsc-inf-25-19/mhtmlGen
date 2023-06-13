#Take input from the user
word = input("Enter the best plant's name: ")

# Conditional checks and appropriate responses

if word == "Spathiphyllum":
    print("Spathiphyllum is the best plant ever!")
elif word == "SPATHIPHYLLUM":
    print("Yes - Spathiphyllum is the best plant ever!")
elif word == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {word}!")
