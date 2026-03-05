from lib.data_generator import student_generator
from testing import students, secondary_students

def test_display_students():
    math_students = student_generator(students, "Mathematics")
    
    assert next(math_students)[1] == "Bob Smith"
    assert next(math_students)[1] == "Eve Lewis"

    physics_students = student_generator(secondary_students, "Physics")
    
    assert next(physics_students)[1] == "Benji"
    assert next(physics_students)[1] == "Natalia"
