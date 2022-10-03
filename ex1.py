import streamlit as st
st.set_page_config(layout="wide")

#文字
st.title('タイトル')
st.header('ヘッダー')
st.write('# write1')
st.write('## write2')
st.write('### write3')
st.write('#### write4')

#データフレーム
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
st.write(data.astype('object'))

#描画
import plotly.express as px
fig = px.scatter(data, x='total_bill', y='tip')
st.plotly_chart(fig)

#ウィジェット
favorite = st.selectbox('セレクトボックスです！',["apple","orange","grape"])
st.slider('スライダーです！',min_value=0, max_value=100, step=5)
st.radio('ラジオボタンです!',["apple","orange"])

st.write("好きな食べ物は何ですか？：", favorite)

#サイドバー
st.sidebar.header('ヘッダー')
st.sidebar.write('write1')

st.sidebar.selectbox('セレクトボックスです！',["apple","orange","grape"],key='test1')
st.sidebar.slider('スライダーです！',min_value=0, max_value=100, step=5,key='test2')
st.sidebar.radio('ラジオボタンです!',["apple","orange"],key='test3')

