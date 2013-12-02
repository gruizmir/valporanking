from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255L, blank=False, unique=True)
    smw_id = models.IntegerField(null=True, blank=True)
    facebook_count = models.IntegerField(default=0)
    twitter_count = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)
    facebook_rate = models.FloatField(default=0.0)
    twitter_rate = models.FloatField(default=0.0)

    class Meta:
        db_table = 'article'
    
    def __unicode__(self):
        return self.name
