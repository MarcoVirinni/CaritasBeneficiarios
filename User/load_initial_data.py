import os
from django.db import connection
from django.conf import settings
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def load_data_script(sender, **kwargs):
    sql_file_path = os.path.join(settings.BASE_DIR, 'User', 'initial_data.sql')

    if not os.path.exists(sql_file_path):
        print(f'SQL file not found: {sql_file_path}')
        return

    affected_tables = ['roles', '"user"']

    with connection.cursor() as cursor:
        for table in affected_tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                if count == 0:
                    with open(sql_file_path, 'r') as file:
                        sql = file.read()
                    # Extraer sólo los statements para esta tabla
                    table_sql = extract_table_data(sql, table)
                    if table_sql:
                        for stmt in table_sql:
                            stmt = stmt.strip()
                            if stmt:
                                cursor.execute(stmt)
                        print(f'Successfully loaded data for table {table}')
            except Exception as e:
                print(f"Skipping table {table}: {e}")
                continue

def extract_table_data(sql, table):
    # Separa por ';' y filtra statements que tengan INSERT INTO table o similares
    statements = sql.split(';')
    table_statements = []
    clean_table = table.replace('"', '').lower()

    for stmt in statements:
        stmt_lower = stmt.lower()
        # Buscamos statements que contengan el nombre exacto de la tabla después de INSERT INTO o UPDATE
        if f"insert into {clean_table}" in stmt_lower or f"update {clean_table}" in stmt_lower:
            table_statements.append(stmt + ';')

    return table_statements if table_statements else None
