from django.conf.urls import patterns, url


urlpatterns = patterns('',
        url(r'(?P<ques_type_id>(\d+))/(?P<start_id>(\d+))/(?P<end_id>(\d+))','gk_ques_answers.views.retrieve_ques', name = 'retrieve_ques'),
        url(r'categories', 'gk_ques_answers.views.fetch_ques_ans_types', name = 'ques_ans_types')
    )