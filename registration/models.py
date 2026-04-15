from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField()

    city = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    category = models.CharField(max_length=100)
    participation_type = models.CharField(max_length=100)
    call_time = models.CharField(max_length=50, blank=True, null=True)

    message = models.TextField(blank=True, null=True)

    id_proof = models.FileField(upload_to='id_proofs/')

    payment_done = models.BooleanField(default=False)  # ✅ NEW FIELD

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name