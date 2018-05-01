from django.db import models

# Create your models here.
class IncomeTract(models.Model):
	tract_id = models.IntegerField(primary_key=True)#many to many field
	income = models.IntegerField(blank=True)#blank=true means that field can be blank, water areas are blank

	#string method, determines how django will reference this object in the admin
	def __str__(self):
	 	return str(self.tract_id)

class SiteLocation(models.Model):
	epa_id = models.IntegerField(primary_key=True)
	tract = models.ForeignKey(IncomeTract, on_delete=models.CASCADE)#foreign key
	formatted_address = models.TextField(max_length=155, blank=True)
	city = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=2, blank=True)
	zipcode = models.IntegerField(blank=True)
	npl_status = models.TextField(max_length=255, blank=True)#char and text fields must have max length
	lon = models.DecimalField(max_digits=9, decimal_places=6, default=0)
	lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)
	address = models.TextField(max_length=155, blank=True)
	income = models.IntegerField(blank=False)
	#string method, determines how django will reference this object in the admin
	#otherwise will be called SiteLocation Object
	def __str__(self):
		return str(self.epa_id)
