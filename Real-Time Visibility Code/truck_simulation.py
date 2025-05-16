
import time
import random
import matplotlib.pyplot as plt

# Number of trucks and simulation duration
NUM_TRUCKS = 3
SIMULATION_STEPS = 10

# Alert thresholds
ALERT_THRESHOLD = {
    'fuel': 35,         # Fuel alert if below 35%
    'temperature': 28,  # Temperature alert if above 28°C
    'humidity': 65      # Humidity alert if above 65%
}

# Initial mock GPS data for each truck
truck_data = [
    {'id': 1, 'lat': 12.9716, 'lon': 77.5946},
    {'id': 2, 'lat': 13.0827, 'lon': 80.2707},
    {'id': 3, 'lat': 17.3850, 'lon': 78.4867}
]

# Historical sensor data storage
history = {
    1: {'temperature': [], 'humidity': [], 'fuel': []},
    2: {'temperature': [], 'humidity': [], 'fuel': []},
    3: {'temperature': [], 'humidity': [], 'fuel': []}
}

# Generate random sensor readings
def generate_sensor_data():
    temperature = round(random.uniform(18, 35), 2)
    humidity = round(random.uniform(40, 75), 2)
    fuel = round(random.uniform(25, 100), 2)
    return temperature, humidity, fuel

# Simulate small GPS movement
def simulate_movement(lat, lon):
    lat += round(random.uniform(-0.01, 0.01), 5)
    lon += round(random.uniform(-0.01, 0.01), 5)
    return lat, lon

# Check and collect alerts based on thresholds
def check_alerts(temp, humidity, fuel):
    alerts = []
    if fuel < ALERT_THRESHOLD['fuel']:
        alerts.append("Low Fuel")
    if temp > ALERT_THRESHOLD['temperature']:
        alerts.append("High Temp")
    if humidity > ALERT_THRESHOLD['humidity']:
        alerts.append("High Humidity")
    return alerts

# Main simulation logic
def simulate():
    print("=== Starting Truck Simulation ===")
    for step in range(SIMULATION_STEPS):
        print(f"\n--- Step {step + 1} ---")
        for truck in truck_data:
            truck_id = truck['id']

            # Simulate movement and sensor reading
            truck['lat'], truck['lon'] = simulate_movement(truck['lat'], truck['lon'])
            temp, hum, fuel = generate_sensor_data()
            alerts = check_alerts(temp, hum, fuel)

            # Print current status
            print(f"Truck-{truck_id} | Location: ({truck['lat']}, {truck['lon']})")
            print(f"Temp: {temp}°C | Humidity: {hum}% | Fuel: {fuel}% | Alerts: {', '.join(alerts) if alerts else 'None'}")

            # Save history for plotting
            history[truck_id]['temperature'].append(temp)
            history[truck_id]['humidity'].append(hum)
            history[truck_id]['fuel'].append(fuel)

            time.sleep(0.5)  # Simulated delay

# Plot data graphs
def plot_data():
    x = list(range(1, SIMULATION_STEPS + 1))
    colors = ['red', 'green', 'blue']

    # Plot temperature
    plt.figure(figsize=(12, 4))
    for i in range(1, NUM_TRUCKS + 1):
        plt.plot(x, history[i]['temperature'], marker='o', label=f"Truck {i}", color=colors[i-1])
    plt.title("Temperature per Truck")
    plt.xlabel("Simulation Step")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot humidity
    plt.figure(figsize=(12, 4))
    for i in range(1, NUM_TRUCKS + 1):
        plt.plot(x, history[i]['humidity'], marker='o', label=f"Truck {i}", color=colors[i-1])
    plt.title("Humidity per Truck")
    plt.xlabel("Simulation Step")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot fuel levels
    plt.figure(figsize=(12, 4))
    for i in range(1, NUM_TRUCKS + 1):
        plt.plot(x, history[i]['fuel'], marker='o', label=f"Truck {i}", color=colors[i-1])
    plt.title("Fuel Level per Truck")
    plt.xlabel("Simulation Step")
    plt.ylabel("Fuel (%)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Entry point
if __name__ == "__main__":
    simulate()
    plot_data()
