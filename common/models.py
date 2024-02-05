from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Profile(BaseModel):
    class DegreeChoice(models.TextChoices):
        BACHELOR = "bachelor", "Bakalavr"
        MASTER = "master", 'Master'

    full_name = models.CharField(max_length=200)
    degree = models.CharField(choices=DegreeChoice.choices, 
                              default=DegreeChoice.BACHELOR, max_length=100)
    image = models.ImageField(upload_to="profile/")
    bio = models.TextField()

    def __str__(self):
        return self.full_name


class Skill(BaseModel):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    order = models.IntegerField(default=1)
    
    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title


class About(BaseModel):
    experience = models.TextField()
    total_projects = models.IntegerField(default=0)
    total_users = models.IntegerField(default=0)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.id
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Post(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts/")
    view_counts = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
class Service(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Portfolio(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField()
    used_tools = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    completed_at = models.DateField()

    def __str__(self) -> str:
        return self.title
    
