from django.db import models


class CrideBaseModel(models.Model):
    """Comparte Ride base model.
    CRideBaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        verbose_name="created at",
        auto_now_add=True,
        help_text="Date time on which the objects was created.",
    )
    modified = models.DateTimeField(
        verbose_name="modified at",
        auto_now=True,
        help_text="Date time on which the objects was last modified.",
    )

    class Meta:
        abstract = True
        get_latest_by = "created"
        ordering = ["-created"]


# class Person(CrideBaseModel):
#     username = models.CharField("username", max_length=100)
#     last_name = models.CharField("last name", max_length=100)

#     class Meta(CrideBaseModel.Meta):
#         ordering = ["username"]

# class PersonProxy(Person):
#     class Meta:
#         """
#         Here it's not necessary to inherit from the Person.Meta class
#         """
#         proxy=True

#     def say_hi(self):
#         return "Hi!"
