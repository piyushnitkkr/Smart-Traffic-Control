import streamlit as st
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="Smart Traffic Control", layout="wide")
st.title("🚦 Smart Traffic Control System")

# Load traffic signal data
try:
    df = pd.read_csv("signal_output.csv")
    st.sidebar.success("✅ signal_output.csv loaded successfully")
except FileNotFoundError:
    st.sidebar.error("❌ File 'signal_output.csv' not found. Run Jupyter notebook first.")
    st.stop()

# Sidebar settings
st.sidebar.header("🛠️ Simulation Settings")
simulation_speed = st.sidebar.slider("Speed Multiplier (1 = real time)", 0.1, 5.0, 1.0, 0.1)
loop_simulation = st.sidebar.checkbox("🔁 Loop Simulation", value=False)

# Layout containers (fixed)
st.header("🔄 Signal Simulation")
lane_cols = st.columns(len(df))
lane_status = [col.empty() for col in lane_cols]
lane_progress = [col.empty() for col in lane_cols]

# Simulation function
def simulate():
    while True:
        for i, row in df.iterrows():
            duration = int(row["Duration"] / simulation_speed)
            for t in range(duration):
                for j in range(len(df)):
                    if j == i:
                        # Active lane
                        lane_status[j].markdown(f"""
                            ### Lane {j+1}  
                            🟢  
                            ⏱ {duration - t} seconds
                        """)
                        lane_progress[j].progress((t + 1) / duration)
                    else:
                        lane_status[j].markdown(f"""
                            ### Lane {j+1}  
                            🔴  
                            ⏱ 0 seconds
                        """)
                        lane_progress[j].progress(0)
                time.sleep(1 / simulation_speed)
        if not loop_simulation:
            break

simulate()
st.success("✅ Simulation Complete")
