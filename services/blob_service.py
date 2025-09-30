import os
import streamlit as st
from utils.Config import Config
from azure.storage.blob import BlobServiceClient, PublicAccess


def upload_to_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION_STRING)

        # Verificar se o container existe e configurar acesso público se necessário
        container_client = blob_service_client.get_container_client(
            Config.CONTAINER_NAME)

        # Tentar criar o container se não existir
        try:
            container_client.create_container(public_access=PublicAccess.BLOB)
        except Exception:
            # Container já existe, continuar
            pass

        blob_client = blob_service_client.get_blob_client(
            container=Config.CONTAINER_NAME, blob=file_name)

        # Fazer upload
        blob_client.upload_blob(file, overwrite=True)

        return blob_client.url

    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
        return None
