from django.db import models


class DailyAction(models.Model):
    """Model representing an action that occurred in the store."""

    GOOD_DAY = "good_day"
    STREET_CLOSED = "street_closed"

    ACTION_CHOICES = [
        (GOOD_DAY, "Good Day"),
        (STREET_CLOSED, "Street Closed"),
    ]

    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def description(self):
        if self.action == self.GOOD_DAY:
            return "Today was a good day."
        if self.action == self.STREET_CLOSED:
            return (
                "Looks like that today is an special event the street has been closed, "
                "so you will lose 0.05% of your incomes."
            )
        return ""
