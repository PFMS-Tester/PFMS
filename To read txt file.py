file_path = "ghj.txt"

try:
    with open(file_path, "r") as file:
        data = file.read()
    print("Data from the file:")
    print(data)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")