import streamlit as st
import pandas as pd

# タイトルの表示
st.title("一週間の勉強計画作成")

# ユーザーからの入力を受け取る
st.header("勉強内容と目標時間を入力してください")

subjects = st.text_area("勉強する科目をカンマで区切って入力してください（例：数学, 英語, プログラミング）")
study_hours = st.text_area("各科目ごとの1週間の勉強時間をカンマで区切って入力してください（例：10, 8, 12）")

# 入力がある場合に処理
if subjects and study_hours:
    # 入力されたデータをリストに変換
    subjects_list = [subject.strip() for subject in subjects.split(',')]
    hours_list = [int(hour.strip()) for hour in study_hours.split(',')]
    
    # 入力されたデータを基に勉強計画を作成
    days = ['月', '火', '水', '木', '金', '土', '日']
    
    # 各日の勉強時間を均等に割り当てる（単純な方法）
    total_hours = sum(hours_list)
    daily_hours = total_hours // len(days)  # 各日ごとの勉強時間
    remaining_hours = total_hours % len(days)  # 残り時間（余り）

    # 1週間の勉強計画を作成
    schedule = pd.DataFrame(columns=days)
    
    for idx, subject in enumerate(subjects_list):
        subject_hours = hours_list[idx]
        
        # 各科目の勉強時間を均等に分ける
        subject_schedule = [daily_hours] * len(days)
        for i in range(remaining_hours):
            subject_schedule[i] += 1
        
        # 1週間の各科目の計画を表示
        schedule[subject] = subject_schedule
    
    # 結果を表示
    st.subheader("一週間の勉強計画")
    st.write(schedule)
