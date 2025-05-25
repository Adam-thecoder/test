import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(20,4),
     columns=["a","b","c","d"]
)
st.set_page_config(
     page_title= "Data charts",
     page_icon= "📊",
     layout= 'centered'
)
     

st.bar_chart(chart_data)
st.line_chart(chart_data)

