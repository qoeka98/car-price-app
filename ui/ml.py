import numpy as np
import streamlit as st
import joblib

def run_ml():
    
    # 유저에게 예측에 필요한 데이터를 입력받는다
    #나이 연봉 신용카드 부채 순자산을 입력 받는다
    # 인공지능으로 예측라여 결과를 화면에 보여준다.
    st.subheader('자동차 가격 예측')
    st.text('사용자의 정보를 입력하세요')
    age= st.number_input('나이',min_value= 19, max_value=120)
    salary= st.number_input('연봉',min_value=1000)
    debt=st.number_input('신용카드 부채',min_value=0,value=10000)
    worth=st.number_input('순자산',min_value=100,value=3000)

    if st.button('구매 금액 예측하기'):
        regressor=joblib.load('model/regressor.pkl')
        new_data = np.array([[age, salary, debt, worth]])
        y_pred=regressor.predict(new_data)

        pred_data=y_pred[0]

        if pred_data <0:
            st.error('예측불가 데이터입니다')
        else:
            #소수점은 버리고 정수부분만 가져오는 것
            pred_data =round(pred_data)
            # 숫자에 3자리마다 , 콤마를 찍어주는 것
            pred_data=format(pred_data,',')
            st.success(f'예측 금액은 {pred_data}$ 입니다')


        

    



