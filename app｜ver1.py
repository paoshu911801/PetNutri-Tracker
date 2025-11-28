import streamlit as st
import pandas as pd
from datetime import date

st.title("Pet Nutri Tracker｜每日飲食紀錄")

# 日期輸入
record_date = st.date_input("日期", value=date.today())

# 食物選單
food_list = ["汪喵星球", "穩贏雞肉飼料", "巔峰主食罐"]
food = st.selectbox("食物選擇", food_list)

# 份量輸入
grams = st.number_input("攝取份量 (g)", min_value=0.0, step=5.0)

# 按鈕送出
if st.button("記錄飲食"):
    # 建立暫存紀錄（存在 session_state）
    st.session_state["log"] = st.session_state.get("log", [])
    st.session_state["log"].append({
        "日期": record_date,
        "食物": food,
        "克數": grams
    })
    st.success("已記錄成功！")

# 顯示目前記錄
st.subheader("目前輸入記錄")
if "log" in st.session_state and st.session_state["log"]:
    df = pd.DataFrame(st.session_state["log"])
    st.dataframe(df)