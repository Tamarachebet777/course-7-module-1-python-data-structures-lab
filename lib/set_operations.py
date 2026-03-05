# This module contains operations related to sets.
# lib/set_operations.py
# lib/filters.py
# lib/data_processing.py
# lib/data_generator.py
def unique_majors(students):
    """
    Return a set of unique majors from the students list using set comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Set of unique majors
    """
    return {student[2] for student in students}


def unique_name_initials(students):
    """
    Return a set of unique name initials (first letter of first name).
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Set of unique initials
    """
    return {student[1][0] for student in students}


def common_majors(students1, students2):
    """
    Find majors that exist in both student lists.
    
    Args:
        students1: First list of student tuples
        students2: Second list of student tuples
    
    Returns:
        Set of majors that appear in both lists
    """
    majors1 = unique_majors(students1)
    majors2 = unique_majors(students2)
    return majors1.intersection(majors2)


def all_majors(students1, students2):
    """
    Get all unique majors from both student lists.
    
    Args:
        students1: First list of student tuples
        students2: Second list of student tuples
    
    Returns:
        Set of all majors from both lists
    """
    majors1 = unique_majors(students1)
    majors2 = unique_majors(students2)
    return majors1.union(majors2)


def unique_majors_count(students):
    """
    Count the number of unique majors.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Integer count of unique majors
    """
    return len(unique_majors(students))


def students_by_major(students):
    """
    Group students by major using dictionary and set comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Dictionary with majors as keys and sets of student names as values
    """
    return {major: {student[1] for student in students if student[2] == major} 
            for major in unique_majors(students)}
