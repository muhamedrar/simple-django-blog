from django.core.management.base import BaseCommand
from django.contrib.auth.forms import PasswordResetForm
from django.test import RequestFactory


class Command(BaseCommand):
    help = "Send password reset email for testing"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):
        email = options["email"]

        form = PasswordResetForm({"email": email})

        if form.is_valid():
            factory = RequestFactory()
            request = factory.get("/")
            request.META["SERVER_NAME"] = "127.0.0.1"
            request.META["SERVER_PORT"] = "8000"

            form.save(
                request=request,
                use_https=False,
                email_template_name="registration/password_reset_email.html",
            )

            self.stdout.write(self.style.SUCCESS("Email sent successfully"))
        else:
            self.stdout.write(self.style.ERROR("Invalid email"))