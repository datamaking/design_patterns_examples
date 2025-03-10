class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize the database connection
            cls._instance.host = "localhost"
            cls._instance.port = 5432
            cls._instance.database = "myapp"
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            # Simulate database connection
            print(f"Connecting to database at {self.host}:{self.port}/{self.database}")
            self.connected = True
        else:
            print("Already connected to database")
    
    def disconnect(self):
        if self.connected:
            print("Disconnecting from database")
            self.connected = False
        else:
            print("Already disconnected")

# Usage example
def main():
    # Both db1 and db2 will reference the same instance
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"Are db1 and db2 the same instance? {db1 is db2}")
    
    db1.connect()
    db2.connect()  # Will show "Already connected"
    
    db1.disconnect()
    db2.disconnect()  # Will show "Already disconnected"

if __name__ == "__main__":
    main() 