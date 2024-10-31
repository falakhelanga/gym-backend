from django.db import models
from companies.models import Company

modality_choices=(
                  ('Balance','Balance'),
                  ('Bodybuilding','Bodybuilding'),
                  ('Cardio','Cardio'),
                  ('Endurance','Endurance'),
                  ('Flexibility','Flexibility'),
                  ('Functional','Functional'),
                  ('High Intensity','High Intensity'),
                  ('Hypertrophy','Hypertrophy'),
                  ('Mobility','Mobility'),
                  ('Power','Power'),
                  ('Plyometrics','Plyometrics'),
                  ('Strength','Strength'),
                  ('Speed','Speed'),
                  ('Stability','Stability'),
                  ('Weight Loss','Weight Loss'),
                  ('Weight Gain','Weight Gain'),
                  ('Activation','Activation'),
                  ('Agility','Agility'),
                  ('Other','Other')
                  
                  
                  )


muscle_groups = (
                 ('Abdominals','Abdominals'),
                 ('Adductors','Adductors'),
                 ('Biceps','Biceps'),
                 ('Calves','Calves'),
                 ('Chest','Chest'),
                 ('Forearms','Forearms'),
                 ('Glutes','Glutes'),
                 ('Hamstrings','Hamstrings'),
                 ('Lats','Lats'),
                 ('Lower Back','Lower Back'),
                 ('Middle Back','Middle Back'),
                 ('Neck','Neck'),
                 ('Quadriceps','Quadriceps'),
                 ('Shoulders','Shoulders'),
                 ('Traps','Traps'),
                 ('Triceps','Triceps'),
                 ('Other','Other')
                 
                 )
movement_patterns=(
                   ('Horizontal Push','Horizontal Push'),
                   ('Horizontal Pull','Horizontal Pull'),
                   ('Vertical Push','Vertical Push'),
                   ('Vertical Pull','Vertical Pull'),
                   ('Squat','Squat'),
                   ('Hinge','Hinge'),
                   ('Lunge','Lunge'),
                   ('Twist','Twist'),
                   ('Gait','Gait'),
                   ('Push','Push'),
                   ('Pull','Pull'),
                   ('Carry','Carry'),
                   ('Other','Other')
                   
                   )

excercise_categories=(
                      ('Strength','Strength'),
                      ('Bodyweight','Bodyweight'),
                      ('Timed','Timed'),
                      ('Distance (Long)','Distance (Long)'),
                      ('Distance (Short)','Distance (Short)'),
                      )

tracking_fields=(
                    ('Reps','Reps'),
                    ('Time','Time'),
                    ('Distance','Distance'),
                    ('Weight','Weight'),
                    ('Sets','Sets'),
                    ('Rounds','Rounds'),
                    ('Calories','Calories'),
                    ('Other','Other')
                    )

equipment_choices=(
                     ('Barbell','Barbell'),
                     ('Dumbbell','Dumbbell'),
                     ('Kettlebell','Kettlebell'),
                     ('Medicine Ball','Medicine Ball'),
                     ('Resistance Bands','Resistance Bands'),
                     ('TRX','TRX'),
                     ('Bosu Ball','Bosu Ball'),
                     ('Stability Ball','Stability Ball'),
                     ('Sandbag','Sandbag'),
                     ('Sled','Sled'),
                     ('Battle Ropes','Battle Ropes'),
                     ('Plyo Box','Plyo Box'),
                     ('Foam Roller','Foam Roller'),
                     ('Yoga Mat','Yoga Mat'),
                     ('Jump Rope','Jump Rope'),
                     ('Pull Up Bar','Pull Up Bar'),
                     ('Box','Box'),
                     ('Bench','Bench'),
                     ('Rings','Rings'),
                     ('Parallettes','Parallettes'),
                     ('Tire','Tire'),
                     ('Squat Rack','Squat Rack'),
                     ('Peg Board','Peg Board'),
                     ('Climbing Rope','Climbing Rope'),
                     ('Ski Erg','Ski Erg'),
                     ('Rowing Machine','Rowing Machine'),
                     ('Air Bike','Air Bike'),
                     ('Treadmill','Treadmill'),
                     ('Elliptical','Elliptical'),
                     ('Stairmaster','Stairmaster'),
                     ('Spin Bike','Spin Bike'),
                     ('Other','Other')
                     )

class Exercise(models.Model):
    name = models.CharField(max_length=100,)
    modality = models.CharField(max_length=100, choices=modality_choices, blank=True, null=True)
    muscle_group = models.CharField(max_length=100, choices=muscle_groups, blank=True, null=True)
    user = models.ManyToManyField('users.User', related_name='exercises', blank=True)
    movement_pattern = models.CharField(max_length=100, choices=movement_patterns, blank=True, null=True)
    excercise_category = models.CharField(max_length=100, choices=excercise_categories, blank=True, null=True)
    tracking_field = models.CharField(max_length=100, choices=tracking_fields, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    video_file = models.FileField(upload_to='exercise_videos/', blank=True, null=True)
    photos = models.ImageField(upload_to='exercise_photos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    equipment = models.CharField(max_length=100, choices=equipment_choices, blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='exercises', blank=True, null=True)

    
