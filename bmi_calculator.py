import streamlit as st

st.title("")

# 　身長と体重の入力
height = st.number_input(
    "身長(cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1
)
weight = st.number_input(
    "体重(kg)", min_value=30.0, max_value=200.0, value=65.0, step=0.1
)

# 　計算ボタン
if st.button("計算する"):
    # 　BMIの計算
    bmi = weight / ((height / 100) ** 2)
    st.write(f"あなたのBMIは**{bmi:.2f}**です")

    # 　判定
    if bmi < 18.5:
        st.info("低体重です。")
    elif 18.5 <= bmi < 25:
        st.success("普通体重です。")
    else:
        st.warning("肥満です。")
