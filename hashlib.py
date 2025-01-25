import hashlib

try:
    file_path = r"C:\Users\Victus\Desktop\python\example,txt"
    with open(file_path, "rb") as file:
        print("SHA-256 hash:", hashlib.sha256(file.read()).hexdigest())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Error: {e}")
