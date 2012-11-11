from django.conf.urls import patterns, url


urlpatterns = patterns('',
        url(r'(?P<question_type>(\d+))/(?P<start_id>(\d+))/(?P<end_id>(\d+))','gk_ques_answers.views.retrieve_ques', name = 'retrieve_ques'),
    )