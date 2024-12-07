import streamlit as st
import random

# キーワードに関連するなぞなぞデータの作成
riddle_data = {
    "動物": [
        {"riddle": "飛ぶのは得意だけど、足がない動物は？", "answer": "鳥"},
        {"riddle": "いつも走っているけど、決して疲れない動物は？", "answer": "時計（ネズミ）"},
        {"riddle": "木に登るのが得意で、バナナが好きな動物は？", "answer": "サル"}
    ],
    "食べ物": [
        {"riddle": "赤くて甘くて、リーダーが食べることが多い果物は？", "answer": "りんご"},
        {"riddle": "中にご飯が入っていて、海苔で巻いているものは？", "answer": "おにぎり"},
        {"riddle": "食べると元気が出る、オレンジ色の野菜は？", "answer": "にんじん"}
    ],
    "自然": [
        {"riddle": "空から降ってきて、濡れるけど食べられるものは？", "answer": "雨"},
        {"riddle": "太陽が西に沈んでいくとき、何が変わる？", "answer": "空の色"},
        {"riddle": "みんなが集まってできる、夜空に輝くものは？", "answer": "星"}
    ]
}

# アプリのタイトル
st.title("なぞなぞに挑戦しよう！")

# キーワードの選択
st.header("なぞなぞを開始するキーワードを選んでください")
selected_topic = st.selectbox("キーワードを選んでください", options=["動物", "食べ物", "自然"])

# なぞなぞのランダムな選択
riddle_list = riddle_data[selected_topic]
riddle = random.choice(riddle_list)

# なぞなぞの表示
st.subheader("なぞなぞ: " + riddle["riddle"])

# ユーザーの答えを入力
user_answer = st.text_input("答えを入力してください")

# 答えが入力された場合
if user_answer:
    # 正解かどうかをチェック
    if user_answer.strip() == riddle["answer"]:
        st.success("正解です！")
    else:
        st.error(f"間違いです。正解は {riddle['answer']} です。")

# 次のなぞなぞに進むボタン
if st.button("次のなぞなぞ"):
    # 新しいなぞなぞを表示
    riddle = random.choice(riddle_list)
    st.subheader("なぞなぞ: " + riddle["riddle"])
    user_answer = st.text_input("答えを入力してください", key=random.randint(0, 1000))  # ランダムキーで状態更新
