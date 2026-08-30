# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

connection = db_config.get("connection", {})


# 1. Извлечь значения host и port из вложенного словаря connection.
host = connection.get("host", None)
port = connection.get("port", None)

# 2. Безопасно проверить наличие ключа ssl_settings. Если этот ключ или вложенный в 
# него параметр ssl_mode отсутствуют, переменная должна принять дефолтное 
# значение verify-full. 
ssl_settings = db_config.get("ssl_settings", {})
ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

# 3. Изменить значение пользователя (user) во вложенном словаре на admin. 
# 4. Добавить новый параметр max_connections со значением 100 непосредственно во вложенный словарь connection. 
connection.update({
    "user": "admin",
    "max_connections": 100
})

# 5. Вывести обновленное содержимое конфигурации connection, используя итерацию по парам ключ-значение.
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")

for key, value in connection.items():
    print(f"* {key}: {value}")