import datetime
import streamlit as st

st.title("Streamlitクリスマスカード 🎅")

# ボタンを押すと雪が降る
button_pushed = st.button("雪を降らせる")
if button_pushed:
    st.snow()

# テキストを入力させる
name = st.text_input(f"あなたのお名前")
# 選択肢から国を選ばせる
country = st.selectbox(f"あなたが住んでいる国", ["", "日本", "アメリカ", "中国", "オーストラリア"])

# 入力内容を表示する
st.write(name)
st.write(country)

# 名前と国が両方とも入力されたとき
if name != "" and country != "":
    st.write("必要な情報が揃いました！")

d = st.date_input("日付を選んでください", datetime.date(2025, 2, 1))
st.write("あなたの誕生日は：", d)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]} star(s).")