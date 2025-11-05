6 ¿Cómo Django maneja la omisión de campos en consultas?

Optimización de consultas SQL: Django modifica la consulta SQL para seleccionar solo los campos especificados en only() o excluir los campos especificados en defer(). Esto reduce la cantidad de datos transferidos desde la base de datos.
Ahorro de memoria: Al no cargar campos innecesarios, se reduce el uso de memoria en tu aplicación.
Acceso diferido: Si intentas acceder a un campo excluido (ej: producto.disponible), Django realizará una consulta adicional a la base de datos para obtener ese campo específico.
Rendimiento: Es útil cuando trabajas con modelos que tienen muchos campos o campos grandes (como TextField o JSONField), y solo necesitas algunos de ellos.

8 Pasando Parámetros a raw() en Django
Explicación:

%s: Es un marcador de posición para el parámetro. Django se encarga de escaparlo correctamente para evitar inyección SQL.
precio_maximo: Lista de parámetros que reemplazarán los marcadores de posición en el orden dado.

Al usar valores fijos en consultas SQL, los datos se integran directamente en la consulta (ej: WHERE precio < 50), lo que puede exponer a riesgos de inyección SQL si los valores no son confiables. Además, este método es menos flexible, ya que modificar el valor implica cambiar la consulta.
Por otro lado, al emplear parámetros, los valores se pasan de forma separada (ej: WHERE precio < %s, [50]). Esto no solo evita riesgos de inyección SQL, ya que Django escapa automáticamente los valores, sino que también hace que la consulta sea más flexible y reutilizable, permitiendo cambiar los valores sin alterar la estructura de la consulta.

Beneficios de usar parámetros:

Seguridad: Evita inyección SQL al escapar automáticamente los valores.
Reutilización: Puedes ejecutar la misma consulta con diferentes valores sin modificar el SQL.
Rendimiento: La base de datos puede reutilizar el plan de ejecución de la consulta si solo cambian los parámetros.

9 ¿Cuándo es recomendable usar connection.cursor()?

Operaciones complejas: Cuando necesitas ejecutar consultas SQL que no pueden expresarse fácilmente con el ORM de Django (ej: consultas con funciones específicas de la base de datos).
Rendimiento crítico: En operaciones masivas (ej: inserciones o actualizaciones de miles de registros), donde el ORM podría ser más lento.
Procedimientos almacenados: Si necesitas llamar a procedimientos almacenados o funciones de la base de datos.
Consultas específicas de la base de datos: Cuando necesitas usar sintaxis SQL que no es compatible con el ORM de Django.

10 Ventajas de usar cursores:

Mayor control: Puedes ejecutar consultas SQL complejas o específicas de la base de datos que no son posibles con el ORM.
Rendimiento: En operaciones masivas (ej: inserciones o actualizaciones de miles de registros), el uso directo de SQL puede ser más rápido que el ORM.
Flexibilidad: Permite usar funciones o características específicas de la base de datos que no están disponibles en el ORM.

Desventajas de usar cursores:

Seguridad: Si no usas parámetros correctamente, puedes exponerte a inyección SQL.
Mantenimiento: El código SQL es menos portable entre diferentes bases de datos (ej: SQLite, PostgreSQL, MySQL).
Legibilidad: El código SQL puede ser más difícil de leer y mantener en comparación con el ORM.
Errores: Es más fácil cometer errores en consultas SQL manuales, especialmente en proyectos grandes.

¿Cuándo usar cursores?

Cuando necesitas ejecutar consultas SQL que no pueden expresarse con el ORM.
Para operaciones masivas donde el rendimiento es crítico.
Cuando necesitas usar funciones específicas de la base de datos.

¿Cuándo usar el ORM?

En la mayoría de los casos, especialmente para consultas simples o medianamente complejas.
Cuando la portabilidad y seguridad son importantes.
Para mantener un código más limpio y fácil de entender.


11 ¿Qué son los procedimientos almacenados?
Los procedimientos almacenados son conjuntos de instrucciones SQL precompiladas que se guardan en la base de datos. Permiten encapsular lógica compleja y ejecutarla directamente en el servidor de la base de datos, mejorando el rendimiento y la seguridad.

¿Cómo se usan en Django?
Django no tiene soporte nativo para procedimientos almacenados en su ORM, pero puedes invocarlos usando connection.cursor() y el método callproc().

¿Cuándo usar procedimientos almacenados?

Operaciones complejas: Cuando necesitas ejecutar lógica SQL compleja que no puede expresarse fácilmente con el ORM.
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