# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]


# 1. Распаковать элементы кортежей на переменные: node_name, cpu_load, ram_usage, status. 
active_nodes = []
cpu_loads = []
ram_usages = []


for node_name, cpu_load, ram_usage, status in system_telemetry:
    # 2. Отфильтровать (проигнорировать) серверы, имеющие статус offline.
    if status == "offline":
        continue

    active_nodes.append(node_name)
    cpu_loads.append(cpu_load)
    ram_usages.append(ram_usage)


# 3. Сформировать список имен активных серверов.
print("Активные узлы в сети:", active_nodes)


# 4. Рассчитать суммарные показатели активной группы: общее количество работающих серверов, среднюю загрузку CPU 
# (с округлением до двух знаков после запятой) и пиковое (максимальное) значение использования оперативной памяти RAM.
telemetry_report = {
    "active_nodes_count": len(active_nodes),
    "metrics": {
        "average_cpu": round(sum(cpu_loads) / len(cpu_loads), 2),
        "max_ram": max(ram_usages)
    }
}


# Вывод итогового отчета
print("Итоговый отчет телеметрии:")
print(telemetry_report)