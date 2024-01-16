from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), 
]

admin.site.index_title = "The Agency"
admin.site.site_header = "The Agency Admin"
admin.site.site_title = "Site Government Agency"

