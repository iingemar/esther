from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Commentator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    comment = models.CharField(max_length=500, blank=True, default=None)
    commentator = models.ForeignKey(Commentator, null=True, blank=True, default=None)

    def get_inverted_stars(self):
        return 5 - self.rating
    def get_stars(self):
        return self.rating
    def link(self, category):
        return '<a href="/kategori/%s">%s</a>' % (category.name,category.name)
    def get_categories(self):
        return (', ').join([self.link(category) for category in self.categories.all()])
    def get_recipe(self):
        return self.reciperow_set.all().order_by('id')
    def __unicode__(self):
        return self.name


class RecipeRow(models.Model):
    description = models.CharField(max_length=200)
    food = models.ForeignKey(Food)

    def __unicode__(self):
        return self.description


