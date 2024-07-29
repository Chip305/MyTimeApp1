import streamlit as st
import pandas as pd
import pytz
from datetime import datetime
import numpy as np

# Function to fetch the current time for a given city
def get_time_for_city(city):
    timezone = pytz.timezone(city)
    city_time = datetime.now(timezone)
    return city_time.strftime('%Y-%m-%d %H:%M:%S')

# List of cities and their timezones
cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Paris": "Europe/Paris",
    "Los Angeles": "America/Los_Angeles",
    "Chicago": "America/Chicago",
    "Moscow": "Europe/Moscow",
    "Beijing": "Asia/Shanghai",
    "Mumbai": "Asia/Kolkata",
    "Dubai": "Asia/Dubai",
    "Rome": "Europe/Rome",
    "Bangkok": "Asia/Bangkok",
    "Istanbul": "Europe/Istanbul"
}

# Streamlit app
st.title("International Clock")

st.sidebar.header("Select Cities")
selected_cities = st.sidebar.multiselect("Choose cities to display time", list(cities.keys()), default=list(cities.keys())[:5])

if selected_cities:
    st.subheader("Current Time in Selected Cities")
    times = {city: get_time_for_city(cities[city]) for city in selected_cities}
    
    time_df = pd.DataFrame(times.items(), columns=['City', 'Current Time'])
    
    # Customize the dataframe display
    st.dataframe(time_df.style.hide(axis="index").set_properties(**{'text-align': 'center'}))
    
    # Add a refresh button to manually refresh the data
    if st.button("Refresh"):
        st.experimental_rerun()

    # Add an area chart
    st.subheader("Time in Selected Cities (Random Data for Visualization)")
    chart_data = pd.DataFrame(
        np.random.randn(20, len(selected_cities)),
        columns=selected_cities
    )
    st.area_chart(chart_data)

    # Add a map with points marked on it
    st.subheader("Map of Selected Cities")
    city_coords = {
        "New York": [40.712776, -74.005974],
        "London": [51.507351, -0.127758],
        "Tokyo": [35.689487, 139.691711],
        "Sydney": [-33.868820, 151.209290],
        "Paris": [48.856613, 2.352222],
        "Los Angeles": [34.052235, -118.243683],
        "Chicago": [41.878113, -87.629799],
        "Moscow": [55.755825, 37.617298],
        "Beijing": [39.904202, 116.407394],
        "Mumbai": [19.076090, 72.877426],
        "Dubai": [25.276987, 55.296249],
        "Rome": [41.902782, 12.496366],
        "Bangkok": [13.756331, 100.501762],
        "Istanbul": [41.008240, 28.978359]
    }
    map_data = pd.DataFrame(
        [city_coords[city] for city in selected_cities],
        columns=['lat', 'lon']
    )
    st.map(map_data)

    # Add more interactive widgets
    st.sidebar.subheader("Additional Settings")

    # Checkbox widget
    show_city_names = st.sidebar.checkbox("Show city names on the map")

    # Slider widget
    num_points = st.sidebar.slider("Number of points to display", 1, 100, 10)

    # Select-slider widget
    selected_timezone = st.sidebar.select_slider(
        "Select timezone to highlight",
        options=list(cities.values())
    )

    # Date input widget
    selected_date = st.sidebar.date_input("Select a date")

    # Time input widget
    selected_time = st.sidebar.time_input("Select a time")

    if show_city_names:
        st.subheader("Selected City Names")
        st.write(selected_cities)

    st.subheader("User Inputs")
    st.write("Number of points to display:", num_points)
    st.write("Selected timezone:", selected_timezone)
    st.write("Selected date:", selected_date)
    st.write("Selected time:", selected_time)

    # Information box
    st.info("This information box will update and provide additional details to the signed-in users in real-time as they move around locations.")

    # Warning box
    st.warning("This is a warning box that'll alert user's of potential issues in their zones.")


