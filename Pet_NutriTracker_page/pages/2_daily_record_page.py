import streamlit as st
import pandas as pd


st.title("每日紀錄")

#讀取 Excel 檔案
csv_path = "../final_nutrition_data.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"找不到 Excel 檔案：{csv_path}")
    st.stop()
except Exception as e:
    st.error(f"讀取 Excel 發生錯誤：{e}")
    st.stop()
st.write("目前欄位名稱：", df.columns.tolist())


# === 2. 清理資料（補 0、移除空白食物）===
#df = df.dropna(subset=["品項"])
df = df.fillna(0)
st.write("df shape：", df.shape)
st.dataframe(df)

# === 3. UI ===
st.subheader("請輸入紀錄")
food_option = st.selectbox("選擇食物", df["品項"])
weight = st.number_input("請輸入重量 (g)", min_value=0.0, step=10.0)

# === 4. 計算與輸出 ===
selected_row = df[df["品項"] == food_option].iloc[0]
kcal = selected_row.get("熱量 (kcal/100g)", 0) * weight / 100
protein = selected_row.get("蛋白質 (g/100g)", 0) * weight / 100

st.subheader("計算結果")
st.write(f"熱量：{kcal:.2f} kcal")
st.write(f"蛋白質：{protein:.2f} g")