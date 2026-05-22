from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from .models import Recipe, Category

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        
        # Створюємо рецепт і примусово встановлюємо дату за 2023 рік 
        # (оскільки auto_now_add перезаписує дату при створенні)
        recipe_2023 = Recipe.objects.create(
            title="Recipe 2023",
            description="Desc",
            instructions="Inst",
            ingredients="Ingr",
            category=self.category
        )
        Recipe.objects.filter(id=recipe_2023.id).update(
            created_at=timezone.make_aware(datetime(2023, 5, 1))
        )
        self.recipe_2023 = Recipe.objects.get(id=recipe_2023.id)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn(self.recipe_2023, response.context['recipes'])