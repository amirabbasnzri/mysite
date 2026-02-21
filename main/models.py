from django.db import models


# Portfolio model
class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=150)
    profile_image = models.ImageField(upload_to='main/media/portfolio')
    resume_link = models.URLField()
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name_plural = "Portfolio"
        
    def __str__(self):
        return self.name
    
# Categories model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Projects model
class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="projects")
    image = models.ImageField(upload_to="main/media/projects/")
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.created_at.date()}'


# AboutMe model
class AboutMe(models.Model):
    bio = models.TextField(max_length=200)
    profile = models.ImageField(upload_to='main/media/about_me')
    frameworks = models.CharField(max_length=80)
    education = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "AboutMe"
        
    def __str__(self):
        return self.job
    
    
# messages
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'