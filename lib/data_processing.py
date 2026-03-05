# This module contains functions to process student data.
# lib/data_processing.py
# lib/data_generator.py
def format_student_data(student):
    """
    Format student data into a readable string.
    
    Args:
        student: Tuple containing (ID, Name, Major)
    
    Returns:
        Formatted string: "ID: {id} | Name: {name} | Major: {major}"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"


def display_students(students):
    """
    Display all students' formatted data.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    """
    for student in students:
        print(format_student_data(student))


def get_student_names(students):
    """
    Get a list of all student names using list comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        List of student names
    """
    return [student[1] for student in students]


def get_student_count_by_major(students):
    """
    Count students in each major.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Dictionary with majors as keys and counts as values
    """
    major_counts = {}
    for student in students:
        major = student[2]
        major_counts[major] = major_counts.get(major, 0) + 1
    return major_counts


def sort_students_by_name(students):
    """
    Sort students by name.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        New list of students sorted by name
    """
    return sorted(students, key=lambda student: student[1])