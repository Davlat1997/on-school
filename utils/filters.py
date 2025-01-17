def filter_courses_by_duration(
    courses_data: list[dict[str, str]], min_duration: int, max_duration: int
) -> list[dict[str, str]]:
    """
    Filters courses based on their duration.

    Args:
        courses_data (list): A list of dictionaries containing course information.
        min_duration (int): The minimum duration (inclusive).
        max_duration (int): The maximum duration (inclusive).

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


def search_courses_by_name(courses_data: list[dict[str, str]], keyword: str) -> list[dict[str, str]]:
    """
    Searches for courses whose names contain a specific keyword.

    Args:
        courses_data (list): A list of dictionaries containing course information.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of dictionaries containing courses whose names contain the keyword.
    """
    result_courses = []
    
    for course in courses_data:
        if keyword.lower() in course["course_name"].lower():  # Ensure the key is correct for course name
            result_courses.append(course)
    
    return result_courses


def filter_courses_by_price(
    courses_data: list[dict[str, str]], min_price: float, max_price: float
) -> list[dict[str, str]]:
    """
    Filters courses based on their price.

    Args:
        courses_data (list): A list of dictionaries containing course information.
        min_price (float): The minimum price (inclusive).
        max_price (float): The maximum price (inclusive).

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