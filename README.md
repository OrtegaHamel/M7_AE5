# Ejercicio M7_AE5_ABP

Por Álvaro Ortega Hamel

## 1. Recuperación de Registros con Django ORM

Se crea un modelo llamado **Producto** con los siguientes campos:

- **nombre**: `CharField` (máximo 100 caracteres)
- **precio**: `DecimalField` (5 dígitos, 2 decimales)
- **disponible**: `BooleanField`

![Ejemplo1](./img/AE5_1.png)

La base de datos se completa con una lista de 10 productos de ejemplo.

![Ejemplo1_1](./img/AE5_1_1.png)

Se utiliza el ORM de Django para recuperar todos los registros del modelo **Producto**.

![Ejemplo1_2](./img/AE5_1_2.png)

---

## 2. Aplicación de Filtros en la Recuperación de Registros

Se aplican filtros con Django ORM para obtener:

- Todos los productos con un precio mayor a 50.  
- Productos cuyo nombre comienza con la letra “A”.  
- Productos disponibles.

![Ejemplo2](./img/AE5_2_1.png)

---

## 3. Ejecución de Consultas SQL desde Django

Se escribe una consulta SQL para obtener los productos cuyo precio sea menor a 100 y se ejecuta utilizando `raw()`.

![Ejemplo3](./img/AE5_3_1.png)

---

## 4. Mapeo de Campos de Consultas al Modelo

Se ejecuta una consulta SQL personalizada con `raw()` para obtener productos con un descuento del 10%, mapeando los resultados a instancias del modelo **Producto**.

![Ejemplo4](./img/AE5_4_1.png)

---

## 5. Búsquedas e Índices

### 5.1. ¿Qué son los índices y cuál es su utilidad en Django?

Los índices son estructuras de datos que optimizan la velocidad de búsqueda en una base de datos. Funcionan como el índice de un libro, permitiendo localizar información rápidamente sin revisar todos los registros.

**Funcionamiento:**  
Un índice almacena una copia ordenada de los valores de una columna (o conjunto de columnas) junto con referencias a los registros originales.  
Al filtrar u ordenar por una columna indexada, la base de datos utiliza el índice para acceder a los resultados de forma eficiente.

**Uso en Django:**  
Se define un índice en un campo del modelo mediante el parámetro `db_index=True`.

**Cuándo usarlos:**  
- En campos utilizados frecuentemente en cláusulas `WHERE`, `ORDER BY` o `JOIN`.  
- En tablas grandes donde el rendimiento de búsqueda es importante.  
- Evitar indexar campos con pocos valores distintos (por ejemplo, un campo booleano).

### 5.2. Creación de un índice en el campo nombre del modelo Producto

![Ejemplo5_2](./img/AE5_5_2.png)

### 5.3. Verificación del impacto en la eficiencia de búsqueda

![Ejemplo5_3](./img/AE5_5_3.png)

---

## 6. Exclusión de Campos del Modelo

### 6.1. Recuperación de productos excluyendo el campo disponible

![Ejemplo6_1](./img/AE5_6_1.png)

### 6.2. Cómo maneja Django la exclusión de campos en consultas

- **Optimización SQL:** Django ajusta la consulta para incluir solo los campos necesarios mediante `only()` o `defer()`.  
- **Ahorro de memoria:** Se reducen los datos transferidos desde la base de datos.  
- **Acceso diferido:** Si se accede a un campo excluido, Django realiza una consulta adicional para obtenerlo.  
- **Rendimiento:** Ideal en modelos con muchos campos o con campos pesados como `TextField` o `JSONField`.

---

## 7. Anotaciones en Consultas

### 7.1. Uso de annotate()

Se utiliza `annotate()` para calcular un campo adicional **precio_con_impuesto**, aplicando un impuesto del 16%.  
El resultado incluye el nuevo campo calculado.

![Ejemplo7_1](./img/AE5_7_1.png)

---

## 8. Uso de Parámetros en Consultas raw()

### 8.1. Ejecución de una consulta con parámetros

![Ejemplo8_1](./img/AE5_8_1.png)

### 8.2. Diferencias y beneficios

- `%s` es un marcador de posición que Django reemplaza de forma segura, evitando inyección SQL.  
- Los parámetros se pasan en una lista que sustituye los marcadores de posición en orden.  

**Ventajas de usar parámetros:**  
- **Seguridad:** Evitan inyección SQL gracias al escape automático de valores.  
- **Reutilización:** La misma consulta puede ejecutarse con diferentes valores sin modificar su estructura.  
- **Rendimiento:** La base de datos puede reutilizar el plan de ejecución si solo cambian los parámetros.

---

## 9. Ejecución Directa de SQL con connection.cursor()

### 9.1. Ejemplos de uso: INSERT, UPDATE y DELETE

**Insertar**  
![Ejemplo9_1](./img/AE5_9_1.png)

**Actualizar**  
![Ejemplo9_2](./img/AE5_9_2.png)

**Eliminar**  
![Ejemplo9_3](./img/AE5_9_3.png)

### 9.2. Cuándo usar connection.cursor()

- Para operaciones complejas no expresables con el ORM.  
- En tareas de alto rendimiento con grandes volúmenes de datos.  
- Al ejecutar procedimientos almacenados o SQL específico del motor de base de datos.

---

## 10. Conexiones y Cursores

### 10.1. Creación manual de una conexión a la base de datos

![Ejemplo10_1](./img/AE5_10_1.png)

### 10.2. Ventajas y desventajas del uso de cursores

**Ventajas:**  
- Mayor control sobre las consultas SQL.  
- Mejor rendimiento en operaciones masivas.  
- Permite aprovechar funciones específicas del motor de base de datos.

**Desventajas:**  
- Riesgo de inyección SQL si no se usan parámetros correctamente.  
- Menor portabilidad entre diferentes bases de datos.  
- Código menos legible y más difícil de mantener.  

**Recomendaciones:**  
- Usar cursores cuando se requieran consultas SQL avanzadas o de alto rendimiento.  
- Usar el ORM para la mayoría de los casos, priorizando la legibilidad y seguridad.

---

## 11. Invocación de Procedimientos Almacenados

### 11.1. Concepto y uso

Los procedimientos almacenados son conjuntos de instrucciones SQL precompiladas que se ejecutan directamente en el servidor de la base de datos. Permiten encapsular lógica compleja, mejorar el rendimiento y reforzar la seguridad.

**Uso en Django:**  
Django no los soporta directamente en el ORM, pero pueden ejecutarse mediante `connection.cursor()` y el método `callproc()`.

**Cuándo usarlos:**  
- Para operaciones SQL complejas o repetitivas.  
- Para optimizar rendimiento en el servidor.  
- Para centralizar la lógica de negocio en la base de datos.

**Ventajas:**  
- Mayor eficiencia y seguridad.  
- Reutilización del código SQL.  
- Reducción del tráfico entre aplicación y base de datos.

**Desventajas:**  
- Menor portabilidad entre bases de datos.  
- Mantenimiento más complejo.  
- Dificultad para depurar errores.  

**Notas por motor:**  
- PostgreSQL: usa `CREATE FUNCTION`.  
- MySQL: usa `CREATE PROCEDURE`.  
- SQLite: soporte limitado.

### 11.2. Ejemplo de invocación

Se crea un procedimiento almacenado para actualizar el precio de un producto:

![Ejemplo11_1](./img/AE5_11_1.png)

Luego, se invoca desde Django usando `cursor.callproc()`:

![Ejemplo11_2](./img/AE5_11_2.png)
