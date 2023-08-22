from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.view_all_location, name="location_list"),
    path('tag/<int:tag_id>/', views.filter_by_tag, name="tag"),
    path('details/<int:pk>/', views.location_details_view, name='location_details'),
    path('create/', views.submit_location, name="submit_location"),
    path('create_feature/<int:s_id>/', views.create_feature, name="create_feature"),
    path('dynamic_feature/<int:s_id>/', views.dynamic_feature, name='dynamic_feature'),
    path('create_season/<int:l_id>/', views.season, name="create_season"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
