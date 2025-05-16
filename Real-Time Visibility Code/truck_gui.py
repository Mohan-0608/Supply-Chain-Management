import tkinter as tk
from tkinter import ttk
import csv
import threading
import time

LOG_FILE = 'truck_logs.csv'
UPDATE_INTERVAL = 2000  # milliseconds (2 seconds)

class TruckMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Real-Time Truck Monitoring")
        self.geometry("400x300")
        
        self.trucks = []
        self.latest_data = {}

        self.create_widgets()
        self.load_trucks()
        self.update_data_periodically()

    def create_widgets(self):
        # Truck list label and listbox
        tk.Label(self, text="Trucks:").pack(pady=5)
        self.truck_listbox = tk.Listbox(self, height=8)
        self.truck_listbox.pack(fill=tk.X, padx=10)
        self.truck_listbox.bind("<<ListboxSelect>>", self.on_truck_select)

        # Frame for showing details
        self.details_frame = ttk.Frame(self)
        self.details_frame.pack(pady=20, fill=tk.X, padx=10)

        ttk.Label(self.details_frame, text="Latitude:").grid(row=0, column=0, sticky=tk.W)
        self.lat_var = tk.StringVar(value="N/A")
        ttk.Label(self.details_frame, textvariable=self.lat_var).grid(row=0, column=1, sticky=tk.W)

        ttk.Label(self.details_frame, text="Longitude:").grid(row=1, column=0, sticky=tk.W)
        self.lon_var = tk.StringVar(value="N/A")
        ttk.Label(self.details_frame, textvariable=self.lon_var).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(self.details_frame, text="Speed (km/h):").grid(row=2, column=0, sticky=tk.W)
        self.speed_var = tk.StringVar(value="N/A")
        ttk.Label(self.details_frame, textvariable=self.speed_var).grid(row=2, column=1, sticky=tk.W)

    def load_trucks(self):
        # Scan the CSV to find unique truck IDs
        try:
            with open(LOG_FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # Use correct column name from the first cell's header
                truck_ids = set()
                for row in reader:
                    truck_ids.add(row['Truck ID']) # Changed 'truck_id' to 'Truck ID'
            self.trucks = sorted(truck_ids)
            self.truck_listbox.delete(0, tk.END)
            for truck in self.trucks:
                self.truck_listbox.insert(tk.END, truck)
        except FileNotFoundError:
            self.trucks = []
            self.truck_listbox.insert(tk.END, "No log file found.")

    def read_latest_data(self):
        latest = {}
        try:
            with open(LOG_FILE, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # This assumes the last entry in the file is the latest for each truck.
                # If the file isn't strictly ordered by timestamp, this logic needs refinement.
                for row in reader:
                    # Use correct column names from the first cell's header
                    truck_id = row['Truck ID'] # Changed 'truck_id' to 'Truck ID'
                    latest[truck_id] = {
                        'latitude': row['Latitude'], # Changed 'latitude' to 'Latitude'
                        'longitude': row['Longitude'], # Changed 'longitude' to 'Longitude'
                        # The original log file doesn't have 'speed_kmph'. 
                        # This needs to be added to the simulation or removed from the GUI.
                        # For now, set to N/A or remove the speed label/variable.
                        # Assuming speed is not in the logs based on the first cell.
                        # If speed is added to the logs, update the header in initialize_csv.
                        'speed_kmph': 'N/A' # Setting to N/A as it's not in the log file schema
                    }
        except FileNotFoundError:
            latest = {}
        self.latest_data = latest

    def on_truck_select(self, event):
        selection = event.widget.curselection()
        if selection:
            truck_id = event.widget.get(selection[0])
            data = self.latest_data.get(truck_id, None)
            if data:
                self.lat_var.set(data['latitude'])
                self.lon_var.set(data['longitude'])
                self.speed_var.set(data.get('speed_kmph', 'N/A')) # Use .get() with default for robustness
            else:
                self.lat_var.set("N/A")
                self.lon_var.set("N/A")
                self.speed_var.set("N/A")

    def update_data_periodically(self):
        self.read_latest_data()
        # Update display for selected truck (if any)
        selection = self.truck_listbox.curselection()
        if selection:
            truck_id = self.truck_listbox.get(selection[0])
            data = self.latest_data.get(truck_id, None)
            if data:
                self.lat_var.set(data['latitude'])
                self.lon_var.set(data['longitude'])
                self.speed_var.set(data.get('speed_kmph', 'N/A')) # Use .get() with default
            else:
                self.lat_var.set("N/A")
                self.lon_var.set("N/A")
                self.speed_var.set("N/A")
        # Schedule the next update
        self.after(UPDATE_INTERVAL, self.update_data_periodically)


if __name__ == "__main__":
    # The following lines attempt to start a Tkinter GUI, which requires a display.
    # Running this directly in a headless notebook environment will cause a TclError.
    # Commenting them out allows the cell to define the class without crashing.
    # To run the GUI, execute this script in an environment with a display,
    # or set up a virtual display (like Xvfb) and the DISPLAY environment variable.
    # app = TruckMonitorApp()
    # app.mainloop()
    pass # Add a pass statement or other code if needed when not running the GUI