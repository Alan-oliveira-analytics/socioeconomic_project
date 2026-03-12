# import psycopg2
# from psycopg2 import pool
# from config import DB_CONFIG

# connection_pool = psycopg2.pool.SimpleConnectionPool(
#     minconn=1,
#     maxconn=10,
#     **DB_CONFIG
# )


# def get_connection():
#     return connection_pool.getconn()


# def release_connection(conn):
#     connection_pool.putconn(conn)