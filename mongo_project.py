### Menu Driven Databse CRUD ###

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

# Returns a record
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter first last > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("")
        print("Error accessing Database")

    if not doc:
        print("")
        print("Error : No results found")
    
    return doc

# Option 1 - Add record to database
def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter first last > ")
    dob = input("Enter date of birth (DD/MM/YYYY) > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender.lower(), 
                'hair_colour': hair_colour.lower(), 'occupation': occupation.lower(),
                'nationality': nationality.lower()}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Record Inserted")
    except:
        print("")
        print("Error accessing database")

# Option 2 - Find Record
def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id": #ID is the mongo DB id number
                print(k.capitalize() + ": " + v.capitalize())

# Option 3 - Edit record
def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > " )

                if update_doc[k] == "":
                    update_doc[k] = v # keep original value

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document Updated")
        except:
            print("")
            print("Error accessing Database")

def delete_record():
    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")
        
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("")
                print("Document deleted!")
            except:
                print("")
                print("Error accessing Database")
        else:
            print("Document not deleted")

# Menu loop
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")


conn = mongo_connect(MONGO_URI) # Run connect to mongo function
coll = conn[DATABASE][COLLECTION] # Add collection to a variable

main_loop()