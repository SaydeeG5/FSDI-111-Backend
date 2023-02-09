import sqlite3
from flask import g 

DATABASE_URL = "main.db"

def get_db(): # allows us to keep minimal space as possible
    db = getattr(g, "_database", None)
    if not db:  # this is the same as saying if db = None 
        db = g._database = sqlite3.connect(DATABASE_URL)
    return db 