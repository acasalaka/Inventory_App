from django.urls import include, path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path('add-amount/<int:id>/', add_amount, name='add_amount'),
    path('substract-amount/<int:id>/', substract_amount, name='substract_amount'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]