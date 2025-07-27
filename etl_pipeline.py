import boto3
import psycopg2
import pandas as pd
from datetime import datetime

def extract_from_s3(bucket_name, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=key)
    return pd.read_csv(response['Body'])

def transform_data(df):
    df['moderation_latency_sec'] = (pd.to_datetime(df['completed_at']) - pd.to_datetime(df['started_at'])).dt.total_seconds()
    df['is_routed_by_ml'] = df['routing_method'] == 'ML'
    df['flagged'] = df['content_flagged'].astype(int)
    df['escalated'] = df['was_escalated'].astype(int)
    return df

def load_to_redshift(df, table_name, conn):
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f'''
            INSERT INTO {table_name} (content_id, moderation_latency_sec, is_routed_by_ml, flagged, escalated)
            VALUES (%s, %s, %s, %s, %s)
        ''', (row['content_id'], row['moderation_latency_sec'], row['is_routed_by_ml'], row['flagged'], row['escalated']))
    conn.commit()

def main():
    bucket = 'content-moderation-data'
    key = 'raw/2025-07-27/moderation_log.csv'
    df_raw = extract_from_s3(bucket, key)
    df_transformed = transform_data(df_raw)

    conn = psycopg2.connect(
        dbname='moddb', user='admin', password='admin123', host='redshift-cluster.abc123.us-west-2.redshift.amazonaws.com'
    )

    load_to_redshift(df_transformed, 'moderation_metrics', conn)
    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()
