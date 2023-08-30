import math
# Расчет дистанции заказа
def calculate_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    radius = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance
# Построение координат маршрута
def build_route(start_point, end_point, step_size):
    route = []
    lat_diff = end_point[0] - start_point[0]
    lon_diff = end_point[1] - start_point[1]
    distance = calculate_distance(start_point, end_point)
    num_steps = int(distance / step_size)

    for i in range(num_steps + 1):
        lat = start_point[0] + (lat_diff * i / num_steps)
        lon = start_point[1] + (lon_diff * i / num_steps)
        route.append((lat, lon))
    return route
# Проверка подходит ли заказ
def find_suitable_orders(start_point, end_point, orders, step_size=0.1):
    route = build_route(start_point, end_point, step_size)
    suitable_orders = []

    for order in orders:
        order_start = (order['start'][0], order['start'][1])
        order_end = (order['end'][0], order['end'][1])

        start_distance = min(calculate_distance(order_start, point) for point in route)
        end_distance = min(calculate_distance(order_end, point) for point in route)

        if start_distance <= 0.5 and end_distance <= 1.0:
            suitable_orders.append(order['order_id'])

    return suitable_orders


# Начальная точка первого заказа
start_point = (62.011175, 129.681262)
end_point = (62.086652, 129.749248)
# Заказы
orders = [
    {'order_id': 1, 'start': (62.023265, 129.694207), 'end': (62.035549, 129.716148)},
    {'order_id': 2, 'start': (62.020875, 129.719627), 'end': (61.991863, 129.677520)},
    {'order_id': 3, 'start': (62.026108, 129.702459), 'end': (62.030987, 129.708674)},
    {'order_id': 4, 'start': (62.011175, 129.681262), 'end': (62.038952, 129.731509)}
]
# Вызов алгоритма и передача данных
suitable_orders = find_suitable_orders(start_point, end_point, orders)
print("Попутные заказы:", suitable_orders)
