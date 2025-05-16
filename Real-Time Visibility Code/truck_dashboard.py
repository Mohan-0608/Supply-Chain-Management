!pip install streamlit pandas pydeck
import streamlit as st
import pandas as pd
import pydeck as pdk
import time

LOG_FILE = "truck_logs.csv"

st.set_page_config(page_title="Truck Monitoring Dashboard", layout="centered")

st.title("Real-Time Truck Monitoring Dashboard")

@st.cache_data(ttl=10)
def load_data():
    # Change 'timestamp' to 'Timestamp' to match the CSV header
    df = pd.read_csv(LOG_FILE, parse_dates=['Timestamp'])
    return df

# Auto-refresh every 10 seconds
refresh_rate = 10

df = load_data()

# Also update column name references for truck_id, latitude, longitude, and speed_kmph
# to match the CSV headers if necessary.
# Based on the CSV header "Truck ID", update 'truck_id' references.
truck_ids = df['Truck ID'].unique()
selected_truck = st.sidebar.selectbox("Select Truck ID", options=sorted(truck_ids))

# Filter data for the selected truck
# Update column names here too
truck_data = df[df['Truck ID'] == selected_truck].sort_values('Timestamp')

if truck_data.empty:
    st.warning("No data available for the selected truck.")
else:
    latest = truck_data.iloc[-1]
    st.subheader(f"Latest Data for {selected_truck}")
    # Update column names here too
    st.write(f"**Timestamp:** {latest['Timestamp']}")
    st.write(f"**Latitude:** {latest['Latitude']}")
    st.write(f"**Longitude:** {latest['Longitude']}")
    # Note: 'Speed (km/h)' is not in the original CSV header from ipython-input-4.
    # Assuming it's intended to be added or removed.
    # If speed is not logged, this line will cause a KeyError.
    # For now, comment it out or handle the missing column.
    # st.write(f"**Speed (km/h):** {latest['Speed (km/h)']}") # Assuming 'Speed (km/h)' is the header name if added


    # Map with latest position
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            # Update column names here too
            latitude=latest['Latitude'],
            longitude=latest['Longitude'],
            zoom=12,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=pd.DataFrame([latest]),
                # Update column names here too
                get_position='[Longitude, Latitude]',
                get_color='[255, 0, 0]',
                get_radius=100,
                pickable=True,
            )
        ],
    ))

    # Optional: show recent path (last 10 points)
    if len(truck_data) > 1:
        path_data = truck_data.tail(10)
        # Update column names here too
        path_coords = list(zip(path_data['Longitude'], path_data['Latitude']))
        st.subheader("Recent Path")
        # Update column names here too
        st.line_chart(path_data[['Latitude', 'Longitude']])

# Auto-refresh page every refresh_rate seconds (works in Streamlit Cloud or local with Streamlit >=1.19)
# st.experimental_rerun() # Comment out or remove the deprecated function
st.rerun() # Use the current function for rerunning the app [2]

# Or if you want a countdown timer before refresh, you could use:
# for i in range(refresh_rate, 0, -1):
#     st.sidebar.write(f"Refreshing in {i} seconds...")
#     time.sleep(1)
# st.experimental_rerun() # This line would also need to be changed to st.rerun() if uncommented.