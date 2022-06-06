"""User model."""

# Django
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

# Utilities
from cride.utils.models import CrideBaseModel


class User(CrideBaseModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={"unique": "A user with that email already exists."},
    )
    _phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="The phone number must be entered in the format +999999999. Up to 15 digits allowed",
    )
    phone_number = models.CharField(
        max_length=17, blank=True, validators=[_phone_regex]
    )
    is_client = models.BooleanField(
        "Client",
        default=True,
        help_text=(
            "Help easily distinguish users and perform queries. "
            "Clients are the main type of user."
        ),
    )
    is_verified = models.BooleanField(
        "Email verification",
        default="False",
        help_text="Set to True when the user has verified it's email address.",
    )

    USERNAME_FIELD = "email"
    # For createsuperuser command
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
