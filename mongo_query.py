
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["transport"]
collection = db["driver_locations"]


collection.insert_many([
{
"driver_id": "rupam1",
"status": "available",
"vehicle_type": "bike",
"last_updated": "2026-04-13",
"rating": 4.5
},
{
"driver_id": "satyajit2",
"status": "on_trip",
"vehicle_type": "car",
"last_updated": "2026-04-13",
"rating": 4.2
},
{
"driver_id": "surya3",
"status": "available",
"vehicle_type": "bike",
"last_updated": "2026-04-13",
"rating": 4.8
}
])

# Step 4: Create compound index
collection.create_index([
("status",1),
("vehicle_type",1)
])

# Step 5: Create single field index
collection.create_index("driver_id")

# Step 6: Query available bike drivers with rating > 4
query = {
"status":"available",
"vehicle_type":"bike",
"rating":{"$gt":4.0}
}

drivers = collection.find(query).sort("last_updated",-1)

print("Available bike drivers:")
for d in drivers:
    print(d)

# Step 7: Explain query execution
print("\nExplain Plan:")
print(collection.find(query).sort("last_updated",-1).explain())

# Step 8: Create covered index
collection.create_index([
("status",1),
("vehicle_type",1),
("last_updated",-1),
("rating",1)
])

# Step 9: Projection query for dashboard
query2 = {"status":"available"}

projection = {
"_id":0,
"status":1,
"vehicle_type":1,
"last_updated":1,
"rating":1
}

result = collection.find(query2,projection)

print("\nCovered Query Result:")
for r in result:
    print(r)

# Step 10: Verify covered query
print("\nCovered Query Explain:")
print(collection.find(query2,projection).explain())