import streamlit as st
import pandas as pd

st.title("📊 Оценки и ученици")

# Инициализация на данните
if "colors" not in st.session_state:
    st.session_state.colors = {
        "Шестица": 0,
        "Петица": 0,
        "Четворка": 0,
        "Тройка": 0,
        "Двойка": 0
    }

if "sports" not in st.session_state:
    st.session_state.sports = {
        "Гощо": 0,
        "Пешо": 0,
        "Мария": 0,
        "Гергана": 0
    }

st.subheader("Избери ученик и оценка.")

color = st.selectbox("Любим цвят:", list(st.session_state.colors.keys()))
sport = st.selectbox("Любим спорт:", list(st.session_state.sports.keys()))

if st.button("Запази избора"):
    st.session_state.colors[color] += 1
    st.session_state.sports[sport] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("📈 Резултати")

# Графика за цветовете
st.write("Любими цветове")
colors_df = pd.DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

# Графика за спортовете
st.write("Любими спортове")
sports_df = pd.DataFrame.from_dict(
    st.session_state.sports, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)
