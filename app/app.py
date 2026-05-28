import fastf1
import streamlit as st
import fastf1
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='F1 Race Dashboard',
    page_icon='🏎️',
    layout='wide'
)

st.title('🏎️ F1 Race Dashboard — Monza 2023')
st.markdown('### Exploring race pace, tyre strategy and team performance')

@st.cache_data
def load_data():
    fastf1.Cache.enable_cache('/Users/sukesh/Desktop/f1-dashboard/data/f1_cache')
    session = fastf1.get_session(2023, 'Italy', 'R')
    session.load()
    laps = session.laps.pick_quicklaps()
    laps = laps[
        (laps['LapNumber'] != 1) & (laps['TrackStatus'] == '1')
    ].copy()
    laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
    return laps

clean_laps = load_data()

st.sidebar.header("Filters")

st.header("Race Overview")
st.write(f"Total clean laps loaded: {len(clean_laps)}")

componds = clean_laps['Compound'].unique().tolist()
selected_compounds = st.sidebar.multiselect(
    label='Select Tyre Compound',
    options=componds,
    default=componds
)

drivers = sorted(clean_laps['Driver'].unique().tolist())
selected_driver = st.sidebar.multiselect(
    label='Select Drivers',
    options=drivers,
    default=drivers
)

filtered_laps = clean_laps[
    (clean_laps['Compound'].isin(selected_compounds)) & 
    (clean_laps['Driver'].isin(selected_driver))
]

col1, col2, col3 = st.columns(3)
col1.metric("Total Laps", len(filtered_laps))
col2.metric("Drivers", filtered_laps['Driver'].nunique())
col3.metric("Compounds Used", filtered_laps['Compound'].nunique())

st.subheader("Tyre Degradation")
tyre_deg = filtered_laps.groupby('TyreLife')['LapTimeSeconds'].mean().reset_index()
fig1 = px.line(tyre_deg,
                x ='TyreLife',
                y = 'LapTimeSeconds' , 
                title='Tyre degradation curve'
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Team Average Pace")
team_pace = filtered_laps.groupby('Team')['LapTimeSeconds'].mean().reset_index()
team_pace = team_pace.sort_values('LapTimeSeconds')
fig2 = px.bar(team_pace,
                x = 'LapTimeSeconds',
                y = 'Team',
                color= 'Team',
                orientation='h',
                title='Team Average Pace - Monza 2023'
)
st.plotly_chart(fig2, use_container_width=True)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Lap Time Distribution by Compound")
    fig3 = px.violin(clean_laps,
                  x= 'Compound',
                  y= 'LapTimeSeconds',
                  box= True ,
                  title= 'Lap Time Distribution by Tyre Compound'
)
    st.plotly_chart(fig3, use_container_width=True)

with col_b:
    st.subheader("Race Lap Time Progression")
    fig4 = px.scatter(clean_laps,
                   x = 'LapNumber',
                   y = 'LapTimeSeconds',
                   hover_data=['Driver', 'Team'],
                   color='Compound',
                   title='Race Lap Times — Monza 2023'
)
    st.plotly_chart(fig4, use_container_width=True)