import sqlite3
from pathlib import Path
from sqlite3 import Error, Connection, Cursor
from typing import List, Any

import pandas as pd
from constants import DATATYPES


def create_connection(database: str) -> Connection:
    try:
        root_dir = Path(__file__).parent.parent
        connection = sqlite3.connect(f'{root_dir}/db/{database}.db')
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.row_factory = sqlite3.Row
            connection.commit()
            return connection


def store_records(db: str, table: str, df: pd.DataFrame) -> None:
    try:
        conn = create_connection(db)
        df.to_sql(table, conn, if_exists="append", dtype=DATATYPES)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def get_all_records(db: str, table: str) -> List[Any]:
    try:
        conn = create_connection(db)
        query = f"""
            SELECT * FROM {table}
        """
        cur = _execute_query(conn, query)
        if cur:
            return cur.fetchall()
        else:
            return []
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def get_product_records(db: str, table: str, product: str) -> List[Any]:
    try:
        conn = create_connection(db)
        query = f"""
            SELECT * FROM {table}
            WHERE product = "{product}"
            """
        cur = _execute_query(conn, query)
        if cur:
            return cur.fetchall()
        else:
            return []
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def _execute_query(conn: Connection, query: str) -> Cursor:
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor
    except Error as e:
        print(e)
