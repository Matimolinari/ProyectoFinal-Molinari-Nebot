Proyect realized by:

Molinari Matias & Nebot Mariano.


We both did a large part of the App together at the same time (both in code and design) where every time there was a difficulty the problem was raised and managed to be solved between the two of us, what can be said is that Mariano is the one who inserted the new design that the App has as well as its aesthetics in terms of the user's view.


-------------------------------------------------------------------


For this App Web we use the version of python 3.10.2 and Django 4.0.3


-------------------------------------------------------------------



The App have the finally of register and search for person related with the views Familiar, Amigos and AmigosCoder.


-------------------------------------------------------------------


Tutorial on how to access and use it
We have 2 ways to use it:
1. Like User
2. Like Admin
1. In the first case we need to have open the App with the command python manage.py runserver, once inside we must register  to be able to use it, go to the URL and put /register , then we fill the fields as we want to and we will be redirected to the login.
Once in the App with our User created  we can access any of the following views where we can register a "familiar", "AmigoCoder" or Friend , then you can search them by their last name and see all of their data.
2.For the second case to access as an admin we need to create, so go to the console and put python manage.py createsuperuser.
Later in the app go back to the URL and put /admin so we can enter the database part and see all of the user register.
This way we can modify them as we want.