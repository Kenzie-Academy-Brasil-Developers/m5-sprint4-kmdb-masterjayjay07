from django.db import models

# Create your models here.
class RecomendationReview(models.TextChoices):
    MUST_WATCH = ("MW", "Must Watch")
    SHOULD_WATCH = ("SW", "Should Watch")
    AVOID_WATCH = ("AW", "Avoid Watch")
    NO_OPINION = ("NO", "No Opinion")


class Review(models.Model):
    stars = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=RecomendationReview.choices, default=RecomendationReview.NO_OPINION)

    critic = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="critic", null=True)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movie", null=True)



