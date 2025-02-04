import streamlit as st

def run_home():
    st.subheader('자동차 데이터를 분석하고 예측하는 APP')
    st.text('데이터는 캐글에 있는 Car_Purchasing_Data.csv를 사용합니다')
    st.text('EDA 탭에서 데이터를 분석하고 ,ML 탭에서 예측을 수행합니다')
    st.image('image/자동차.png',use_container_width=True)