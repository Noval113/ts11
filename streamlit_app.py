import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv("tips.csv")

st.subheader("Scatter Plot")
plt.scatter(data['day'], data['tip'], c=data['size'], 
			s=data['total_bill'])

plt.title("Scatter")

plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()
st.pyplot()

data = pd.read_excel("ds_salaries.xlsx")
st.subheader("Bar - Salary)
plt.bar(data['company_size'], data['salary'])
plt.title("Salary in job title")
plt.xlabel('company size')
plt.ylabel('salary')
st.pyplot()
