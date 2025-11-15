from django.urls import path, include

app_name= 'core'

urlpatterns = [
  path('', include('core.urls.core_urls')),    
]