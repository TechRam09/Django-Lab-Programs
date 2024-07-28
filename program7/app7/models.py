from django.db import models
from django.forms import ModelForm

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_usn = models.CharField(max_length=200)
    student_sem = models.IntegerField(blank=True,null=True)
    def __str__(self) :
       return self.student_name + "(" + self.student_usn + ")"
        
        
class Project(models.Model):
    student = models.ForeignKey(Student,on_delete= models.CASCADE)
    ptopic = models.CharField(max_length=200)
    planguage = models.CharField(max_length=200)
    pduration = models.IntegerField()
    def __str__(self):
      return self.ptopic
        
class ProjectReg(ModelForm):
    required_css_class = "required"
    class Meta:
        model = Project
        fields = ['student','ptopic','planguage','pduration']