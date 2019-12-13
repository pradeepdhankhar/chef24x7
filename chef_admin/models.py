from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Chef(models.Model):
	user_id = models.IntegerField()
	name = models.CharField(max_length=200)
	returant_name = models.CharField(max_length=200)
	place = models.CharField(max_length=200)	
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	open_days = models.CharField(max_length=200)
	open_hours = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')		


class Category(models.Model):
	cat_id = models.IntegerField()	
	name = models.CharField(max_length=200)	
	img = models.CharField(max_length=200)	
	pub_date = models.DateTimeField('date published')	



class Items(models.Model):
	name = models.CharField(max_length=200)	
	img = models.CharField(max_length=200)	
	cat = models.IntegerField()	
	price = models.CharField(max_length=200)	
	pub_date = models.DateTimeField('date published')	

class Restcat(models.Model):
	rest_id = models.CharField(max_length=200)	
	cat_id = models.IntegerField()	