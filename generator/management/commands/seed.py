from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from categories.models import Category, Hashtag

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Preparing seed data...")
        if not User.objects.filter(username="instaman").exists():
            instaman = User.objects.create_user("instaman", password="password")
            instaman.save()
            self.stdout.write("Creating instaman user...")
        else:
            self.stdout.write("Username instaman already exists, skipping to seed data...")

        if not Category.objects.filter(category_name="Food").exists():
            food_category = Category(user_id=User.objects.get(username="instaman"), category_name="Food")
            food_category.save()
        food_hashtags = ["Keto", "Low Fat", "Healthy", "Power", "Munchies"]
        for hashtag_item in food_hashtags:
            if not Hashtag.objects.filter(category_id=Category.objects.get(category_name="Food"), hashtag=hashtag_item).exists():
                hashtag_create = Hashtag(category_id=Category.objects.get(category_name="Food"), hashtag=hashtag_item)
                hashtag_create.save()
                self.stdout.write("Creating " + hashtag_item + " hashtag" )

        if not Category.objects.filter(category_name="Gym").exists():
            gym_category = Category(user_id=User.objects.get(username="instaman"), category_name="Gym")
            gym_category.save()
        gym_hashtags = ["Workout", "Fitness", "Health", "Strong", "Muscles"]
        for hashtag_item in gym_hashtags:
            if not Hashtag.objects.filter(category_id=Category.objects.get(category_name="Gym"),hashtag=hashtag_item).exists():
                hashtag_create = Hashtag(category_id=Category.objects.get(category_name="Gym"), hashtag=hashtag_item)
                hashtag_create.save()
                self.stdout.write("Creating " + hashtag_item + " hashtag")

        if not Category.objects.filter(category_name="Living").exists():
            living_category = Category(user_id=User.objects.get(username="instaman"), category_name="Living")
            living_category.save()
        living_hashtags = ["Life", "Live Long", "Run", "Strong", "Mind"]
        for hashtag_item in living_hashtags:
            if not Hashtag.objects.filter(category_id=Category.objects.get(category_name="Living"),hashtag=hashtag_item).exists():
                hashtag_create = Hashtag(category_id=Category.objects.get(category_name="Living"), hashtag=hashtag_item)
                hashtag_create.save()
                self.stdout.write("Creating " + hashtag_item + " hashtag")

        self.stdout.write("All data seeded...")