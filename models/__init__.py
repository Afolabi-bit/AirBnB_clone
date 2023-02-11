#!/usr/bin/python3
"""The __init__ magic file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
