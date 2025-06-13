import streamlit as st

st.title("easyアンケート")

# 入力ウィジェット
name = st.text_input("名を残す")
month_group = st.radio(
    "何月生まれですか？",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"),
)
fish = st.selectbox("一番好きな魚は？", ("鮭", "鯖", "鱈", "太刀魚"))

# 送信ボタン
if st.button("送信"):
    st.write("---")
    st.write(
        "ご回答ありがとうございます！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"
    )
    st.write(f"**名:**{name}")
    st.write(f"**生まれ月:**{month_group}")
    st.write(f"**好きなSAKANNNNNNA:**{fish}")
