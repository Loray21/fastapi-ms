## Fast api - Microservicios



# CORRER APLICACION



1.  
``` python
pip install requirements.txt
```

2. levantar la aplicacion junto con la base de datos
``` python
uvicorn main:app --reload
```

3. Descargarse cliente de mysql ej:
https://www.sqlite.org/

4. entrar a la base de datos

``` bash
sqlite3 todos.db
```

4. configure db

- ver schema

``` sql 
 .schema

 ```

- insertar registros:

``` sql 
 insert into todos (title,description,priority,complete) values ('Go to the store' , 'Pick up eggs', 5 , False)
```

- configurar modo columnas.

``` sql
.mode columns   

.mode table

```



## USER MODELS





## hash password
pip install passlib
pip install Bcrypt==4.0.1

hay que instalar esa version prq passlib y Bcrypt trabajan juntos.


## json web token review

- es uno  de los protocolos mas populares dentro de las api

- cada vez que el cliente hace un peticion al servidor le manda el jwt y el servidor chequea su validez

estructura:

- header: (a)
- Payload (b)
- Signature (c)

formato:

aaaaaa.bbbbbb.cccccc

1. headers

suele tener dos partes , el algoritmo utilizado para firmar y el type

ej

``` json
{
"alg":"HS256",
"TYP": "JWT"
}

esto se codifica y forma la primera parte del token.

2. payload 

contiene la informacion del usuario y informacion extra.

ej:
``` json
{
    "sub": 1234567@,
    "name": "Eric Roby",
    "given_name": "Eric",
    "email": "cofingwithtomi@gmail.com"
}

esto se codifica y forma la segunda parte del token.


3. jwt signature

la signature es la firma del token y se obtiene hashseando el contenido anterior segun el algoritmo en el header

ej:
``` json
HMACSHA256(
BASE64uRLEncode(header)+ "." + 
BASE64uRLEncode(payload),
secret
)

el secreto tiene que estar en una parte del servidor que el cliente no conozca.


## poder devolver un jwt token steps

1. instalar nueva libreria 

``` python
pip install "python-jose[crytopgraphy]
```

1. instalar nueva libreria 

``` python
pip install "python-jose[crytopgraphy]
```

2. generar un secret key randow

``` bash
openssl rand -hex 32
````



## unit testing

Son pruebas unitarias de una solo compoente del software.
en python se puede usar pytest.

- Popular en python
- Simple y Flexible



## integration testing.

Es para probar la interaccion entre distitnas partes o componentes de una aplicaciones. 



STEPS:

1 . crear nueva carpetas que se llama test/

2. crear file text_example.py

3. pytest corre todos los archivos que tengas test en su nombre debajo de la carepta test.

4. 
