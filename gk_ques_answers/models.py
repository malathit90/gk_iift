from django.db import models

# Create your models here.

class question_type(models.Model):
    type_name = models.CharField('Specify Question Type',max_length = 100)
    def __unicode__(self):
        return self.type_name
    def to_string(self):
        return self.type_name
    
class questions(models.Model):
    question = models.CharField('Question',max_length = 300)
    answer = models.TextField('Answer')
    type = models.ForeignKey(question_type)
    answer_description = models.TextField('Additional Comments', blank = True, default = '')
    time_added = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s , %s" % (self.question, self.answer)
