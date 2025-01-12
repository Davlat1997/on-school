def check_grades(grades_data: dict[str, dict[str, str]], student_email: str) -> None:
    """
    Displays the grades for a student if available. If no grades are available for 
    the student, it shows a message indicating so.
    Args:
        grades_data (dict): A dictionary where student emails are keys, and their grades 
                             for each course are stored as values.
        student_email (str): The email of the student whose grades are being checked.
    """
    print("\nMy Grades:")
    enrolled_courses = grades_data.get(student_email, {})
    
    if not enrolled_courses:
        print("No grades available. You are either not enrolled in any courses or grades are not yet assigned.")
    else:
        for course, grade in enrolled_courses.items():
            print(f"{course}: {grade}")