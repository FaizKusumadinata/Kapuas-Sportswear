from django.urls import path, include
from main.views import show_main, create_products, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, update_products, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_products/', create_products, name='create_products'),
    path('products/<str:id>/', show_products, name='show_products'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<uuid:id>/update', update_products, name='update_products'),
    path('products/<uuid:id>/delete', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:products_id>/', show_json_by_id, name='show_json_by_id'),
]
