import streamlit as st
import pandas as pd

st.title("売上データ表示")

# サンプルデータ作成
data = {"月": ["1月", "2月", "3月", "4月"], "売上(万円)": [120, 150, 135, 180]}
df = pd.DataFrame(data)

st.header("インタラクティブなテーブル(st.dataframe)")
st.dataframe(df)

st.header("静的なテーブル(st.table)")
st.table(df)
