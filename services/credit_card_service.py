from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from utils.Config import Config
import streamlit as st


def analyze_credit_card(card_url):
    try:
        document_client = DocumentIntelligenceClient(
            endpoint=Config.ENDPOINT,
            credential=AzureKeyCredential(Config.API_KEY)
        )

        st.write(f"🔍 Analisando URL: {card_url}")

        # Método correto para a versão atual do SDK
        poller = document_client.begin_analyze_document(
            model_id="prebuilt-creditCard",
            body={
                "urlSource": card_url
            }
        )

        result = poller.result()

        st.write(f"📊 Resultado bruto recebido")

        credit_card_info = {}

        if hasattr(result, 'documents') and result.documents:
            st.write(f"📄 Documentos detectados: {len(result.documents)}")

            for i, doc in enumerate(result.documents):
                st.write(
                    f"📝 Campos disponíveis no documento: {list(doc.fields.keys())}")

                if hasattr(doc, 'fields'):
                    # Usar os nomes corretos dos campos conforme a resposta do Azure
                    card_holder_name = doc.fields.get("CardHolderName")
                    card_number = doc.fields.get("CardNumber")
                    issuing_bank = doc.fields.get("IssuingBank")
                    expiration_date = doc.fields.get("ExpirationDate")

                    credit_card_info = {
                        "card_name": card_holder_name.value_string if card_holder_name and hasattr(card_holder_name, 'value_string') else None,
                        "card_number": card_number.value_string if card_number and hasattr(card_number, 'value_string') else None,
                        "issuer": issuing_bank.value_string if issuing_bank and hasattr(issuing_bank, 'value_string') else None,
                        "expiry_date": expiration_date.value_string if expiration_date and hasattr(expiration_date, 'value_string') else None
                    }
                    st.write(f"✅ Informações extraídas: {credit_card_info}")
                    break
        else:
            st.write("❌ Nenhum documento detectado na análise")

        return credit_card_info

    except Exception as e:
        st.error(f"❌ Erro na análise do cartão: {e}")
        return {}
