import streamlit as st
from dbhelper import DB
import plotly.graph_objs as go
import plotly.express as px
import pandas  as pd

db = DB()

st.sidebar.title('Flights Analysis')
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
    col1, col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    st.title('Analytics')
# 1
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )
    st.header('Pie chart')
    st.plotly_chart(fig)
# 2
    city ,frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# 3
    date ,frequency2 = db.daily_frequency()
    fig = px.line(
        x=date,
        y=frequency2
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    import streamlit as st

    st.title("✈️ About This Project")

    st.markdown("""
    This project is a **Flight Data Explorer and Visualizer** built using **Python**, **Streamlit**, **MySQL**, and **Plotly**.  
    It is designed to help users interactively explore flight data and gain useful insights through filtering and visualization.

    The dataset includes key details about various flights such as:
    - **Airline**
    - **Date of Journey**
    - **Source and Destination**
    - **Route**
    - **Departure Time**
    - **Flight Duration**
    - **Number of Stops**
    - **Price**

    ---

    ### 📄 Project Structure

    **1. About This Project**  
    An introduction to the app, its purpose, and the technologies used.

    **2. Check Flights**  
    This interactive page allows users to:
    - Select **Source** and **Destination** cities using sliders.
    - Click a **Search** button to filter flights.
    - View filtered results displaying the **Airline**, **Route**, **Departure Time**, **Duration**, and **Price** of the available flights.

    **3. Flight Analysis**  
    This section provides visual insights using interactive charts created with Plotly. Currently, it includes:
    - A few analytical graphs showing patterns and trends in the data.
    - More visualizations will be added soon to help users better understand flight behaviors such as pricing trends, duration comparisons, and stop frequency.
    """)

    st.subheader('📂 Dataset Used in This Project')

    file_path = ".venv/flights_data.csv"
    df = pd.read_csv(file_path)

    st.dataframe(df)

    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Download Dataset",
            data=f,
            file_name="flight_data.csv",
            mime="text/csv"
        )
