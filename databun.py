import streamlit as st
import pandas as pd
import matplotlib.pyplot  as plt

st.title("シンプルなデータ分析アプリ") #アプリのタイトルタイトル

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"]) # CSVファイルのアップロード

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("データレビュー", df.head()) # データフレームデータフレーム表示

    columns = df.columns.tolist() # 列選択
    selected_column = st.selectbox("分析したい列を選んでください", columns)
    st.write("基本統計情報", df[selected_column].describe())

    fig, ax = plt.subplots()
    df[selected_column].hist(ax=ax, bins=20)
    st.pyplot(fig)

