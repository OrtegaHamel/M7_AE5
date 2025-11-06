# Ejercicio M7_AE5_ABP

Por Álvaro Ortega Hamel

1 Recuperando Registros con Django ORM
Crea un modelo llamado Producto con los siguientes campos:

nombre (CharField, máximo 100 caracteres)
precio (DecimalField, 5 dígitos, 2 decimales)
disponible (BooleanField)

![Ejemplo1](./img/AE5_1.png)

Se pobla la base de datos con una lista de 10 productos de ejemplo

![Ejemplo1_1](./img/AE5_1_1.png)

Se usa el ORM de Django para recuperar todos los registros de la tabla Producto.

![Ejemplo1_2](./img/AE5_1_2.png)


2 Aplicando Filtros en Recuperación de Registros

Se utilizan filtros en Django ORM para obtener:
Todos los productos con un precio mayor a 50.
Productos cuyo nombre empiece con la letra "A".
Productos disponibles.

![Ejemplo2](./img/AE5_2_1.png)


3 Ejecutando Queries SQL desde Django

Se escribe una consulta SQL que obtenga los productos cuyo precio sea menor a 100.
Se ejecuta la consulta utilizando raw() en Django.

![Ejemplo3](./img/AE5_3_1.png)

4 Mapeando Campos de Consultas al Modelo

Se ejecuta una consulta SQL personalizada con raw() para obtener productos con un descuento del 10%.
Se mapean los resultados a una instancia del modelo Producto

![Ejemplo4](./img/AE5_4_1.png)


5. Realizando Búsquedas de Índice

5.1 Qué son los índices en bases de datos y su utilidad en Django.

Los índices son estructuras de datos especiales que optimizan la velocidad de las búsquedas en una base de datos. Funcionan de manera similar a un índice en un libro: en lugar de recorrer todas las páginas (o registros) para encontrar un dato, la base de datos usa el índice para localizar la información de manera casi instantánea.
¿Cómo funcionan?
Un índice almacena una copia ordenada de los valores de una columna (o grupo de columnas) junto con referencias a los registros originales.
Cuando se realiza una consulta que filtra o ordena por una columna indexada, la base de datos usa el índice para encontrar los resultados sin escanear toda la tabla.
¿Cómo se usan en Django?
En Django, puedes definir un índice en un campo del modelo usando el parámetro db_index=True.
¿Cuándo usarlos?
En campos que se usan frecuentemente en condiciones WHERE, ORDER BY o JOIN.
En tablas grandes donde el rendimiento de las búsquedas es crítico.
Evita indexar columnas con poca diversidad de valores (ej: un campo booleano como disponible).

5.2 Se crea un índice en el campo nombre del modelo Producto.

![Ejemplo5_2](./img/AE5_5_2.png)

5.3 Se verifica el impacto en la eficiencia de búsqueda.

![Ejemplo5_3](./img/AE5_5_3.png)


6 Exclusión de Campos del Modelo

6.1 Se recuperan todos los productos pero excluyendo el campo disponible.

![Ejemplo6_1](./img/AE5_6_1.png)

6.2 ¿Cómo Django maneja la omisión de campos en consultas?

Optimización de consultas SQL: Django modifica la consulta SQL para seleccionar solo los campos especificados en only() o excluir los campos especificados en defer(). Esto reduce la cantidad de datos transferidos desde la base de datos.
Ahorro de memoria: Al no cargar campos innecesarios, se reduce el uso de memoria en tu aplicación.
Acceso diferido: Si intentas acceder a un campo excluido (ej: producto.disponible), Django realizará una consulta adicional a la base de datos para obtener ese campo específico.
Rendimiento: Es útil cuando trabajas con modelos que tienen muchos campos o campos grandes (como TextField o JSONField), y solo necesitas algunos de ellos.


7 Añadiendo Anotaciones en Consultas

7.1 Se usa annotate() para calcular un campo adicional llamado precio_con_impuesto, donde el impuesto sea del 16%.
Se muestra el resultado con el nuevo campo.

![Ejemplo7_1](./img/AE5_7_1.png)

8 Pasando Parámetros a raw() en Django

8.1 Se ejecuta una consulta con raw(), pero esta vez utilizando parámetros en lugar de valores fijos.

![Ejemplo8_1](./img/AE5_8_1.png)

8.2 Diferencias y beneficios:

%s: Es un marcador de posición para el parámetro. Django se encarga de escaparlo correctamente para evitar inyección SQL.
precio_maximo: Lista de parámetros que reemplazarán los marcadores de posición en el orden dado.

Al usar valores fijos en consultas SQL, los datos se integran directamente en la consulta (ej: WHERE precio < 50), lo que puede exponer a riesgos de inyección SQL si los valores no son confiables. Además, este método es menos flexible, ya que modificar el valor implica cambiar la consulta.
Por otro lado, al emplear parámetros, los valores se pasan de forma separada (ej: WHERE precio < %s, [50]). Esto no solo evita riesgos de inyección SQL, ya que Django escapa automáticamente los valores, sino que también hace que la consulta sea más flexible y reutilizable, permitiendo cambiar los valores sin alterar la estructura de la consulta.
Beneficios de usar parámetros:
Seguridad: Evita inyección SQL al escapar automáticamente los valores.
Reutilización: Puedes ejecutar la misma consulta con diferentes valores sin modificar el SQL.
Rendimiento: La base de datos puede reutilizar el plan de ejecución de la consulta si solo cambian los parámetros.

9 Ejecutando SQL Personalizado Directamente

9.1 Se usa connection.cursor() para ejecutar un SQL INSERT, UPDATE o DELETE directamente en la base de datos.

Insertar
![Ejemplo9_1](./img/AE5_9_1.png)

Actualizar
![Ejemplo9_2](./img/AE5_9_2.png)

Eliminar
![Ejemplo9_3](./img/AE5_9_3.png)

9.2 ¿Cuándo es recomendable usar connection.cursor()?

Operaciones complejas: Cuando se necesita ejecutar consultas SQL que no pueden expresarse fácilmente con el ORM de Django (ej: consultas con funciones específicas de la base de datos).
Rendimiento crítico: En operaciones masivas (ej: inserciones o actualizaciones de miles de registros), donde el ORM podría ser más lento.
Procedimientos almacenados: Si se necesita llamar a procedimientos almacenados o funciones de la base de datos.
Consultas específicas de la base de datos: Cuando necesitas usar sintaxis SQL que no es compatible con el ORM de Django.

10 Conexiones y Cursores

10.1 Se crea una conexión manual a la base de datos en Django.

![Ejemplo10_1](./img/AE5_10_1.png)

10.2 Ventajas de usar cursores:

Mayor control: Se puede ejecutar consultas SQL complejas o específicas de la base de datos que no son posibles con el ORM.
Rendimiento: En operaciones masivas (ej: inserciones o actualizaciones de miles de registros), el uso directo de SQL puede ser más rápido que el ORM.
Flexibilidad: Permite usar funciones o características específicas de la base de datos que no están disponibles en el ORM.

Desventajas de usar cursores:
Seguridad: Si no se usan parámetros correctamente, puede exponerse a inyección SQL.
Mantenimiento: El código SQL es menos portable entre diferentes bases de datos (ej: SQLite, PostgreSQL, MySQL).
Legibilidad: El código SQL puede ser más difícil de leer y mantener en comparación con el ORM.
Errores: Es más fácil cometer errores en consultas SQL manuales, especialmente en proyectos grandes.

¿Cuándo usar cursores?
Cuando se necesita ejecutar consultas SQL que no pueden expresarse con el ORM.
Para operaciones masivas donde el rendimiento es crítico.
Cuando se necesita usar funciones específicas de la base de datos.

¿Cuándo usar el ORM?
En la mayoría de los casos, especialmente para consultas simples o medianamente complejas.
Cuando la portabilidad y seguridad son importantes.
Para mantener un código más limpio y fácil de entender.

11 Invocación a Procedimientos Almacenados

11.1 ¿Qué son los procedimientos almacenados?
Los procedimientos almacenados son conjuntos de instrucciones SQL precompiladas que se guardan en la base de datos. Permiten encapsular lógica compleja y ejecutarla directamente en el servidor de la base de datos, mejorando el rendimiento y la seguridad.

¿Cómo se usan en Django?
Django no tiene soporte nativo para procedimientos almacenados en su ORM, pero puedes invocarlos usando connection.cursor() y el método callproc().

¿Cuándo usar procedimientos almacenados?
Operaciones complejas: Cuando se necesita ejecutar lógica SQL compleja que no puede expresarse fácilmente con el ORM.
Rendimiento: Para reducir la carga en la aplicación y aprovechar el poder de procesamiento del servidor de la base de datos.
Seguridad: Permiten controlar el acceso a los datos y encapsular la lógica de negocio en la base de datos.

Ventajas:
Eficiencia: Reducen el tráfico de red al ejecutar múltiples operaciones en una sola llamada.
Reutilización: Pueden ser llamados desde múltiples aplicaciones.
Seguridad: Permiten definir permisos específicos para ejecutar el procedimiento.

Desventajas:
Portabilidad: La sintaxis varía entre bases de datos (PostgreSQL, MySQL, SQLite, etc.).
Mantenimiento: La lógica de negocio se divide entre la aplicación y la base de datos.
Depuración: Puede ser más difícil depurar errores en procedimientos almacenados.

Notas importantes:
PostgreSQL: Usa CREATE FUNCTION.
MySQL: Usa CREATE PROCEDURE.
SQLite: Tiene soporte limitado para procedimientos almacenados.

11.2 Se invoca un procedimiento almacenado desde Django usando cursor.callproc().

Se ejecuta el siguiente código SQL para crear un procedimiento almacenado que actualice el precio de un producto.
![Ejemplo11_1](./img/AE5_11_1.png)

Se invoca el Procedimiento desde Django
![Ejemplo11_2](./img/AE5_11_2.png)