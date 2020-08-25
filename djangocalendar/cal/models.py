from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Event(models.Model):
    user= models.ForeignKey(User,default=None,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        url2= reverse('cal:event_delete' ,args=(self.id,) )
        
        
        return f'<a href="{url}"> {self.title} </a> <a class=" btn-info right" style="  font-size: medium; " href="{url2}" >delete</a>'

