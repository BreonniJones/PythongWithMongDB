from pymongo import MongoClient

def get_database():
    try:
        # MongoDB connection details (username and password)
        from pymongo import MongoClient

        client = MongoClient("mongodb://Breonni:password@localhost:27017/testDB")
        db = client["testDB"]

        return db
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None
