# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from gk_ques_answers.models import questions, question_type

def fetch_ques_ans_types(request): 
    ques_types_obj = question_type.objects.all()
    ques_types = {}
    for a_ques_type_obj in ques_types_obj:
        ques_types[a_ques_type_obj.to_string()] = a_ques_type_obj.id
    return HttpResponse(simplejson.dumps(ques_types), mimetype='application/json')

def retrieve_ques(request, ques_type_id, start_id, end_id):
    result = questions.objects.filter(type_id = ques_type_id).order_by('-time_added')[start_id:end_id]
    ques_ans_list = []
    ques_ans = {}
    for a_record in result :
        ques_ans['Q'] = a_record.question
        ques_ans['A'] = a_record.answer
        ques_ans['D'] = a_record.answer_description
        ques_ans_list.append(ques_ans)
        ques_ans = {} 
    return HttpResponse(simplejson.dumps(ques_ans_list), mimetype='application/json')
