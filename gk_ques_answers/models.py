from django.db import models

# Create your models here.

class question_type(models.Model):
    type_name = models.CharField('Question Type',max_length = 100)
    
class questions(models.Model):
    question = models.CharField('Question',max_length = 300)
    answer = models.TextField('answer')
    type = models.ForeignKey(question_type, default = '', blank = True)
    answer_description = models.TextField('Additional Comments', blaank = True, default = '')
    
    def __unicode__(self):
        return "%s , %s" % (self.question, self.answer)
