from fastapi import FastAPI, HTTPException
from .db_helper import get_item, add_item, delete_item, update_item
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    barcode: str
    name: str = None
    quantity: int = None

@app.get("/")
def home():
    return ("Message: Inventory API is running.")

@app.post("/save")
def save_item(item: Item):
    add_item(item)
    return ("Message: Item {item.barcode} saved.")

@app.get("/check/{barcode}")
def check_item(barcode: str):
    item = get_item(barcode)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item": item}

@app.delete("/delete/{barcode}")
def delete_item_by_barcode(barcode: str):
    delete_item(barcode)
    return {"message": f"Item {barcode} deleted from database."}

@app.post("/update/{barcode}")
def update_item_status(barcode: str):
    update_item(barcode)
    return {"message": f"Item {barcode} marked as completed."}

from fastapi.staticfiles import StaticFiles
app.mount("/web", StaticFiles(directory="web_ui"), name="web")
