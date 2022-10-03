#モデリング
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X = iris.data[:,[0, 2]]
Y = iris.target

clf = LogisticRegression()
clf.fit(X, Y)

#app
import streamlit as st

#サイドバー
st.sidebar.header('Input features')
sepalValue = st.sidebar.slider('sepel length [cm]', min_value=0.0, max_value=10.0, step = 0.1) #花弁の長さ
petalValue = st.sidebar.slider('petel length [cm]', min_value=0.0, max_value=10.0, step = 0.1) #がくの長さ

#メインパネル
st.title('Iris Classifier')

#データ作成
value_df = pd.DataFrame([], columns=['data','sepal length','petal length'])
record = np.array(['data', sepalValue, petalValue])
value_df.loc[0,:] = record
value_df.set_index("data", inplace=True)

#value_df = pd.DataFrame([], columns=['data','sepal length','petal length'])
#record = pd.Series(['data',sepalValue, petalValue], index=value_df.columns)
#value_df = value_df.append(record, ignore_index=True)
#value_df.set_index("data", inplace=True)


#予測
pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs, columns=['setosa','versicolor','versinica'], index=['probability'])

#結果出力
st.write('## Input value')
st.write(value_df)

st.write('## Output probability')
st.write(pred_df)

name = pred_df.idxmax(axis=1).tolist()

st.write('## Result')
st.write('このIrisはきっと',str(name[0]), "です!")

