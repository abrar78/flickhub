from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='SignUpView'),
    path('user/',views.city,name = 'city'),
    path('hyderabad/',views.hyd,name = 'hyd'),
    path('delhi/',views.delhi,name = 'delhi'),
    path('banglore/',views.bang,name = 'bang'),
    path('toystory4/',views.toystory,name = 'toystory'),
    path('toystory4_tickets/',views.toystory_tickets,name = 'toystory_tickets'),
    path('oh!_baby/',views.ohbaby,name = 'ohbaby'),
    path('oh!_baby_tickets/',views.ohbaby_tickets,name = 'ohbaby_tickets'),
    path('Annabelle/',views.anna,name = 'anna'),
    path('Annabelle_tickets/',views.anna_tickets,name = 'anna_tickets'),
    path('Article_15/',views.a15,name = 'a15'),
    path('Article_15_tickets/',views.a15_tickets,name = 'a15_tickets'),
    path('Brochevarevarura/',views.bro,name = 'bro'),
    path('Brochevarevarura_tickets/',views.bro_tickets,name = 'bro_tickets'),
    path('Kabir_Singh/',views.kabir,name = 'kabir'),
    path('Kabir_Singh_tickets/',views.kabir_tickets,name = 'kabir_tickets'),  
    path('seats/',views.seats,name = 'seats'),
    path('seats1/',views.seats1,name = 'seats1'),
    path('seats2/',views.seats2,name = 'seats2'),
    path('search/',views.search,name = 'search'),
    path('tickit/',views.tickit,name = 'tickit'),
    path('E-ticket/',views.ticket,name = 'ticket'),
    
]