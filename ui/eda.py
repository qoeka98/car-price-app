import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda():
    st.subheader('탐색적 데이터 분석')
    st.info('데이터를 분석합니다')  

    # CSV 파일 불러오기
    df = pd.read_csv('./data/Car_purchasing_Data.csv')
    st.dataframe(df)

    # 버튼 클릭 시 통계 데이터 보기
    if st.button('통계 데이터 보기'):
        st.dataframe(df.describe())

    # 체크박스로 상관관계 분석 표시
    if st.checkbox('상관관계 분석'):
        st.dataframe(df.corr(numeric_only=True))  

  
    menu = ['차트로 보기', '수치로 보기']
    choice = st.radio('선택하세요', menu)

    if choice == menu[0]: 
        fig1 = plt.figure(figsize=(8, 6))
        sb.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        st.pyplot(fig1)
    elif choice == menu[1]: 
        st.dataframe(df.corr(numeric_only=True))

 
    st.info('최대/최소 데이터 확인하기')
    
   
    menu2 = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']
    selected_column = st.selectbox('컬럼을 선택하세요', menu2)

   
    if selected_column:
        max_value = df[selected_column].max()
        min_value = df[selected_column].min()
        st.write(f'**최대값:** {max_value}')
        st.write(f'**최소값:** {min_value}')


if __name__ == '__main__':
    run_eda()
