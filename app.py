
import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Smart Waste Management", layout="wide")

st.title("🗑️ Smart Waste Management & Bin Level Detection System")

bin_height = st.sidebar.slider("Bin Height (cm)", 20, 100, 30)
distance = st.sidebar.slider("Current Distance From Sensor (cm)", 0, bin_height, 15)

fill_percentage = max(0, min(100, ((bin_height-distance)/bin_height)*100))

if fill_percentage < 50:
    status = "Empty"
elif fill_percentage < 80:
    status = "Half Full"
else:
    status = "Full"

c1,c2,c3 = st.columns(3)
c1.metric("Distance (cm)", distance)
c2.metric("Fill %", f"{fill_percentage:.1f}%")
c3.metric("Status", status)

st.progress(fill_percentage/100)

if fill_percentage >= 80:
    st.error("⚠️ Collection Alert: Bin is nearly full!")
else:
    st.success("Bin operating normally")

if st.button("Generate Sample Log"):
    rows=[]
    for i in range(20):
        d=random.randint(1,bin_height)
        f=((bin_height-d)/bin_height)*100
        rows.append([datetime.now(), d, round(f,2)])
    df=pd.DataFrame(rows, columns=["Timestamp","Distance","FillPercentage"])
    df.to_csv("data/bin_logs.csv", index=False)
    st.dataframe(df)
    st.success("CSV log generated in data/bin_logs.csv")

st.subheader("Project Overview")
st.write("Virtual IoT simulation for smart waste monitoring using ultrasonic bin-level detection.")
