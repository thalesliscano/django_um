from django.urls import path
from .views import index, contato, sair, produto


urlpatterns = [ 
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sair/', sair, name='sair'),
    path('produto/<int:id>', produto, name='produto')
]

