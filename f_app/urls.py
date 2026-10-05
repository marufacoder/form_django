from django.urls import path
from f_app.views import *

urlpatterns = [
    path('', welcome_view, name='welcome_view'),
    path('blog/', blog_list, name='blog_list'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:id>/', update_blog, name='update_blog'),
    
]
