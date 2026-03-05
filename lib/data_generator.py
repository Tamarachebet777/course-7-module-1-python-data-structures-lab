# This module contains functions to lazily generate student data.
# lib/data_generator.py
def student_generator(students, major=None):
    """
    Return a generator expression for all students, optionally filtered by major.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: Optional major to filter by
    
    Returns:
        Generator expression yielding student tuples
    """
    if major:
        return (student for student in students if student[2] == major)
    else:
        return (student for student in students)


def student_names_generator(students, major=None):
    """
    Return a generator expression for student names, optionally filtered by major.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: Optional major to filter by
    
    Returns:
        Generator expression yielding student names
    """
    if major:
        return (student[1] for student in students if student[2] == major)
    else:
        return (student[1] for student in students)


def student_id_generator(students, major=None):
    """
    Return a generator expression for student IDs, optionally filtered by major.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: Optional major to filter by
    
    Returns:
        Generator expression yielding student IDs
    """
    if major:
        return (student[0] for student in students if student[2] == major)
    else:
        return (student[0] for student in students)


def process_large_dataset(students, chunk_size=100):
    """
    Process a large dataset in chunks using generator expressions.
    
    Args:
        students: List of student tuples
        chunk_size: Size of each chunk
    
    Returns:
        Generator yielding chunks of students
    """
    for i in range(0, len(students), chunk_size):
        yield students[i:i + chunk_size]


def get_student_info_generator(students):
    """
    Return a generator yielding formatted student information.
    
    Args:
        students: List of student tuples
    
    Returns:
        Generator yielding formatted strings for each student
    """
    from data_processing import format_student_data
    return (format_student_data(student) for student in students)
