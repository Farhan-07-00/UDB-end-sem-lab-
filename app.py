import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["transport"]
collection = db["driver_locations"]

# --------------------------
# Q2(a) Create Indexes
# --------------------------
collection.create_index([("status",1),("vehicle_type",1)])
collection.create_index("driver_id")

# --------------------------
# Insert sample data if empty
# --------------------------
if collection.count_documents({}) == 0:
    collection.insert_many([
        {
            "driver_id":"D1",
            "status":"available",
            "vehicle_type":"bike",
            "lat":22.57,
            "lon":88.36,
            "rating":4.5,
            "last_updated":"2026-04-13"
        },
        {
            "driver_id":"D2",
            "status":"on_trip",
            "vehicle_type":"car",
            "lat":22.58,
            "lon":88.37,
            "rating":4.2,
            "last_updated":"2026-04-13"
        },
        {
            "driver_id":"D3",
            "status":"available",
            "vehicle_type":"bike",
            "lat":22.59,
            "lon":88.38,
            "rating":4.8,
            "last_updated":"2026-04-13"
        }
    ])

# Q2(b) Query
query = {
    "status": "available",
    "vehicle_type": "bike",
    "rating": {"$gt": 4.0}
}

drivers = list(collection.find(query).sort("last_updated",-1))

print("Available bike drivers:")
for d in drivers:
    print(d)

# Explain query plan
print("\nExplain Plan:")
explain_result = collection.find(query).sort("last_updated",-1).explain()
print(explain_result)
# Q2(c) Covered Index
collection.create_index([
    ("status",1),
    ("vehicle_type",1),
    ("last_updated",-1),
    ("rating",1)
])

projection = {
    "_id":0,
    "status":1,
    "vehicle_type":1,
    "last_updated":1,
    "rating":1
}

covered_query = list(collection.find({"status":"available"},projection))

print("\nCovered Query Result:")
for r in covered_query:
    print(r)

print("\nCovered Query Explain:")
print(collection.find({"status":"available"},projection).explain())
# --------------------------
# Map visualization (Q1)
# --------------------------
data = list(collection.find({},{"_id":0}))

df = pd.DataFrame(data)

# Rename columns for Streamlit map
df = df.rename(columns={"lat":"latitude","lon":"longitude"})

st.title("Driver Locations")

st.map(df)