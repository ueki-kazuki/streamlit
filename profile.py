import streamlit as st

st.title("鈴木蒼一朗")

st.header("自己紹介")
st.write("最近働き始めたエンジニアです")

st.header("趣味")
st.markdown(
    """
- ゲーム
- 岩石採取
- 受験勉強           
"""
)

st.header("好きなPythonライブラリ")
st.code("import pandas as pd", language="python")
