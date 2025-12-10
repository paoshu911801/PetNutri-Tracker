import streamlit as st
import pandas as pd


st.title("每日紀錄")

#讀取 Excel 檔案
csv_path = "final_nutrition_data.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"找不到 Excel 檔案：{csv_path}")
    st.stop()
except Exception as e:
    st.error(f"讀取 Excel 發生錯誤：{e}")
    st.stop()
