from django.core.management.base import BaseCommand
from blog.models import Post
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with fake posts"

    def handle(self, *args, **kwargs):
        user_1 = User.objects.filter(username = 'mohamed').first()  
        user_2 = User.objects.filter(username = 'mohamedtest').first()  

        for i in range(15):
            user = random.choice([user_1, user_2])
            Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=3),
                author=user
            )

        self.stdout.write(self.style.SUCCESS("Successfully added fake posts!"))