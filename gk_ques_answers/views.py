# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from gk_ques_answers.models import questions
import json

def retrieve_ques(request, question_type, start_id, end_id):
    result = questions.objects.filter(type_id = question_type).order_by('-time_added')[start_id:end_id]
    json_to_print = []
    ques_ans = {}
    for a_record in result :
        ques_ans['Q'] = a_record.question
        ques_ans['A'] = a_record.answer
        json_to_print.append(ques_ans)
    return render_to_response('questions.html',{'final_result_in_json': json.dumps(json_to_print)}, context_instance = RequestContext(request))