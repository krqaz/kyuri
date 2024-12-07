import streamlit as st
import random

# キーワードとそれに関連するクイズデータの作成
quiz_data = {
    "数学": [
        {"question": "1 + 1 = ?", "options": ["1", "2", "3", "4"], "answer": "2"},
        {"question": "πの値は？", "options": ["3.14", "3.41", "3.00", "3.20"], "answer": "3.14"},
        {"question": "2 × 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"}
    ],
    "歴史": [
        {"question": "アメリカ独立宣言は何年に発表されたか？", "options": ["1776", "1800", "1812", "1900"], "answer": "1776"},
        {"question": "第二次世界大戦はいつ終わったか？", "options": ["1945", "1939", "1918", "1965"], "answer": "1945"},
        {"question": "ナポレオンはどこの国の出身か？", "options": ["フランス", "イギリス", "ドイツ", "イタリア"], "answer": "フランス"}
    ],
    "プログラミング": [
        {"question": "Pythonの公式のロゴに描かれている動物は？", "options": ["カメ", "ヘビ", "トカゲ", "ウサギ"], "answer": "ヘビ"},
        {"question": "HTMLのタグで見出しを表すものは？", "options": ["<header>", "<head>", "<h1>", "<div>"], "answer": "<h1>"},
        {"question": "Pythonのバージョン3.6で導入された機能は？", "options": ["f文字列", "ジェネレータ", "型アノテーション", "モジュールのインポート"], "answer": "f文字列"}
    ]
}

# アプリのタイトル
st.title("キーワード関連クイズ")

# キーワードの選択
st.header("クイズを開始するキーワードを選んでください")
selected_topic = st.selectbox("キーワードを選んでください", options=["数学", "歴史", "プログラミング"])

# クイズのランダムな選択
quiz_list = quiz_data[selected_topic]
quiz = random.choice(quiz_list)

# クイズ問題を表示
st.subheader("問題: " + quiz["question"])

# 選択肢を表示
user_answer = st.radio("選択肢:", quiz["options"])

# ユーザーが答えを選択した場合
if user_answer:
    # 正解かどうかをチェック
    if user_answer == quiz["answer"]:
        st.success("正解です！")
    else:
        st.error(f"間違いです。正解は {quiz['answer']} です。")

# クイズの進行
if st.button("次の問題"):
    # 新しいクイズを表示
    quiz = random.choice(quiz_list)
    st.subheader("問題: " + quiz["question"])
    user_answer = st.radio("選択肢:", quiz["options"], key=random.randint(0, 1000))  # ランダムキーで状態更新
