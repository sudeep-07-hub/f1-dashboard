# 🏎️ F1 Race Dashboard — Monza 2023

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://f1-dashboard-44.streamlit.app/)

A live, interactive web application for analyzing Formula 1 race data. This dashboard specifically explores race pace, tyre strategy, and team performance for the **2023 Italy Grand Prix (Monza)**.

**Live Demo:** [https://f1-dashboard-44.streamlit.app/](https://f1-dashboard-44.streamlit.app/)

---

## ✨ Features

- **Race Overview Metrics:** High-level statistics on clean laps, active drivers, and compounds used during the race.
- **Interactive Filters:** Customize your view by filtering data based on specific drivers and tyre compounds.
- **Tyre Degradation Analysis:** A line chart visualizing average lap times as tyre life increases.
- **Team Average Pace:** A horizontal bar chart comparing the average pace of each constructor.
- **Lap Time Distribution:** A violin plot showcasing the spread and consistency of lap times across different tyre compounds.
- **Race Progression:** A scatter plot of all lap times throughout the race, color-coded by compound to reveal race strategies and stints.

## 🛠️ Technology Stack

- **[Streamlit](https://streamlit.io/):** For building the interactive web application UI.
- **[FastF1](https://docs.fastf1.dev/):** For fetching telemetry and lap data directly from Formula 1.
- **[Plotly Express](https://plotly.com/python/plotly-express/):** For creating rich, interactive, and responsive visualizations.
- **[Pandas & NumPy](https://pandas.pydata.org/):** For data manipulation and analysis.

## 🚀 How to Run Locally

If you want to run this dashboard on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sudeep-07-hub/f1-dashboard.git
   cd f1-dashboard
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The `packages.txt` file is used to specify system-level dependencies for Streamlit Cloud deployment.)*

3. **Run the Streamlit app:**
   ```bash
   streamlit run app/app.py
   ```

4. **View the app:**
   Open your browser and navigate to `http://localhost:8501`.

## 📂 Project Structure

- `app/app.py`: The main Streamlit application script containing all the logic and UI components.
- `requirements.txt`: Python package dependencies.
- `packages.txt`: System-level dependencies for Streamlit Cloud deployment.

---
*Created for F1 enthusiasts to dive deeper into race data!*
