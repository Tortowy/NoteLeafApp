from django.db import models

from django.urls import reverse
# Create your models here.


class Note(models.Model):

    PRIORITIES = (
        ('1', "Low"),
        ('2',"Medium"),
        ('3', "High"),
    )

    title = models.CharField(max_length=50,)
    content = models.TextField(max_length=500)
    category = models.CharField(max_length=30)
    creation_date = models.DateTimeField(verbose_name="creation date",auto_now_add=True)
    execution_date = models.DateTimeField()
    priority = models.CharField(max_length=1,choices=PRIORITIES,default='1')
    owner_id = models.ForeignKey("users.Account",on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:detail_note_view",kwargs={"id":self.id})
