import streamlit as st
import pandas as pd


st.title("每日紀錄")

#讀取 Excel 檔案
excel_path = "final_nutrition_data.csv"
#哪一個sheet
sheet_name = "工作表 1"

try:
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
except FileNotFoundError:
    st.error(f"找不到 Excel 檔案：{excel_path}")
    st.stop()
except Exception as e:
    st.error(f"讀取 Excel 發生錯誤：{e}")
    st.stop()
