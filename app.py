import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Assembly QR", page_icon="🤖")

query_params = st.query_params
part = query_params.get("part", "76809-89402D")
robot = query_params.get("Robot", "RB134")
substation = query_params.get("Sub", "5")

st.title("📦 ระบบบันทึกงาน Assembly")

with st.form("log_form"):
    st.markdown("### 🔍 ตรวจเช็คข้อมูล")
    st.text_input("📦 Part", part, disabled=True)
    st.text_input("🤖 Robot", robot, disabled=True)
    st.text_input("📍 Substation", substation, disabled=True)

    name = st.text_input("👤 กรอกชื่อพนักงาน")

    submitted = st.form_submit_button("✅ บันทึกข้อมูล")

    if submitted:
        if name.strip() == "":
            st.error("❗ กรุณากรอกชื่อก่อน")
        else:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = pd.DataFrame([[now, name, part, robot, substation]],
                              columns=["Timestamp", "Name", "Part", "Robot", "Substation"])
            df.to_csv("log.csv", mode='a', header=False, index=False)
            st.success("📌 บันทึกสำเร็จ!")