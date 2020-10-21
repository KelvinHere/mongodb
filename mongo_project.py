import os
import pymongo
if os.path.exists("env.py"):
    import env

# Create constants for URI login data / database / collection in database
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "FirstCluster"
COLLECTION = "myFirstMDB"

# Connect to mongo
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except:
        print("Could not connect to MongoDB: %s") %e

def show_menu():
    print("")
    print("1. Add Record")
    print("2. Find Record by Name")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Exit")

    option = input("Enter an option - ")
    return option

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")

# Run connect to mongo function
conn = mongo_connect(MONGO_URI)
# Add collection to a variable
coll = conn[DATABASE][COLLECTION]

main_loop()