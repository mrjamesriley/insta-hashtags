from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 200)
    second_name = models.CharField(max_length = 200)
    email_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.first_name + " " + self.second_name

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    category_name = models.CharField(max_length= 200)

    def __str__(self):
        return self.category_name


class Hashtag(models.Model):
    hashtag = models.CharField(max_length = 200)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.hashtag




