from lib.filters import filter_students_by_major
from testing import students, secondary_students

def test_filter_students_by_major():
    cs_students = filter_students_by_major(students, "Computer Science")
    assert len(cs_students) == 2
    assert cs_students[0][1] == "Alice Johnson"
    math_students = filter_students_by_major(secondary_students, "Mathematics")
    assert len(math_students) == 3
    assert math_students[0][1] == "Miles"

def test_filter_no_results():
    bio_students = filter_students_by_major(students, "Biology")
    assert bio_students == []
    alt_cs_students = filter_students_by_major(secondary_students, "Computer Science")
    assert len(alt_cs_students) == 0
