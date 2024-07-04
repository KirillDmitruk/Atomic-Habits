from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Список всех привычек."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitPublishListAPIView(generics.ListAPIView):
    """Список публичных привычек."""

    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """Делаем текущего пользователя 'Создателем' привычки."""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение одной привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""

    queryset = Habit.objects.all()