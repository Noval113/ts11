import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")
display(data.head(10))

# reading the database
data = pd.read_csv("tips.csv")

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'], c=data['size'], 
			s=data['total_bill'])

# Adding Title to the Plot
plt.title("Scatter")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()

plt.show()
