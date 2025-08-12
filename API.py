from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="BoomBurger API", version="2.0")


def validar_email(email: str) -> bool:
    return "@" in email and "." in email


MENU_ITEMS = [
    "BoomBurger Sencilla",
    "EspecialBoomBurger",
    "KangreBoom"
]


class Registro(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del usuario")
    email: str = Field(min_length=5, description="Correo electrónico a validar")


@app.get("/menu")
def get_menu():
    return {"menu": MENU_ITEMS}


@app.post("/registro")
def post_registro(data: Registro):
    if not validar_email(data.email):
        raise HTTPException(status_code=400, detail="Correo electrónico inválido")

    return {
        "status": "ok",
        "mensaje": f"Usuario '{data.nombre}' registrado con éxito."
    }
