import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data = sns.load_dataset('tips')
use_data = data[['total_bill','size','time','tip']]
use_data = pd.get_dummies(use_data, drop_first=True)

X = use_data[['total_bill','size','time_Dinner']]
Y = use_data[['tip']]

clf = LinearRegression()
clf.fit(X, Y)

### STREAMLIT
import streamlit as st
st.set_page_config(layout="wide")

#タイトル
st.title('チップ額の予測')
st.header('チップ額を予測するアプリケーションです！')

#画像の挿入
from PIL import Image
image = Image.open('money.png')
st.image(image, caption='money')#, use_column_width=True)

#分析データの表示
st.header('分析用データ')
st.write('分析に使用するチップのデータです')

st.write(data.astype('object'))
st.write('データの件数は全部で',str(len(data)),'件です')

#サイドバー（分析プロット用）
st.sidebar.header('分析用プロット')
left_plot = st.sidebar.selectbox('左のボックスプロットはx軸を何にしますか？',["sex","smoker","time","day"])
right_plot = st.sidebar.selectbox('右の散布図はx軸を何にしますか？',["total_bill","size"])

#分析プロット
st.header('分析プロット')
st.write('y軸がチップの額になるプロットを作成します（左：ボックスプロット、右：散布図）')

import plotly_express as px

col1, col2 = st.beta_columns(2)
with col1:
    fig = px.box(data, x=left_plot, y='tip')
    st.plotly_chart(fig)
with col2:
    fig = px.scatter(data, x=right_plot, y='tip')
    st.plotly_chart(fig)

#サイドバー（機械学習パートのインプット）
st.sidebar.header('インプットデータ')
totalbill = st.sidebar.slider('Total bill ($)を入力してください', min_value = 0.0, max_value=50.0, step=0.5)
size = st.sidebar.slider('Size（人数）を入力してください', min_value=1, max_value=10, step=1)
dinner = st.sidebar.radio('Lunchですか？Dinnerですか？', ['Lunch','Dinner'])
if dinner=='Lunch':
    dinner01 = 0
else:
    dinner01 = 1

#Input value
st.header('インプットデータの値')
st.write('今回はインプットデータとして、totalbill, size, timeのデータを使うことにします  \n  timeデータはone-hot encodingしており、dinnerフラグとなっています')
st.write('Totalbill:', totalbill)
st.write('Size:', size)
st.write('Lunch or Dinner:', dinner)

#インプットデータの整形
value_df = pd.DataFrame([], columns=['Totalbill','Size', 'Dinner flag'])
record = pd.Series([totalbill, size, dinner01], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)

#予測
Y_pred = clf.predict(value_df)

#結果出力
st.header('チップの予測額')
st.write('チップ額はおそらく', str('{:.2g}'.format(Y_pred[0,0])), 'USドルくらいでしょう！')

