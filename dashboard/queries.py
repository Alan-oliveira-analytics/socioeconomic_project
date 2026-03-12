# import pandas as pd
# from database import get_connection, release_connection


# def get_indicators():
#     conn = get_connection()

#     query = """
#     SELECT *
#     FROM socioeconomic_data
#     """

#     df = pd.read_sql(query, conn)

#     release_connection(conn)
    
#     df.to_parquet("data/socioeconomic_data.parquet", index=False)


#     return df


# get_indicators()