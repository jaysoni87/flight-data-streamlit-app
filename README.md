# Flight Data Streamlit Web Application

## 📌 Project Overview
This project is a **Streamlit-based web application** built using **flight data stored in MySQL**.  
The data is fetched **directly from MySQL into PyCharm**, processed, and displayed through an interactive web interface.

The application provides:

- Flight search functionality (source → destination)
- Interactive analysis charts
- Complete project information
- Data transparency for users to explore or modify the dataset

---

## 🚀 Features

### **1️⃣ About Page**
- Provides a complete explanation of the project  
- Lists all steps performed:  
  - MySQL data extraction  
  - Data cleaning & preprocessing  
  - Streamlit UI development  
- Includes a downloadable copy of the dataset for users  
- Helps users understand and modify the project based on their needs  

---

### **2️⃣ Check Flights Page**
This page allows users to:

- Select **Source** 🛫  
- Select **Destination** 🛬  
- Click **Search** to view all available flights  

The results display:

- Flight name / airline  
- Source and destination cities  
- Flight timing  
- Additional flight details from the database  

This feature replicates a simple flight search system.

---

### **3️⃣ Analysis Page**
This page contains multiple visual analytics generated from the flight dataset:

#### **📊 Pie Chart – Flight Company Comparison**
Visualizes the share of different airlines such as:  
- Indigo  
- Jet Airways  
- SpiceJet  
- Air India  
- GoAir  
- Others  

---

#### **🏙️ Most Frequent Cities (Source & Destination)**
- Bar/column charts showing the most commonly used **source airports**  
- Similar chart for **destination airports**  
- Helps understand the busiest flight routes  

---

#### **📅 Date-wise Flight Distribution**
A line or bar chart showing:  
- Number of flights per date  
- Trends in travel volume  
- Peak travel days  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** MySQL  
- **IDE:** PyCharm  
- **Visualization:** matplotlib / seaborn / plotly (as used inside Streamlit)  

---
