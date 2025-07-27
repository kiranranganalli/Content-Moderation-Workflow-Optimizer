import pandas as pd
import psycopg2

def load_to_redshift(csv_file, conn_params):
    df = pd.read_csv(csv_file)
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("INSERT INTO moderation_routing (content_id, assigned_to, cost) VALUES (%s, %s, %s)",
                       (row['content_id'], row['assigned_to'], row['cost']))
    conn.commit()
    cursor.close()
    conn.close()