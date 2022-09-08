import streamlit as st
import pandas

chart = {
    "Serias1": [1,2,3,4,5],
    "Serias2": [6,3,4,7,6]
}

df = pandas.DataFrame(chart)

st.title("Первое приложение на streamlit")
st.subheader("Публичный сайт на Python")
st.write("Здесь указан наш текст")
st.write(df)
st.area_chart(df)
st.line_chart(df)

mainslider = st.slider("Футы")
st.write(mainslider, " в метрах ", mainslider * 0.3)