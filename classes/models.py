from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null =True)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	GENDER_CHOICES = (('Male','Male'), ( 'Female','Female'))
	GRADE_CHOICES = (

		("A", "A"),
		("B+", "B+"),
		("B", "B"),
		("B-", "B-"),
		("C+", "C+"),
		("C", "C"),
		("C-", "C-"),
		("D+", "D+"),
		("D", "D"),
		("D-", "D-"),
		("E+", "E+"),
		("E", "E"),
		("E-", "E-"),
		("F", "F"),

		)
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField(max_length=120)
	
	gender = models.CharField(max_length=120, choices = GENDER_CHOICES)
	exam_grade = models.CharField(max_length=105, choices = GRADE_CHOICES)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
