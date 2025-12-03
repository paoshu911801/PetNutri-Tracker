import streamlit as st
import pandas as pd
from datetime import date

st.title('Pet Nutri Tracker｜基本資料輸入')

#分兩欄位
col1, col2 = st.columns(2)

with col1:
    st.write('這裡填您的資料', key = 'user_title')

#使用者info表
    with st.form('Human_Info'):
#使用者資料輸入｜姓名
        name = st.text_input('Name', key = 'user_name')

#使用者資料輸入｜性別
        options = ["Select ur gender", "Male", "Female", "Transgender", "Non-binary / Third gender", 'Prefer not to say']
        gender_select_index = 0
        gender_select = st.selectbox('Gender', options, key = 'user_gender')

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
        st.write("Your Birthday is:", birth_date, key = 'user_birth')

#使用者資料輸入｜mail
        email = st.text_input("Your Email", key = 'user_mail')

#按送出鈕(Human)
        user_submitted = st.form_submit_button("Send")

    if user_submitted:
        st.write("Name:", name)
        st.write("Gender:", gender_select)
        st.write("Date of Birth:", birth_date)
        st.write('Email', email)

with col2:
    st.write('這裡填狗勾的資料', key = 'pet_title')

#寵物info表
    with st.form('pet_info'):
#寵物資料輸入｜姓名
        pet_name = st.text_input('Name', key = 'pet_name')

#寵物資料輸入｜性別
        pet_options = ["which gender", "Male", "Female", 'Prefer not to say']
        pet_gender_select_index = 0
        pet_gender_select = st.selectbox('Pet\'s Gender', pet_options, key = 'pet_gender')
#寵物資料輸入｜生日
#預設
        default_pet_date = date(2021, 2, 5)
#設定起始與最後日期
        pet_min_date = date(2000, 1, 1)
        pet_max_date = date.today()
#日期輸入零件
        pet_birth_date = st.date_input(
            label = "Please select baby\'s date of birth",
            value = default_pet_date,
            min_value = pet_min_date,
            max_value  = pet_max_date
        )
#write生日
        st.write("Baby\'s Birthday is:", pet_birth_date, key = 'pet_birth')

#品種
        pet_breed_options = ['Mix', 'Poodle', 'Husky', 'Corgi', 'French Bulldog', 'Others']
        pet_breed = st.selectbox('Breed', pet_breed_options, index = 0)
        st.write('Breed:', pet_breed, key = 'pet_breed')

#體重
        pet_weight = st.number_input('Baby\'s Weight(kg)', key = 'pet_weight')

#毛色
        pet_color = st.text_input('Baby\'s Color', key = 'pet_color')

#飲食習慣
        pet_diet_options = ['平常吃什麼', '乾飼料', '濕飼料', '乾濕混合', '鮮食']
        pet_diet = st.selectbox('What Baby Eat', pet_diet_options, index = 0)
        st.write('What Baby Eat A Day', key = 'pet_diet')

#每日運動量
        pet_activity_options = ['低活動量', '中活動量', '高活動量']
        pet_activity = st.radio('pet_activity', pet_activity_options, index = 0)
        st.write('參考以下說明判斷活動量喔', key = 'pet_activity')

#每日活動量說明
        pet_activity_instruction = st.markdown(
            "低活動量：室內為主，每日短暫散步少於1小時，可能有肥胖傾向或老年犬。\n  "
            "中活動量：每日散步1-3小時，體態平衡。\n  "
            "高活動量：每日劇烈運動超過3小時，如跑步或敏捷訓練。"
        )

#按送出鈕(Pet)
        pet_submitted = st.form_submit_button("Send")

    if pet_submitted:
        st.write("Baby\'s Name:", pet_name)
        st.write("Baby\'s Gender:", pet_gender_select)
        st.write("Baby\'s Date of Birth:", pet_birth_date)
        if pet_breed == 'Others':
            other_breed = st.text_input('Please specify the breed')
            st.write('Breed:', other_breed)
        else:
                st.write('Breed:', pet_breed)
        st.write('Weight:', pet_weight)
        st.write('Skin Color:', pet_color)
        st.write('Diet:', pet_diet)
        st.write('Activity Level', pet_activity)