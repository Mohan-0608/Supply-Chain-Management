# Supply-Chain-Management
# 🚚 Real-Time Truck Monitoring System

A real-time truck monitoring system with simulation, CSV logging, a desktop GUI, and a web dashboard.

---

## 📦 Project Structure

Real-Time Visibility/

├── truck_simulation.py           # CLI-based simulation
├── truck_logger.py               # CSV logger module
├── truck_gui.py                  # Desktop GUI with Tkinter
├── truck_dashboard.py            # Web dashboard with Streamlit
├── truck_logs.csv                # Auto-generated CSV file
└── README.md                     # Project documentation



---

## 🚀 Features

- Real-time truck simulation with status updates
- CSV logging of location, speed, and status
- Desktop GUI for offline/local monitoring
- Web dashboard for online visualization using Streamlit
- Modular and extensible Python architecture

---

   ## 🛠️ Installation

   ###1. Clone the Repository

    ```bash
                   git clone https://github.com/yourusername/real_time_truck_monitoring.git
                    cd real_time_truck_monitoring

   ###2.✅ How to Run:

   Save this code as
     
                 truck_simulation.py

     
   Make sure you have matplotlib installed:
                  
                  pip install matplotlib

     
   Run the script:
         
                  python truck_simulation.py

### 📈 Usage
   ### 🧪 Run Truck Simulation (CLI)
             
                  python truck_simulation.py
             
   This simulates real-time truck data and writes it to truck_logs.csv.
      
   ### 💾 CSV Logging
              
                  truck_logger.py 
   is automatically used to log data to CSV format. No manual steps needed unless customizing.
     
   ### 🖥️ Launch Desktop GUI
            
                  python truck_gui.py
   View live truck status in a local desktop window.
   
   ### 🌐 Launch Web Dashboard

                 streamlit run truck_dashboard.py
   Open the browser (usually http://localhost:8501) to interact with the dashboard


          
