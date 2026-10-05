from fastapi import FastAPI

# Inicializamos la aplicación
app = FastAPI(title="Dashboard HITL API")

# Creamos nuestra primera ruta (endpoint)
@app.get("/")
def prueba_de_vida():
    return {"mensaje": "El servidor del Dashboard HITL está vivo y respirando"}
