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

# 清理資料（補 0）
#df = df.dropna(subset=["品項"])
df = df.fillna(0)

# UI
st.subheader("請輸入紀錄")
#food_brand_option = df["品牌"].astype(str).str.strip()
#food_brand_option = food_brand_option[(food_brand_option != "") & (food_brand_option != "0") & (food_brand_option !="-")]
#food_brand_option = sorted(food_brand_option.unique()) #去掉重複的值
#food_brand_option = st.selectbox("食物的品牌", food_brand_option)
food_option = df["品項"].astype(str).str.strip()
food_option = food_option[(food_option !="") & (food_option !="0") & (food_option !="-")]
food_option = sorted(food_option.unique()) #去掉重複的值
food_option = st.selectbox("食物品項", food_option)
weight = st.number_input("請輸入重量 (g)", min_value=0.0, step=1.0)

# 計算與輸出
cleaned_food_option = str(food_option).strip()
matched_rows = df[df["品項"].astype(str).str.strip() == cleaned_food_option]
st.write("比對結果：", matched_rows)
if not matched_rows.empty:
    selected_row = matched_rows.iloc[0]
    try:
        kcal = float(selected_row["熱量 (kcal/100g)"]) * weight / 100
    except (KeyError, ValueError, TypeError):
        kcal = 0.0

    try:
        protein = float(selected_row["蛋白質 (g/100g)"]) * weight / 100
    except (KeyError, ValueError, TypeError):
        protein = 0.0
else:
    kcal = 0.0
    protein = 0.0

st.subheader("計算結果")
st.write(f"熱量：{kcal:.2f} kcal")
st.write(f"蛋白質：{protein:.2f} g")