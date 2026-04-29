from django.core.management.base import BaseCommand
from django.contrib.auth.forms import PasswordResetForm


class Command(BaseCommand):
    help = "Send password reset email for testing"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="Email to send reset link to")

    def handle(self, *args, **options):
        email = options["email"]

        form = PasswordResetForm({"email": email})

        if form.is_valid():
            form.save(
                use_https=False,
                from_email=None,
                request=None,  # OK for console backend, but better via real request in production
                email_template_name="registration/password_reset_email.html",
            )

            self.stdout.write(self.style.SUCCESS(f"Reset email sent to {email}"))
        else:
            self.stdout.write(self.style.ERROR("Invalid email"))