import psycopg2


def get_connection():

    return psycopg2.connect(
        host="aws-0-us-east-1.pooler.supabase.com",
        port=5432,
        database="postgres",
        user="postgres.rzbwjavzsmpbkygilhfo",
        password="43759816JACK7",
        sslmode="require"
    )


# ------------------------------------------------------------------
# Credenciales para la API de Storage (distintas a las de Postgres).
# Reemplaza SUPABASE_KEY por tu key real de este proyecto
# (Project Settings > API Keys en el dashboard de Supabase).
# ------------------------------------------------------------------
SUPABASE_URL = "https://rzbwjavzsmpbkygilhfo.supabase.co"
SUPABASE_KEY = "sb_publishable__Gt_tL4-lp2iqPSNshaPsA_k9N5eUma"