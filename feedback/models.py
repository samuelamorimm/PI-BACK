from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Feedback de {self.name} - {self.created_at}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"