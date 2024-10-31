from django.db import models
from brands.models import Brand


type_of_instructors = (('personal_trainer','personal_trainer'),('sports_coach','sports_coach'),('yoga_instructor','yoga_instructor'),('dance_instructor','dance_instructor'),('fitness_instructor','fitness_instructor'),('nutritionist','nutritionist'),('physiotherapist','physiotherapist'),('psychologist','psychologist'),('counsellor','counsellor'),('life_coach','life_coach'),('career_coach','career_coach'),('business_coach','business_coach'),('academic_coach','academic_coach'),('music_instructor','music_instructor'),('art_instructor','art_instructor'),('craft_instructor','craft_instructor'),('language_instructor','language_instructor'),('other','other'))

type_of_companies = (('gym','gym'),('fitness_center','fitness_center'),('yoga_center','yoga_center'),('dance_center','dance_center'),('nutrition_center','nutrition_center'),('physiotherapy_center','physiotherapy_center'),('psychology_center','psychology_center'),('counselling_center','counselling_center'),('life_coaching_center','life_coaching_center'),('career_coaching_center','career_coaching_center'),('business_coaching_center','business_coaching_center'),('academic_coaching_center','academic_coaching_center'),('music_center','music_center'),('art_center','art_center'),('craft_center','craft_center'),('language_center','language_center'),('other','other'))

number_of_teammates = (('1-10','1-10'),('11-50','11-50'),('51-100','51-100'),('101-500','101-500'),('501-1000','501-1000'),('1000+','1000+'))

number_of_clients = (('1-10','1-10'),('11-50','11-50'),('51-100','51-100'),('101-500','101-500'),('501-1000','501-1000'),('1000+','1000+'))


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='companies', blank=True, null=True)
    type_of_company = models.CharField(max_length=100, choices=type_of_companies, blank=True, null=True)
    number_of_teammates = models.CharField(max_length=100, choices=number_of_teammates, blank=True, null=True)
    number_of_clients = models.CharField(max_length=100, choices=number_of_clients, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # logo = models.ImageField(upload_to='companies/logos/', blank=True, null=True)
    # cover_image = models.ImageField(upload_to='companies/cover_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    

