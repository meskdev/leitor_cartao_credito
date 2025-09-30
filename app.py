import streamlit as st
from services.blob_service import upload_to_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title("Validação de Documentos com Azure")
    uploaded_file = st.file_uploader("Escolha um arquivo pdf ou Imagem", type=[
                                     "pdf", "png", "jpg", "jpeg"])
    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o blob storage
        blob_url = upload_to_blob(uploaded_file, fileName)
        if blob_url:
            st.write(
                f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage!")
            # Chamar função de detecção de informações de cartão de crédito
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write("Erro ao enviar o arquivo para o Azure Blob Storage.")


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_container_width=True)
    st.write("Resultado da Validação:")

    # Melhor lógica de validação
    is_valid = False
    card_data = {}

    if credit_card_info:
        # Verificar se pelo menos o número do cartão foi detectado
        card_number = credit_card_info.get("card_number")
        card_name = credit_card_info.get("card_name")
        issuer = credit_card_info.get("issuer")
        expiry_date = credit_card_info.get("expiry_date")

        # Considerar válido se tiver número OU nome do cartão
        if card_number or card_name:
            is_valid = True
            card_data = {
                "card_name": card_name,
                "card_number": card_number,
                "issuer": issuer,
                "expiry_date": expiry_date
            }

    if is_valid:
        st.markdown(f"<h1 style='color:green;'>Cartão Válido</h1>",
                    unsafe_allow_html=True)
        if card_data["card_name"]:
            st.write(f"Nome no Cartão: {card_data['card_name']}")
        if card_data["card_number"]:
            st.write(f"Número do Cartão: {card_data['card_number']}")
        if card_data["issuer"]:
            st.write(f"Banco Emissor: {card_data['issuer']}")
        if card_data["expiry_date"]:
            st.write(f"Data de Validade: {card_data['expiry_date']}")

        # Mostrar informações completas para debug
        st.write("---")
        st.write("**Informações completas detectadas:**")
        st.json(credit_card_info)
    else:
        st.markdown(f"<h1 style='color:red;'>Cartão Inválido ou não detectado</h1>",
                    unsafe_allow_html=True)
        st.write(
            "Não foi possível detectar informações válidas do cartão de crédito.")

        # Mostrar o que foi retornado para debug
        if credit_card_info:
            st.write("**Dados retornados (para debug):**")
            st.json(credit_card_info)


if __name__ == "__main__":
    configure_interface()
