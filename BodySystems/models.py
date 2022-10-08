from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class System(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    

    def __str__(self) -> str:
        return self.code




class Disease(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=False)
    sys = models.ForeignKey(System, related_name='diseases', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name






class news(models.Model):
    source=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    title=models.IntegerField()
    #description=models.ForeignKey(Department, on_delete=models.CASCADE)

    def str(self) -> str:
        return self.source







from pydoc import describe
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=False)
    description  = models.TextField(null=True)
    dept_date = models.DateTimeField(auto_now_add=True, null=True)


    def str(self) -> str:
        return self.name