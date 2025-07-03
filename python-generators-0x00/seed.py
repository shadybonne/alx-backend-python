#!/usr/bin/env python3

from mysql.connector import connect, Error

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'ALX_prodev'

def connect_db():
    try:
        return connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
    except Error as e:
        print(e)


def create_database(connection):
    query = f'CREATE DATABASE IF NOT EXISTS {DB_NAME}'
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
    except Error as e:
        print(e)
