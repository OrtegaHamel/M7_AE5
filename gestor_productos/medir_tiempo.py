from django.db import connection
import time
from productos.models import Producto

query = "SELECT * FROM productos_producto WHERE nombre LIKE 'A%'"

start_time = time.time()
with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
end_time = time.time()

print(f"Tiempo SIN índice: {end_time - start_time:.6f} segundos")
print(f"Resultados encontrados: {len(result)}")
