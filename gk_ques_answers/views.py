# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from gk_ques_answers.models import questions

def retrieve_ques(request, question_type, start_id, end_id):
    result = questions.objects.filter(type_id = question_type).order_by('-time_added')[start_id:end_id]
    json_to_print = []
    ques_ans = {}
    for a_record in result :
        ques_ans['Q'] = a_record.question
        ques_ans['A'] = a_record.answer
        json_to_print.append(ques_ans)
        ques_ans = {}
    return HttpResponse(simplejson.dumps(json_to_print), mimetype='application/json')