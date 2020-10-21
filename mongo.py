import os
import pymongo
# Grab the file that has the mongo URI data
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
        print("Mongo is connected")
        return conn
    except:
        print("Could not connect to MongoDB: %s") %e

# Run connect to mongo function
conn = mongo_connect(MONGO_URI)
# Add collection to a variable
coll = conn[DATABASE][COLLECTION]

# Create and insert a new doc to collection
#new_doc = {"first": "duglas", "last": "adams", "dob": "11/03/1952", "hair_colour": "grey", "occupation": "writer", "nationality": "british"}
#coll.insert(new_doc)

# Create and insert multiple new docs to collection
#new_docs = [{"first": "terry",
#             "last": "pratchett", 
#             "dob": "28/04/1948", 
#             "gender": "m",
#             "hair_colour": "not much", 
#             "occupation": "writer", 
#             "nationality": "british"},
#
#             {"first": "george",
#             "last": "rr martin", 
#             "dob": "20/09/1948", 
#             "gender": "m",
#             "hair_colour": "white", 
#             "occupation": "writer", 
#             "nationality": "american"}]
#coll.insert_many(new_docs)

# Show all documents in collection
#documents = coll.find()

# Find documents in collection
#documents = coll.find({"first": "duglas"})

# Remove document
#coll.remove({"first": "duglas"})

# Update single document
#coll.update_one({"nationality": "american"}, {"$set": {"hair_colour": "maroon"}})

# Update many documents
#coll.update_many({"nationality": "american"}, {"$set": {"hair_colour": "blue"}})

#documents = coll.find({"nationality": "american"})
for doc in documents:
    print(doc)
    