from django.urls import path
from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView

app_name = 'gap'
urlpatterns = [
    path('', RoomListView.as_view(), name='rooms'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room'),
    path('like/<int:pk>/', LikeOpinionView.as_view(), name='opinion-like')
]