import streamlit as st

st.title("簡易To-Doリスト")

# session_stateの初期化
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# タスク入力
new_task = st.text_input("新しいタスクを入力")

# タスク追加ボタン
if st.button("追加"):
    if new_task:
        st.session_state.tasks.append(new_task)
    else:
        st.warning("タスクを入力してください。。")

# タスク一覧表示
st.header("現在のタスク")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"{i+1}.{task}")
else:
    st.info("タスクはありません。")
