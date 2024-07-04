from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""

    DAILY = "Раз в день"
    EVERY_TWO_DAYS = "Раз в два дня"
    EVERY_THREE_DAYS = "Раз в три дня"
    EVERY_FOUR_DAYS = "Раз в четыре дня"
    EVERY_FIVE_DAYS = "Раз в пять дней"
    EVERY_SIX_DAYS = "Раз в шесть дней"
    WEEKLY = "Раз в неделю"

    PERIOD_CHOICES = (
        (DAILY, "Раз в день"),
        (EVERY_TWO_DAYS, "Раз в два дня"),
        (EVERY_THREE_DAYS, "Раз в три дня"),
        (EVERY_FOUR_DAYS, "Раз в четыре дня"),
        (EVERY_FIVE_DAYS, "Раз в пять дней"),
        (EVERY_SIX_DAYS, "Раз в шесть дней"),
        (WEEKLY, "Раз в неделю"),
    )

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
    )
    place = models.CharField(
        max_length=150,
        verbose_name="Место привычки",
    )
    time = models.TimeField(
        verbose_name="Время выполнения привычки",
    )
    action = models.TextField(
        max_length=300,
        verbose_name="Действие, которое следует выполнять",
    )
    is_pleasant = models.BooleanField(
        **NULLABLE,
        verbose_name="Признак приятной привычки",
    )
    relate_habit = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name="Связанная привычка",
        **NULLABLE
    )
    periodicity = models.CharField(
        choices=PERIOD_CHOICES,
        default=DAILY,
        verbose_name="Периодичность"
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="Награда за выполнение",
        **NULLABLE
    )
    duration = models.DurationField(
        default=None,
        verbose_name="Продолжительность выполнения (в сек)",
        **NULLABLE
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.action} - {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
