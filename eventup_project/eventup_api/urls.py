from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.contact import ContactViewSet
from .views.event import EventViewSet
from .views.invitation import InvitationViewSet
from .views.activity import ActivityViewSet
from .views.activity import ParticipationViewSet
from .views.payment import PaymentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'events', EventViewSet)
router.register(r'invitations', InvitationViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'participations', ParticipationViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]