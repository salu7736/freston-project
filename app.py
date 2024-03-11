import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("""
Credit Limit Prediction
""")
st.write('---')
 
data=pd.read_csv('fixed.csv')
x=data.drop('Credit_limit',axis=1)
y=data['Credit_limit']
 
st.sidebar.header('inputs')
 
def user_input_features():
    Own_car_min = int(x['Own_car'].min())
    Own_car_max = int(x['Own_car'].max())
    Own_property_min=int(x['Own_property'].min())
    Own_property_max=int(x['Own_property'].max())
    Total_income_min = max(int(data['Total_income'].min()), 100000)
    Total_income_max=int(x['Total_income'].max())
    Total_income_mean=int(x['Total_income'].mean())
    Age_min=int(x['Age'].min())
    Age_max=int(x['Age'].max())
    Age_mean=int(x['Age'].mean())
    Years_employed__mean=int(x['Years_employed'].mean())
    Occupation_min=int(x['Occupation'].min())
    Occupation_max=int(x['Occupation'].max())
    Occupation_mean=int(x['Occupation'].mean())    
    Own_car = st.sidebar.slider('Own_car', Own_car_min, Own_car_max)
    Own_property = st.sidebar.slider('Own_property', Own_property_min, Own_property_max)
    # Use text_input for Total_income
    Total_income = st.sidebar.number_input('Total_income',Total_income_min,Total_income_max,Total_income_mean)
    # Use number_input for Age
    Age = st.sidebar.number_input('Age',Age_min,Age_max,Age_mean)
    Years_employed = st.sidebar.number_input('Years_employed',Years_employed__mean)    
    occupation_descriptions = {
    0: 'Unskilled',
    1: 'Unknown',
    2: 'Skilled',
    3: 'Professional'
}
    # Using a select box for Occupation input
    Occupation = st.sidebar.selectbox('Occupation', [0, 1, 2, 3], format_func=lambda x: occupation_descriptions[x])
    data1 = {'Own_car': Own_car, 'Own_property': Own_property, 'Total_income': Total_income, 'Age': Age, 'Years_employed': Years_employed,'Occupation': Occupation}
    features = pd.DataFrame(data1, index=[0])
    return features


df=user_input_features()

st.header('specified input features')
st.write(df)
st.write('---')

model=LinearRegression()
model.fit(x,y)
prediction=model.predict(df)
    
st.header('Prediction')
st.write(f"The predicted credit limit is: {prediction[0]:.2f}")
st.write('---')
