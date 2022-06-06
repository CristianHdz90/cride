"""Profile model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CrideBaseModel


class Profile(CrideBaseModel):
    """Profile model.

    A profile holds the user's public data like biography, picture
    and statistics.
    """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    picture = models.ImageField(
        "profile picture", upload_to="users/pictures", blank=True, null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0, help_text="User's reputation based on the rides taken and offered."
    )

    def __str__(self):
        """Return users's str representation"""
        return str(self.user.username)
