try:
    with open("data/input.txt", "r") as file:
        data = file.read().strip().splitlines()
except FileNotFoundError:
    print("Input file not found.")
print('Data loaded successfully.')