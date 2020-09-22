import json


def get_insert_into_query(table_name, json_path):
    with open(json_path) as f:
        data = json.load(f)
        if data:
            columns = data[0].keys()
            query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES "
            for row in data:
                row = [value.strip("'") for value in row.values()]
                row = [f"'{value}'" for value in row]
                query += f"({','.join(row)}),"
    return query


sql_query = get_insert_into_query("authors", "authors.json")
print(sql_query)