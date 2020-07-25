# from django.db import models
# from django.utils import timezone
# from aut
#
# # Create your models here.
# class BankStatement(models.Model):
#     date = models.DateField()
#     narration = models.CharField(max_length=300)
#     reference = models.IntegerField()
#     valuedate = models.DateField()
#     withdrawal = models.IntegerField()
#     deposit = models.IntegerField()
#     closing_balance = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=timezone.now)
#     document = models.FileField(upload_to='',null = True)
