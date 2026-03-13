import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
st.title("disease prediction")
data = pd.read_excel(r"C:\Users\sushm\Downloads\diseases.xlsx")
data
if 'Unnamed: 0' in data.columns:
    data = data.drop("Unnamed: 0" ,axis=1)
x=data[['age', 'gender', 'cp', 'trestbps', 'chol', 'thalach', 'exang',
       'oldpeak']]
x = pd.get_dummies(x, columns=['gender'], drop_first=True)
y=data["disease"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
age=st.number_input("enter age: ")
gender=st.number_input("enter gender: (0 for female, 1 for male)",min_value=0,max_value=1)
cp=st.number_input("enter cp: ")
trestbps=st.number_input("enter trestbps: ")
chol=st.number_input("enter chol: ")
thalach=st.number_input("enter thalach: ")
exang=st.number_input("enter exang: ")
oldpeak=st.number_input("enter oldpeak: ")
bt=st.button("Submit")
if bt:
  predicted=model.predict([[age,gender,cp,trestbps,chol,thalach,exang,oldpeak]])
  st.write("predicted value:",predicted)