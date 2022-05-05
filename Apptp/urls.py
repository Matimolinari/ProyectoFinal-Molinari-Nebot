
from django.urls import path
from Apptp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),  # esta era nuestra primer view
    path('buscarfamiliar/', views.buscarFamiliar),
    path('familiar', views.familiar, name="Familiar"),
    path('leerFamiliar', views.leerFamiliar, name="leerFamiliar"),
    path('eliminarFamiliar/<familiar_nombre>/',
         views.eliminarFamiliar, name="EliminarFamiliar"),
    path('editarFamiliar/<familiar_nombre>/',
         views.editarFamiliar, name="EditarFamiliar"),
    path('familiar/list', views.FamiliarList.as_view(), name='ListFamiliar'),
    path(r'^detallefamiliar(?P<pk>\d+)$',
         views.FamiliarDetalle.as_view(), name='DetailFamiliar'),
    path(r'^nuevofamiliar$', views.FamiliarCreacion.as_view(), name='NewFamiliar'),
    path(r'^editarfamiliar/(?P<pk>\d+)$',
         views.FamiliarUpdate.as_view(), name='EditFamiliar'),
    path(r'^borrarfamiliar/(?P<pk>\d+)$',
         views.FamiliarDelete.as_view(), name='DeleteFamiliar'),

    path('amigoscoder', views.amigoscoder, name="AmigosCoder"),
    path('buscaramigoscoder/', views.buscarAmigosCoder),
    path('leeramigoscoder', views.leeramigoscoder, name="leeramigoscoder"),
    path('eliminaramigoscoder/<amigoscoder_nombre>/',
         views.eliminaramigoscoder, name="Eliminaramigoscoder"),
    path('editaramigoscoder/<amigoscoder_nombre>/',
         views.editaramigoscoder, name="Editaramigoscoder"),
    path('amigoscoder/list', views.AmigosCoderList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.AmigosCoderDetalle.as_view(),
         name='Detailamigoscoder'),
    path(r'^nuevo$', views.AmigosCoderCreacion.as_view(), name='Newamigoscoder'),
    path(r'^editar/(?P<pk>\d+)$',
         views.AmigosCoderUpdate.as_view(), name='Editamigoscoder'),
    path(r'^borrar/(?P<pk>\d+)$', views.AmigosCoderDelete.as_view(),
         name='Deleteamigoscoder'),

    path('amigos', views.amigos, name="Amigos"),
    path('buscaramigos/', views.buscarAmigos),
    path('leeramigos', views.leeramigos, name="leeramigos"),
    path('elimaramigos/<amigos_nombre>/',
         views.eliminaramigos, name="EliminarAmigos"),
    path('editaramigos/<amigos_nombre>/',
         views.editaramigos, name="EditarAmigos"),
    path('amigos/list', views.AmigosList.as_view(), name='ListAmigos'),
    path(r'^amigosdetalles(?P<pk>\d+)$',
         views.AmigosDetalle.as_view(), name='DetailAmigos'),
    path(r'^nuevoamigos$', views.AmigosCreacion.as_view(), name='NewAmigos'),
    path(r'^editaramigos/(?P<pk>\d+)$',
         views.AmigosUpdate.as_view(), name='EditAmigos'),
    path(r'^borraramigos/(?P<pk>\d+)$',
         views.AmigosDelete.as_view(), name='DeleteAmigos'),


    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(
        template_name='Apptp/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('pages/', views.listbd, name="listbd"),

    path('padre', views.padre, name="padre"),



]
