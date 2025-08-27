from django.db import models

# Create your models here.
class Details(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	mobilenumber=models.CharField(max_length=15,default="",null=False)
	emailid=models.CharField(max_length=50,default="",null=False)
	password=models.CharField(max_length=120,default="",null=False)

class Notes(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	subject=models.CharField(max_length=100,default="",null=False)
	

class Details1(models.Model):
	fullname=models.CharField(max_length=100,default="",null=False)
	mobilenumber=models.CharField(max_length=15,default="",null=False)
	emailid=models.CharField(max_length=50,default="",null=False)
	password=models.CharField(max_length=120,default="",null=False)

class Files(models.Model):
    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='store/pdfs/')
    cover = models.ImageField(upload_to='store/covers/', null=True, blank=True)

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


class Pelcon(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='store/pdfs/')
    


    def __str__(self):
        return self.name
	
	
	



