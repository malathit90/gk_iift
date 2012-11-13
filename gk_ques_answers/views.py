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
        ques_ans['D'] = a_record.answer_description
        ques_ans_list.append(ques_ans)
        ques_ans = {} 
    return ques_ans_list    

def retrieve_ques(request, ques_type_id, start_id, end_id):
    print "inside retrieve"
    ques_ans_list = fetch_ques_ans(ques_type_id, start_id, end_id)
    json_to_print = {}
    ques_type_obj = question_type.objects.get(pk = ques_type_id)
    ques_type = ques_type_obj.to_string()
    json_to_print['types'] = [ques_type]
    json_to_print[ques_type] = ques_ans_list
    return HttpResponse(simplejson.dumps(json_to_print), mimetype='application/json')

def initial_fetch(request):
    ques_types = question_type.objects.distinct()
    all_questions = {}
    all_questions["types"] = []
    for each_type in ques_types:
        all_questions[each_type.type_name] = fetch_ques_ans(each_type.id, 0, 15)
        all_questions["types"].append(each_type.to_string())
    return HttpResponse(simplejson.dumps(all_questions), mimetype='application/json')