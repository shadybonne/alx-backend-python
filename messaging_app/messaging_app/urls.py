from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chats.views import ConversationViewSet, MessageViewSet  # adjust import if needed

# Create the router and register your viewsets
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

# Include the router URLs under the 'api/' path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]