from django.db import models

# Create your models here.


class recentViews(models.Model):
	url = models.URLField(unique=True)

	def __str__(self):
		return self.url
	