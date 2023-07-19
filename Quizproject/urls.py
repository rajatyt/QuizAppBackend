
from django.contrib import admin
from django.urls import path,include
from quiz import views
from rest_framework.routers import DefaultRouter


app_name='quiz'
# router=DefaultRouter()
# router.register('Quiz',views.Quiz,basename="Quiz")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls))
    path('q/',views.Quiz.as_view(),name='quiz'),
    # path('r/',views.Quiz.as_view(),name='quiz'),
    path('r/<str:topic>/',views.RandomQuiz.as_view(),name='random'),
    path('q/<str:topic>/',views.QuestionQuiz.as_view(),name='questions'),
]
