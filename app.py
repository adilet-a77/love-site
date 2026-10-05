import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Для моей любимой Алии ❤️", page_icon="💖", layout="centered"
)

# Кастомные стили для романтической атмосферы
st.markdown(
    """
    <style>
    .main {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        color: #d81b60;
    }
    .stButton>button {
        background-color: #ff4081;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #e91e63;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Заголовок с именем
st.title("Сайт специально для тебя, Алия! 🥰")
st.write("Этот маленький цифровой уголок создан для того, чтобы ты улыбнулась.")

st.markdown("---")

# Красивое фото Алии
try:
  st.image(
      "aliya.jpg",
      caption="Моя самая прекрасная и любимая Алия ❤️",
      use_container_width=True,
  )
except:
  st.info(
      "💡 Подсказка: добавь фото с именем `aliya.jpg` в папку проекта, чтобы"
      " оно здесь появилось!"
  )

st.markdown("---")

# Интерактивная кнопка-сюрприз
if st.button("Нажми для сюрприза! 🎁"):
  st.balloons()
  st.success(
      "Алия, ты — самое прекрасное, что есть в моей жизни! Люблю тебя"
      " бесконечно! ❤️"
  )

st.markdown("---")

# Счетчик времени
st.subheader("⏳ Время, пока мы вместе:")
st.metric(label="Дней абсолютного счастья", value="1008")

st.markdown("---")

# Интерактивные причины
st.subheader("💌 Почему ты у меня самая лучшая:")

reasons = [
    "Твоя улыбка способна сделать прекрасным даже самый пасмурный день ✨",
    "С тобой мне невероятно тепло, легко и уютно ❤️",
    "Ты понимаешь меня так, как никто другой, моя дорогая Алия 🌸",
    "Твои глаза — самое красивое, что я когда-либо видел 👀",
]

for i, reason in enumerate(reasons, 1):
  with st.expander(f"Причина №{i} 💖"):
    st.write(reason)

st.markdown("---")

# Секретное послание внизу
st.markdown(
    "<h3 style='text-align: center; color: #ad1457;'>Сделано с бесконечной"
    " любовью для тебя, Алия! 🌹</h3>",
    unsafe_allow_html=True,
)