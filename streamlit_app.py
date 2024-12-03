import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Display a simple text
st.write('Hello, World! This is a simple Streamlit app.')

# Add a slider
number = st.slider('Pick a number', 0, 100)
st.write(f'You picked {number}')

# Add a button
if st.button('Click me'):
    st.write('Button clicked!')

# Add a simple plot (using random data)
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.hist(data, bins=20)
st.pyplot(plt)
