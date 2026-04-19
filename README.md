# 🚗 Driver Location Visualization with Streamlit & MongoDB

A data visualization and database optimization project that demonstrates how to build a **real-time driver location dashboard** using **Streamlit**, **MongoDB**, and **PyMongo**.
The project also explores **MongoDB indexing techniques** such as compound indexes and covered queries to improve query performance.

---

## 📌 Overview

This project was developed as part of the **Unstructured Database (UDB) Lab**.

The application performs the following tasks:

* Stores driver information in a **MongoDB collection**
* Retrieves driver data using **PyMongo queries**
* Displays driver locations on a **Streamlit interactive map**
* Demonstrates **index optimization techniques** in MongoDB
* Analyzes query execution using **MongoDB explain plans**

---

## 🛠 Technologies Used

* **Python**
* **Streamlit**
* **MongoDB**
* **PyMongo**
* **Pandas**
* **Docker (Multi-Stage Containerization)**

---

## 📂 Project Structure

```
driver_streamlit_app
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Multi-stage Docker configuration
└── README.md           # Project documentation
```

---

## 🚀 Features

* 📍 Interactive **map visualization of driver locations**
* 🗄 MongoDB database integration
* ⚡ **Compound and single-field indexes**
* 🔎 Query optimization using **explain()**
* 📈 Performance improvement using **covered indexes**
* 🐳 Docker container support

---

## 🧪 Experiment Tasks

### 1️⃣ Driver Location Visualization

A Streamlit dashboard visualizes driver coordinates stored in MongoDB.

Example code:

```python
st.title("Driver Locations")
st.map(df)
```

Each marker on the map represents a driver with latitude and longitude coordinates.

---

### 2️⃣ MongoDB Indexing

Indexes were created to improve database query performance.

#### Compound Index

```python
collection.create_index([("status",1),("vehicle_type",1)])
```

#### Single Field Index

```python
collection.create_index("driver_id")
```

These indexes reduce collection scanning and speed up queries.

---

### 3️⃣ Query Optimization

A PyMongo query retrieves **available bike drivers with rating greater than 4**.

```python
query = {
 "status":"available",
 "vehicle_type":"bike",
 "rating":{"$gt":4.0}
}
```

The results are sorted using:

```python
collection.find(query).sort("last_updated",-1)
```

---

### 4️⃣ Query Execution Analysis

MongoDB's **explain()** method is used to analyze query performance.

Key execution stages:

* **IXSCAN** → Index scan used
* **FETCH** → Retrieves matching documents

This confirms that MongoDB used indexes instead of scanning the entire collection.

---

### 5️⃣ Covered Index

A **covered index** was implemented to allow MongoDB to return results directly from the index.

```python
collection.create_index([
("status",1),
("vehicle_type",1),
("last_updated",-1),
("rating",1)
])
```

Explain output shows:

```
PROJECTION_COVERED
totalDocsExamined = 0
```

This means MongoDB answered the query **without scanning any documents**.

---

## 📊 Output

The Streamlit dashboard displays driver locations on an interactive map.

Each marker represents a driver retrieved from the MongoDB database.

---

## 🎯 Learning Outcomes

This project demonstrates:

* Integration of **MongoDB with Python applications**
* Building **interactive dashboards with Streamlit**
* Using **database indexing techniques**
* Understanding **query execution plans**
* Improving performance using **covered queries**

---

## 🧑‍💻 Author

Developed as part of a **University Database Systems Lab Project**.

---

⭐ If you found this project helpful, feel free to give it a star!
