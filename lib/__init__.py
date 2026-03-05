from lib.student_data import students, more_students
from lib.filters import filter_students_by_major, filter_students_by_id_range, filter_students_by_name_length
from lib.data_processing import (format_student_data, display_students, 
                               get_student_names, get_student_count_by_major, sort_students_by_name)
from lib.set_operations import (unique_majors, unique_name_initials, common_majors,
                              all_majors, unique_majors_count, students_by_major)
from lib.data_generator import (student_generator, student_names_generator,
                              student_id_generator, process_large_dataset, get_student_info_generator)


def main():
    print("=" * 50)
    print("STUDENT DATA MANAGEMENT SYSTEM")
    print("=" * 50)
    
    # Display all students
    print("\n1. All Students:")
    display_students(students)
    
    # Filter by major
    print("\n2. Computer Science Students:")
    cs_students = filter_students_by_major(students, "Computer Science")
    display_students(cs_students)
    
    # Get unique majors
    print("\n3. Unique Majors:")
    print(unique_majors(students))
    
    # Count students by major
    print("\n4. Student Count by Major:")
    for major, count in get_student_count_by_major(students).items():
        print(f"   {major}: {count} students")
    
    # Get student names
    print("\n5. All Student Names:")
    print(get_student_names(students))
    
    # Sort students by name
    print("\n6. Students Sorted by Name:")
    sorted_students = sort_students_by_name(students)
    display_students(sorted_students)
    
    # Set operations
    print("\n7. Unique Name Initials:")
    print(unique_name_initials(students))
    
    print("\n8. Students Grouped by Major:")
    for major, student_names in students_by_major(students).items():
        print(f"   {major}: {student_names}")
    
    # Generator expressions
    print("\n9. Using Generator for Math Students:")
    math_gen = student_generator(students, "Mathematics")
    for student in math_gen:
        print(f"   {format_student_data(student)}")
    
    # Process with generator
    print("\n10. Using Student Names Generator:")
    names_gen = student_names_generator(students, "Physics")
    for name in names_gen:
        print(f"    {name}")
    
    # Chunk processing
    print("\n11. Processing Large Dataset in Chunks:")
    all_students = students + more_students
    for i, chunk in enumerate(process_large_dataset(all_students, 5)):
        print(f"   Chunk {i + 1}: {len(chunk)} students")
    
    # Common majors between two datasets
    print("\n12. Common Majors between Students and More Students:")
    print(common_majors(students, more_students))
    
    print("\n" + "=" * 50)
    print("END OF DEMONSTRATION")
    print("=" * 50)


if __name__ == "__main__":
    main()