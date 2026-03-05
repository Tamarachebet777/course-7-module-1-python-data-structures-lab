# This module contains functions for filtering student data.
# lib/filters.py
# lib/data_processing.py
# lib/data_generator.py
def filter_students_by_major(students, major):
    """
    Filter students by major using list comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: Major to filter by
    
    Returns:
        List of students with the specified major
    """
    return [student for student in students if student[2] == major]


def filter_students_by_id_range(students, min_id, max_id):
    """
    Filter students by ID range using list comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        min_id: Minimum ID (inclusive)
        max_id: Maximum ID (inclusive)
    
    Returns:
        List of students with IDs in the specified range
    """
    return [student for student in students if min_id <= student[0] <= max_id]


def filter_students_by_name_length(students, min_length):
    """
    Filter students by name length using list comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        min_length: Minimum name length
    
    Returns:
        List of students with names longer than min_length
    """
    return [student for student in students if len(student[1]) > min_length]
