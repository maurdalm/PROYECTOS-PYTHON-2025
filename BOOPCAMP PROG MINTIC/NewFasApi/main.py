# main.py

from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Definición del Modelo de Datos (Pydantic)
# BaseModel nos ayuda a definir la estructura de los datos 
# que esperamos recibir (Request Body) y enviar (Response).
class Item(BaseModel):
    """Estructura de un Item para la API."""
    id: int # Identificador único del item
    name: str # Nombre del item (cadena de texto)
    description: Optional[str] = None # Descripción (opcional)

# 2. Inicialización de la Aplicación y "Base de Datos" (Mock)
app = FastAPI()

# Simulación de una base de datos en memoria (una lista de objetos Item)
fake_items_db = [
    Item(id=1, name="Laptop", description="Computadora portátil de alto rendimiento"),
    Item(id=2, name="Mouse", description="Mouse inalámbrico",)
]

# Variable global para asignar IDs de forma incremental
next_id = 3 

# --- OPERACIONES CRUD (Create, Read, Update, Delete) ---

## 1️⃣ CREATE (Crear) - Método POST
# Se usa para **agregar** un nuevo recurso.
@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    """
    Agrega un nuevo item a la base de datos.
    El ID se asigna automáticamente.
    """
    global next_id
    item.id = next_id # Asigna el próximo ID
    next_id += 1 
    
    # Simula la inserción en la "base de datos"
    fake_items_db.append(item)
    return item # Retorna el objeto Item creado

## 2️⃣ READ (Leer) - Método GET
# Se usa para **obtener** uno o más recursos.

@app.get("/items/", response_model=List[Item])
def read_items():
    """Obtiene el listado completo de todos los items."""
    # Simula la consulta de todos los registros
    return fake_items_db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """Obtiene un item específico por su ID."""
    # Busca el item en la lista
    for item in fake_items_db:
        if item.id == item_id:
            return item
    
    # Si no se encuentra, lanza un error HTTP 404 Not Found
    raise HTTPException(status_code=404, detail="Item no encontrado")

## 3️⃣ UPDATE (Actualizar) - Método PUT
# Se usa para **reemplazar** completamente un recurso existente.

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, new_item_data: Item):
    """Actualiza completamente un item existente por su ID."""
    global fake_items_db
    
    # 1. Buscar el índice del item a actualizar
    for index, item in enumerate(fake_items_db):
        if item.id == item_id:
            # 2. Asignar el ID correcto y reemplazar el item
            new_item_data.id = item_id
            fake_items_db[index] = new_item_data
            return new_item_data # Retorna el item actualizado
            
    # Si no se encuentra, lanza un error HTTP 404 Not Found
    raise HTTPException(status_code=404, detail="Item no encontrado")

## 4️⃣ DELETE (Eliminar) - Método DELETE
# Se usa para **remover** un recurso específico.

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Elimina un item específico por su ID."""
    global fake_items_db
    
    # 1. Buscar el item a eliminar
    initial_length = len(fake_items_db)
    
    # Crea una nueva lista excluyendo el item con el ID dado
    fake_items_db = [item for item in fake_items_db if item.id != item_id]
    
    # 2. Verificar si se eliminó algo
    if len(fake_items_db) == initial_length:
        # Si la longitud no cambió, el item no existía
        raise HTTPException(status_code=404, detail="Item no encontrado para eliminar")
    
    # Retorna un 204 No Content (éxito sin cuerpo de respuesta)
    return