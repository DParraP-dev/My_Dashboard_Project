# core/database.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las variables secretas de tu archivo .env
load_dotenv()

# Obtener los valores
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Crear el cliente (el puente de comunicación)
def obtener_cliente_supabase() -> Client:
    if not url or not key:
        raise ValueError("Faltan las credenciales de Supabase en el archivo .env")
    return create_client(url, key)

# Instanciamos la conexión para usarla en el resto del proyecto
db = obtener_cliente_supabase()
