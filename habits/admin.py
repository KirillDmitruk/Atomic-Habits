from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant",
        "relate_habit",
        "periodicity",
        "reward",
        "duration",
        "is_public"
    )