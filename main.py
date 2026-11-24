# Project: Student Management System (3 Roles: Student, Teacher, Admin)
# Team Members: Marmik & Manan (7 Days College Mini Project)

from teacher_module import teacher_menu, show_all_students
from admin_module import admin_menu, load_data


def student_menu(students):
    while True:
        print("\n--- STUDENT PORTAL ---")
        print("1. Maro Profile ane Marks Jovo (View My Result)")
        print("2. Badha Students nu List Jovo (View Directory)")
        print("3. Paccha Jao (Back)")
        choice = input("Tamaro option nakho (1-3): ").strip()

        if choice == "1":
            sid = input("Tamaro Student ID nakho (e.g. 101): ").strip()
            found = False
            for s in students:
                if s["id"] == sid:
                    found = True
                    marks = s["marks"]
                    grade = "Pass" if marks >= 35 else "Fail"
                    print(f"\nNaam: {s['name']} | Branch: {s['branch']}")
                    print(f"Marks: {marks}/100 | Attendance: {s['attendance']}% | Result: {grade}")
                    if marks >= 80:
                        print("Wah bhai wah! Topper niklya tame to!")
                    elif marks >= 35:
                        print("Bachi gaya bhai, pass thai gaya!")
                    else:
                        print("Arre bhai thodu vanchvanu rakho, ATKT aavse!")
                    break
            if not found:
                print("Arey bhai, aa ID no koi student nathi! Sacho ID nakho.")

        elif choice == "2":
            show_all_students(students)

        elif choice == "3":
            break
        else:
            print("Khotu button dabavyu bhai! 1 thi 3 ma thi nakho.")


def main():
    students = load_data()
    print("==========================================")
    print("   STUDENT MANAGEMENT SYSTEM (BY MARMIK & MANAN)")
    print("==========================================")
    print(f"Total {len(students)} students no data mali gayo chhe!")

    while True:
        print("\nRole Select Karo:")
        print("1. Student")
        print("2. Teacher")
        print("3. Admin")
        print("4. Exit (Bahaar Niklo)")
        role = input("Enter choice (1-4): ").strip()

        if role == "1":
            student_menu(students)
        elif role == "2":
            teacher_menu(students)
        elif role == "3":
            admin_menu(students)
        elif role == "4":
            print("Chalo aavjo! System bandh thay chhe... Tata!")
            break
        else:
            print("Arey yaar, 1, 2, 3 ke 4 nakho ne!")


if __name__ == "__main__":
    main()
