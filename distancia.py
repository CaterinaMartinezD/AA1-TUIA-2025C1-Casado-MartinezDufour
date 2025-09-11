import math

def haversine(lon1, lat1, lon2, lat2):
    """
    Calcula la distancia entre dos puntos en la Tierra usando la fórmula de Haversine.
    Parámetros en grados decimales.
    Devuelve la distancia en kilómetros.
    """
    # Radio de la Tierra en km
    R = 6371.0  

    # Convertir a radianes
    lon1_rad, lat1_rad = math.radians(lon1), math.radians(lat1)
    lon2_rad, lat2_rad = math.radians(lon2), math.radians(lat2)

    # Diferencias
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c

    return distancia

# # Ejemplo con tus datos
# pickup_longitude = -73.9998168945313
# pickup_latitude = 40.7383537292481
# dropoff_longitude = -73.99951171875
# dropoff_latitude = 40.7232170104981

# distancia_km = haversine(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)
# print(f"Distancia: {distancia_km:.3f} km")
