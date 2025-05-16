
import csv
from datetime import datetime

CSV_FILE = "truck_logs.csv"

# Initialize the CSV file with headers (if not already present)
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Truck ID", "Latitude", "Longitude", "Temperature", "Humidity", "Fuel", "Alerts"])
    except FileExistsError:
        pass  # File already exists

# Log a single truck record to the CSV
def log_truck_data(truck_id, lat, lon, temperature, humidity, fuel, alerts):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            truck_id, lat, lon, temperature, humidity, fuel,
            "; ".join(alerts) if alerts else "None"
        ])
