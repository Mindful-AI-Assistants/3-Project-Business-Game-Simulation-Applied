import streamlit as st

st.set_page_config(page_title="Business Game", page_icon="🎮")

st.markdown("<h1 style='text-align:center;'>Business Game!</h1>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; font-size:18px;'>Bem-vindo ao <b>Business Game</b>! Baixe, jogue e acompanhe atualizações. <b>Let's do it</b>!</div>",
    unsafe_allow_html=True
)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    left.markdown('<h1>Windows</h1>', unsafe_allow_html=True)
    
    with open("downloads\\Business_Game.rar", "rb") as f:
        left.download_button("Business Game.rar", f.read(), file_name="BusinessGame.rar", mime="application/x-rar-compressed")
    
    with open("downloads\\Business Game.zip", "rb") as f:
        left.download_button("Business Game.zip", f.read(), file_name="BusinessGame.zip", mime="application/x-zip-compressed")
        