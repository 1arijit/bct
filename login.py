from tabulate import tabulate

# Initialize an empty list to store user data
users = []

def sign_up():
    """Handles user sign-up and stores the user in the list."""
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if email already exists
    for user in users:
        if user["email"] == email:
            print("Email already registered. Try logging in.")
            return

    user_data = {"name": name, "email": email, "password": password}
    users.append(user_data)
    print("User registered successfully!")

def login():
    """Handles user login by checking credentials."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful!")
            return
    print("Login failed! Incorrect email or password.")

def display_users():
    """Displays the user list in a tabular format."""
    if not users:
        print("No users found.")
        return

    table = [[i + 1, user["name"], user["email"]] for i, user in enumerate(users)]
    print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))

def delete_user():
    """Deletes a user based on the provided email."""
    email = input("Enter email to delete: ")

    for user in users:
        if user["email"] == email:
            users.remove(user)
            print("User deleted successfully!")
            return

    print("User not found!")

# Menu-driven program
while True:
    print("\n1. Sign Up\n2. Login\n3. Display Users\n4. Delete User\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        display_users()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
