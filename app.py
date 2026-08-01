print('HELLO WORD')
# vibeconding- programar copiloto- IA Generativa
# procoding
import streamlit as st
import pandas as pd
st.title('Minha web page')
st.map()
dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)
st.map()

#graficos

st.bar_chart(df, x = 'vendedor', y = 'vendas')
st.map()



