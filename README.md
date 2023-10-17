# Diario_Trader
![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/bbd7515b-40e5-44b9-bef7-3d5c3f635bbd)

<h3>Un demo de una aplicacion de flask con fastapi para crear soporte a los traders en base a una necesidad real </h3> 
<h3>Por que = Falta de apps similares con aplicaciones al mercado argentino, Costos en moneda extranjera </h3> 
<h3>Que = webapp para traders </h3> 
<h3>Para quien = Traders individuales que buscan llevar un trackrecord de sus operaciones y registrarlo de manera simple generando metricas utiles, llevando persistencia a los datos </h3> 

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/a6973997-0807-49e2-aa26-f0a2cba39751)

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/94dff370-f31c-4bbd-b11a-3457993e9541)



![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/bb813fc1-c56b-4131-bb9f-5338cbb9c414)


![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/027f6794-3a0d-4a23-9fd8-c7446da6b524)

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/ee6bd681-84d9-44a4-89b1-7fe92663acb5)


<h1>Planeacion y fundamentacion de las tecnologias y arquitectura aplicada </h1>

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/44c34302-5711-4d77-bf9b-e18f4fb57450)

<h3>Me parecio correcto elejir una arquitectura MVC, de facil implementacion y desarrollo</h3>
● Modelo (Model): ● Vista (View): ● Controlador :


![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/4e03f865-48ac-4122-b91a-0c0cb4f344a0)


<h3>Utilizo flask por su virtud para desarrollar proyectos en pequeña escala y su comunidad que genera gran documentacion</h3>

<h3>Utilizo PostgreSQL, comprobado su funcionamiento y documentacion respaldatoria. Base de dato relacional sera en este caso por la naturaleza de los datos  </h3>

Base de datos :Diseño conceptual
Modelo Entidad-Relación Cuando empezamos a pensar o diseñar una base de datos, puede parecer simple en un principio, pero en la medida que nuestra idea de base de datos crece, el diseño también crece y necesitamos una forma de poder conceptualizar y visualizar todos los elementos que la componen este modelo representación de la realidad a través de entidades.

Hay tres elementos básicos en un modelo ER: 1. Entidad 2. Atributo 3. Relación

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/c52b4909-0c8a-407c-96f8-48161edfe60a)

<h3>Utilizo FastApi ya que me parece la solucion mas correcta para generar estas estructuras de API y Micro'servicios con Python, es de facil uso con documentacion clara  </h3>
<h3>Cabe resaltar la integracion con Swagger hace mucho mas dinamico el desarrollo </h3>

![image](https://github.com/Pana-Onnti/Diario_Trader/assets/97043308/882dbc6d-e072-4254-b27a-7080f76c5457)


<h3>Criticas Back </h3>

Falta de métodos.
Puntos a favor: el sistema de inicio de sesión parece estar bien
Falta de control de acceso a recursos (CORS) y middleware.

Pruebas: falta de pruebas completas.

Diagramas para el backend:
- Diagrama de colaboración entre clases.
- Diagramas de casos de uso.

<h3>Criticas Front </h3>
Menú hamburguesa para el usuario y página para modificar la contraseña del usuario.
Responsivo en todos los dispositivos.
Modificar algunas fuentes y colores.

En general, darle un nuevo estilo más profesional, con imágenes, videos, caricaturas y efectos.

Notas de Flask: intentar evitar repetir código HTML y utilizar bloques de herencia de Jinja.

Blanco y negro + formulario.

DevOps

Docker, Kubernetes,Airflow y copias de seguridad de bases de datos, etc

