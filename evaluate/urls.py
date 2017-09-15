from django.conf.urls import url, include
from django.contrib import admin
from evaluator.views import AnswerView, HomeView

urlpatterns = [
	url(r'^$', HomeView.as_view()),
    url(r'^test/', AnswerView.as_view()),
    url(r'^evaluator/', include('evaluator.urls')),
    url(r'^admin/', admin.site.urls),
]
