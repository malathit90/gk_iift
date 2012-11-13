# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from gk_ques_answers.models import questions, question_type

def fetch_ques_ans(question_type, start_id, end_id): 
    result = questions.objects.filter(type_id = question_type).order_by('-time_added')[start_id:end_id]
    ques_ans_list = []
    ques_ans = {}
    for a_record in result :
        ques_ans['Q'] = a_record.question
        ques_ans['A'] = a_record.answer
        ques_ans['T'] = a_record.type.type_name
        ques_ans['D'] = a_record.answer_description
        ques_ans_list.append(ques_ans)
        ques_ans = {} 
    return ques_ans_list    

def retrieve_ques(request, question_type, start_id, end_id):
    json_to_print = fetch_ques_ans(question_type, start_id, end_id)
    print json_to_print
    return HttpResponse(simplejson.dumps(json_to_print), mimetype='application/json')

def initial_fetch(request):
    question_types = question_type.objects.distinct();
    all_questions = {}
    for each_type in question_types:
        all_questions[each_type.type_name] = fetch_ques_ans(each_type.id, 0, 15);
    return HttpResponse(simplejson.dumps(all_questions), mimetype='application/json')