from lib.set_operations import unique_majors
from testing import students, secondary_students

def test_unique_majors():
    majors = unique_majors(students)
    assert "Computer Science" in majors
    assert "Mathematics" in majors
    assert "Physics" in majors
    assert len(majors) == 3
    majors = unique_majors(secondary_students)
    assert "Computer Science" not in majors
    assert "Mathematics" in majors
    assert "Physics" in majors
    assert len(majors) == 2

def test_empty_students():
    assert unique_majors([]) == set()
