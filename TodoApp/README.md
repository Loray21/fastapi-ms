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