# from django.db import models

# class MainCourse(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     price = models.FloatField()

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = 'main_course'  # Specify the table name


from django.db import models

class MainCourse(models.Model):
    mainCourseId = models.AutoField(primary_key=True, db_column='mainCourseId')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_course'
        
    @staticmethod
    def get_main_course(main_course_id: int):
        try:
            main_course = MainCourse.objects.get(mainCourseId=main_course_id)
            return main_course
        except MainCourse.DoesNotExist:
            return None

    def update_main_course(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        self.save()

    def delete_main_course(self):
        self.delete()

