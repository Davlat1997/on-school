from school import students
from school import courses

def main():
    # Talabalar bazasi va kurslar bazasi
    students_data = []  # Talabalar ma'lumotlari
    courses_data = [
        {"name": "Python Basics", "duration": "8 hafta", "instructor": "John Doe"},
        {"name": "Data Science 101", "duration": "10 hafta", "instructor": "Jane Smith"},
    ]

    print("=== Welcome to On-School ===")

    while True:
        # Asosiy menyuni chiqarish
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choose_commond = int(input("Select an option: "))

        # Foydalanuvchi ro‘yxatdan o‘tishni tanlasa
        if choose_commond == 1:
            student = {}
            # Yangi talabaning ma'lumotlarini ro‘yxatdan o‘tkazish
            new_student = students.register_student(student, students_data)

            # Yangi talaba bazaga qo‘shiladi
            students_data.append(new_student)

        # Foydalanuvchi tizimga kirishni tanlasa
        elif choose_commond == 2:
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            # Talabaning tizimga kirishini tekshirish
            user = students.login_student(email, password, students_data)

            # Agar login muvaffaqiyatli bo‘lsa
            if user:
                print(f"\nWelcome, {user['name']}!")

                # Talabaning menyusi
                while True:
                    print("\n--- Main Menu ---")
                    print("1. View Available Courses")
                    print("2. Enroll in a Course")
                    print("3. View My Courses")
                    print("4. Logout")
                    choose_commond_user = int(input("Choose an option: "))

                    if choose_commond_user == 1:
                        # Mavjud kurslarni ko‘rsatish
                        courses.view_courses(courses_data)

                    elif choose_commond_user == 2:
                        # Kursga yozilish
                        course_name = students.enroll_in_course(
                            courses_data, students_data, user["pas_log"]["log"]
                        )
                        if course_name:
                            user["course"].append(course_name)

                    elif choose_commond_user == 3:
                        # Talabaning kurslarini ko‘rsatish
                        courses.view_courses(user["course"])

                    elif choose_commond_user == 4:
                        # Tizimdan chiqish
                        print("\nGoodbye!")
                        break

                    else:
                        print(
                            "\nSiz mavjud bo‘lmagan buyruq kiritdingiz, iltimos tekshirib qaytadan urinib ko‘ring!\n"
                        )

        # Foydalanuvchi chiqishni tanlasa
        elif choose_commond == 3:
            print("Darslarni qoldirishni hayolinga ham keltirma!!!", "Ishlaringga omad!", sep="\n")
            break

        else:
            print("\nMavjud bo‘lmagan buyruq kiritdingiz, iltimos tekshirib qaytadan urinib ko‘ring!\n")