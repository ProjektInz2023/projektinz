import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system_zamowien.settings')
django.setup()

from api.models import MainCourse

if __name__ == "__main__":
    action = input("Enter the action (create/read/update/delete): ")

    if action == "create":
        name = input("Enter the name of the main course: ")
        description = input("Enter the description: ")
        price = float(input("Enter the price: "))
        main_course = MainCourse(name=name, description=description, price=price)
        main_course.save()
        print("Main course created:", main_course)

    elif action == "read":
        main_course_id = int(input("Enter the ID of the main course: "))
        main_course = MainCourse.get_main_course(main_course_id)
        if main_course:
            print("Main course found:", main_course)
        else:
            print("Main course not found.")

    elif action == "update":
        main_course_id = int(input("Enter the ID of the main course: "))
        main_course = MainCourse.get_main_course(main_course_id)
        if main_course:
            name = input("Enter the updated name (leave empty to keep the same): ")
            description = input("Enter the updated description (leave empty to keep the same): ")
            price = float(input("Enter the updated price (leave empty to keep the same): "))
            main_course.update_main_course(name, description, price)
            print("Main course updated:", main_course)
        else:
            print("Main course not found.")

    elif action == "delete":
        main_course_id = int(input("Enter the ID of the main course: "))
        main_course = MainCourse.get_main_course(main_course_id)
        if main_course:
            main_course.delete_main_course()
            print("Main course deleted.")
        else:
            print("Main course not found.")

    else:
        print("Invalid action.")