# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

url = "https://docs.google.com/spreadsheets/d/1iQXmKw0rvLhvB7BKXZZqZVm4Xg0K8YZqKDnZ6zHkOLE/edit#gid=692283458"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
pd.DataFrame(data)
data['PESO'] = data['PESO'].str.replace(',', '.').astype(float)
data['PESO'] = data['PESO'].replace('.', ',')
data['PESO'] = round(data['PESO'], 0).astype(int)
st.write(data.dtypes)
st.dataframe(data)

cores_por_raça = {
                    'TLLZZ - TN70': 'gray',
                    'TZZZZ - AVÓ':'red'
}
grafico  = px.scatter(data, x='IDADE', y='PESO', color='RAÇA', color_discrete_map=cores_por_raça)
st.plotly_chart(grafico)