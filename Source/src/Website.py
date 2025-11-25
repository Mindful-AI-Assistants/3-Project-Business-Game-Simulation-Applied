import streamlit as st
import os
import zipfile
from io import BytesIO


st.set_page_config(page_title="Business Game", page_icon="🎮")

st.markdown("<h1 style='text-align:center;'>Business Game!</h1>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; font-size:18px;'>Bem-vindo ao <b>Business Game</b>! Baixe, jogue e acompanhe atualizações. <b>Let's do it</b>!</div>",
    unsafe_allow_html=True
)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)



#left, right = st.columns(2)

def create_zip(source_folder):
    """Cria um arquivo zip em memória a partir de uma pasta"""
    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zipf.write(file_path, arcname)
    
    zip_buffer.seek(0)
    return zip_buffer.getvalue()


# 1. Descobre o diretório onde este arquivo .py está localizado
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# 2. Cria o caminho completo para o arquivo .rar (une a pasta + o nome do arquivo)
caminho_arquivo = os.path.join(diretorio_script, "Game")


container = st.container(horizontal_alignment="center")

with container:
    st.markdown("<h2 style='text-align:center'>Windows</h2>", unsafe_allow_html=True)

    # Botão que gera o zip dinamicamente
    if st.button("Gerar e Baixar ZIP"):
        with st.spinner("Gerando arquivo ZIP..."):
            zip_data = create_zip(caminho_arquivo)
            st.download_button(
                label="📥 Baixar Business Game.zip",
                data=zip_data,
                file_name="BusinessGame.zip",
                mime="application/zip"
            )