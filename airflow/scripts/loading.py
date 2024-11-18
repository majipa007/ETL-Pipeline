import psycopg2

# Connect to the production database
db_config = {
    'host': 'localhost',
    'dbname': 'db',
    'user': 'etl',
    'password': 'secret',
    'port': '5000'
}


conn = psycopg2.connect(
    host=db_config['host'],
    dbname=db_config['dbname'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port']
)

# Define the load query
def load_table(source_table, target_table, conn):
    cursor = conn.cursor()
    sql = f"INSERT INTO production.{target_table} SELECT * FROM public_analytics_schema.{source_table};"
    cursor.execute(sql)
    conn.commit()
    cursor.close()

# Load dimension tables
load_table('dim_doctors', 'dim_doctors', conn)
load_table('dim_branches', 'dim_branches', conn)
load_table('dim_risk', 'dim_risk', conn)
load_table('dim_patients', 'dim_patients', conn)

# Load fact table
load_table('fact_revenue', 'fact_revenue', conn)

conn.close()