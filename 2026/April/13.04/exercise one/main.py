from pathlib import Path

from aluno import student
from persistencia import load_students, save_students

data_file = str(Path(__file__).with_name("class_record.txt"))


def ask_student_name(students):
    name = input("student name: ").strip().lower()
    if not name:
        print("invalid name.")
        return None
    item = students.get(name)
    if not item:
        print("student not found.")
        return None
    return item


def ask_grade():
    try:
        grade = float(input("module grade (0 to 20): ").strip().replace(",", "."))
    except ValueError:
        print("invalid grade.")
        return None
    if grade < 0 or grade > 20:
        print("grade must be between 0 and 20.")
        return None
    return grade


def register_student(students):
    name = input("student name: ").strip().lower()
    if not name:
        print("invalid name.")
        return
    if name in students:
        print("student already exists.")
        return
    students[name] = student(name=name)
    print("student registered.")


def add_subject_modules(students):
    item = ask_student_name(students)
    if not item:
        return

    subject_name = input("subject name: ").strip().lower()
    if not subject_name:
        print("invalid subject.")
        return

    modules_text = input("modules (comma separated): ").strip().lower()
    modules = [module.strip() for module in modules_text.split(",") if module.strip()]
    if not modules:
        print("add at least one module.")
        return

    item.add_subject(subject_name, modules)
    print("subject and modules saved.")


def add_module_grade(students):
    item = ask_student_name(students)
    if not item:
        return

    subject_name = input("subject: ").strip().lower()
    if subject_name not in item.subjects:
        print("subject not found for this student.")
        return

    module_name = input("module: ").strip().lower()
    grade = ask_grade()
    if grade is None:
        return

    if item.add_grade(subject_name, module_name, grade):
        print("grade saved.")
    else:
        print("module not found in this subject.")


def show_averages(students):
    item = ask_student_name(students)
    if not item:
        return

    if not item.subjects:
        print("this student has no subjects yet.")
        return

    print(f"\nstudent averages: {item.name}")
    for subject_name, subject_item in item.subjects.items():
        average = subject_item.average()
        if average is None:
            print(f"- {subject_name}: no grades")
        else:
            print(f"- {subject_name}: {average:.2f}")

    overall = item.overall_average()
    if overall is not None:
        print(f"overall average: {overall:.2f}")


def list_class(students):
    if not students:
        print("no students registered yet.")
        return
    print("\nregistered students:")
    for name in sorted(students):
        print(f"- {name}")


def menu():
    students = load_students(data_file)

    while True:
        print("\n===== class manager =====")
        print("1 - register student")
        print("2 - add subject and modules")
        print("3 - add module grade")
        print("4 - show student averages")
        print("5 - list class")
        print("6 - save and exit")

        option = input("choose an option: ").strip().lower()

        if option == "1":
            register_student(students)
        elif option == "2":
            add_subject_modules(students)
        elif option == "3":
            add_module_grade(students)
        elif option == "4":
            show_averages(students)
        elif option == "5":
            list_class(students)
        elif option == "6":
            save_students(data_file, students)
            print(f"data saved in '{data_file}'. bye.")
            break
        else:
            print("invalid option.")


if __name__ == "__main__":
    menu()
