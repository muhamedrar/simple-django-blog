from django.core.management.base import BaseCommand
from blog.models import Post
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with fake posts"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("No users found!"))
            return

        for i in range(20):
            user = random.choice(users)

            Post.objects.create(
                title=fake.sentence(nb_words=9),
                content=fake.paragraph(nb_sentences=5),
                author=user
            )

        self.stdout.write(self.style.SUCCESS("Successfully added fake posts!"))