Proyecto hecho por :
Molinari Matias y Nebot Mariano .
Ambos hicimos la gran parte de la App juntos al mismo tiempo(tanto en codigo como diseño) donde cada vez que habia una dificultad se planteaba el problema  y  entre las dos lograbamos resolverlo , lo que se puede decir es que Mariano es  quien inserto el nuevo diseño que tiene  la APP como su estetica en cuanto a la vista del usuario.
-------------------------------------------------------------------
Para esta App Web se usaron las versiones de python  3.10.2y Django version 4.0.3
-------------------------------------------------------------------

La app tiene la finalidad del registro y busqueda de personas relacionadas con las vistas Familiar, Amigos y AmigosCoder


-------------------------------------------------------------------

-------------------------------------------------------------------

Tutorial de como acceder y utilizarla:
Tenemos 2 maneras de usarla .
1.Como usuario.
2.Como administrador.
1.En el primer caso como usuario abrimos la apliacion con el comando python manage.py runserver luego entro de ella debemos registrarnos para poder utilizarla, vamos arriba en la URL(direccion) ponemos /register , luego llenamos los campos como querramos y nos rediccionara al login .
Ya dentro de la App con nuestro usuario creado podemos acceder a cualquiera de las siguientes vistas donde podemos registrar ya sea un familiar , un AmigoCoder o un amigo , luego podemos buscarlo mediante su apellido y nos saldran todos los datos.
2. Para el segundo caso, para acceder como administrador necesitamos crearlo, así que vamos a la consola y colocamos python manage.py createsuperuser.
Más tarde en la aplicación, regresamos a la URL y ponemos /admin para que podamos ingresar a la parte de la base de datos y ver todo el registro de usuarios.
Así podremos modificarlos como queramos.