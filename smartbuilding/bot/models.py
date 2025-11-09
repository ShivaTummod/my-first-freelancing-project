from django.db import models
from django.contrib.auth.hashers import make_password


class Signup(models.Model):
	ROLE_SECURITY = 'security'
	ROLE_SECRETARY = 'secretary'
	ROLE_FLAT_OWNER = 'flat_owner'

	ROLE_CHOICES = [
		(ROLE_SECURITY, 'Security'),
		(ROLE_SECRETARY, 'Secretary'),
		(ROLE_FLAT_OWNER, 'Flat Owner'),
	]

	role = models.CharField(max_length=20, choices=ROLE_CHOICES)
	full_name = models.CharField(max_length=150)
	contact_number = models.CharField(max_length=15)
	aadhar_number = models.CharField(max_length=20)
	dob = models.DateField()
	password = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)
	profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

	def save(self, *args, **kwargs):
		# Hash the password if it isn't already hashed
		if self.password and not self.password.startswith('pbkdf2_') and not self.password.startswith('argon2'):
			self.password = make_password(self.password)
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.full_name} ({self.get_role_display()})"
