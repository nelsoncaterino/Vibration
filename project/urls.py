from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),

]

handler404 = "app.views.custom_404"
