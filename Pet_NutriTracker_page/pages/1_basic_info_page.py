import streamlit as st
import pandas as pd
from datetime import date

st.title('Pet Nutri Tracker｜基本資料輸入')

#使用者info表
with st.form('Human_Info'):
#使用者資料輸入｜姓名
    Name = st.text_input('Name')

#使用者資料輸入｜性別
    options = ["Select ur gender", "Male", "Female", "Transgender", "Non-binary / Third gender", 'Prefer not to say']
    gender_select_index = 0
    gender_select = st.selectbox('Gender', options)

#使用者資料輸入｜生日
#預設
    default_date = date(1994, 11, 19)
#設定起始與最後日期
    min_date = date(1925, 1, 1)
    max_date = date.today()
#日期輸入零件
    birth_date = st.date_input(
        label = "Please select your date of birth",
        value = default_date,
        min_value = min_date,
        max_value  =max_date
    )
#write生日
    st.write("Your birthday is:", birth_date)

#使用者資料輸入｜mail
    email = st.text_input("Your Email")

#按送出鈕
    submitted = st.form_submit_button("Send")

if submitted:
    st.write("Name:", Name)
    st.write("Gender:", gender_select)
    st.write("Date of Birth:", birth_date)
    st.write('Email', email)