import sqlite3

DB_FILE = "inventory.db"

def connect():
    return sqlite3.connect(DB_FILE)

def add_item(item):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO components (barcode, name, quantity) VALUES (?, ?, ?)",
              (item.barcode, item.name, item.quantity))
    conn.commit()
    conn.close()

def get_item(barcode):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM components WHERE barcode=?", (barcode,))
    item = c.fetchone()
    conn.close()
    return item

def delete_item(barcode):
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM components WHERE barcode=?", (barcode,))
    conn.commit()
    conn.close()

def update_item(barcode):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO completed (barcode) VALUES (?)", (barcode,))
    conn.commit()
    conn.close()
