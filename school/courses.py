def search_courses_by_name(courses_data: list[dict[str, str]], keyword: str) -> list[dict[str, str]]:
    """
    Searches courses by name containing the given keyword.
    Args:
        courses_data (list): A list of dictionaries containing course details.
        keyword (str): The keyword to search in course names.
    Returns:
        list: A list of dictionaries containing courses whose names contain the keyword.
    """
    result_courses = []
    for course in courses_data:
        if keyword.lower() in course["course_name"].lower():
            result_courses.append(course)
    return result_courses

def filter_courses_by_duration(courses_data: list[dict[str, str]], min_duration: int, max_duration: int) -> list[dict[str, str]]:
    """
    Filters courses by duration between min_duration and max_duration.
    Args:
        courses_data (list): A list of dictionaries containing course details.
        min_duration (int): Minimum duration in hours.
        max_duration (int): Maximum duration in hours.
    Returns:
        list: A list of dictionaries containing courses whose duration is between min_duration and max_duration.
    """
    filtered_courses = []
    for course in courses_data:
        try:
            course_duration = int(course["duration"])  # Convert duration to integer
            if min_duration <= course_duration <= max_duration:
                filtered_courses.append(course)
        except ValueError:
            print(f"Invalid duration value for course: {course.get('course_name', 'Unknown Course')}")
    return filtered_courses

def filter_courses_by_price(courses_data: list[dict[str, str]], min_price: float, max_price: float) -> list[dict[str, str]]:
    """
    Filters courses by price between min_price and max_price.
    Args:
        courses_data (list): A list of dictionaries containing course details.
        min_price (float): Minimum price.
        max_price (float): Maximum price.
    Returns:
        list: A list of dictionaries containing courses whose price is between min_price and max_price.
    """
    result = []
    for course in courses_data:
        try:
            course_price = float(course["price"])  # Ensure price is treated as a float
            if min_price <= course_price <= max_price:
                result.append(course)
        except ValueError:
            print(f"Invalid price value for course: {course.get('course_name', 'Unknown Course')}")
    return result

def view_courses(courses_data: list[dict[str, str]]) -> None:
    """
    Displays a list of available courses with details.
    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', 'duration', and 'price'.
    """
    if not courses_data:
        print("No courses available at the moment.")
    else:
        print("\nAvailable Courses:")
        for index, course in enumerate(courses_data, start=1):
            print(
                f"{index}. {course['course_name']} - Instructor: {course['instructor']}, "
                f"Duration: {course['duration']} hours, Price: ${course['price']}"
            )