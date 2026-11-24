# Module: teacher_module.py
# Made by: Manan (Teacher Functions & Reports)

from admin_module import save_data


def show_all_students(students):
    if len(students) == 0:
        print("Koi student data nathi bhai! Pehla Admin ma jaine add karo.")
        return

    print("\n-------------------------------------------------------------")
    print(f"{'ID':<6} {'Name':<20} {'Branch':<22} {'Marks':<7} {'Att%'}")
    print("-------------------------------------------------------------")
    for s in students:
        print(f"{s['id']:<6} {s['name']:<20} {s['branch']:<22} {s['marks']:<7} {s['attendance']}%")
    print("-------------------------------------------------------------")


def teacher_menu(students):
    while True:
        print("\n--- TEACHER PORTAL ---")
        print("1. Badha Students Jovo (View All)")
        print("2. Student Search Karo (By ID or Name)")
        print("3. Marks ane Attendance Update Karo")
        print("4. Class Topper Jovo")
        print("5. Paccha Jao (Back)")
        choice = input("Option select karo (1-5): ").strip()

        if choice == "1":
            show_all_students(students)

        elif choice == "2":
            q = input("Student nu Naam ke ID lakho: ").strip().lower()
            found = False
            for s in students:
                if q == s["id"].lower() or q in s["name"].lower():
                    print(f"Malyo! -> ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']} | Att: {s['attendance']}%")
                    found = True
            if not found:
                print("Koi na malyu bhai, spelling check karo!")

        elif choice == "3":
            sid = input("Jena marks update karva hoy eno ID nakho: ").strip()
            found = False
            for s in students:
                if s["id"] == sid:
                    found = True
                    print(f"Selected: {s['name']} (Current Marks: {s['marks']}, Att: {s['attendance']}%)")
                    try:
                        new_marks = int(input("Nava Marks nakho (0-100): "))
                        new_att = int(input("Navi Attendance nakho (0-100): "))
                        if 0 <= new_marks <= 100 and 0 <= new_att <= 100:
                            s["marks"] = new_marks
                            s["attendance"] = new_att
                            save_data(students)
                            print("Done! Marks ane attendance update thai gaya chhe!")
                        else:
                            print("Bhai 0 thi 100 ni vachhe number nakho!")
                    except ValueError:
                        print("Arey sir, number nakhvano chhe, ABCD nahi!")
                    break
            if not found:
                print("Aa ID no student list ma nathi!")

        elif choice == "4":
            if len(students) == 0:
                print("Data khali chhe bhai!")
            else:
                topper = max(students, key=lambda x: x["marks"])
                print(f"\nClass no Topper chhe: {topper['name']} ({topper['marks']} marks)! Party to banti hai!")

        elif choice == "5":
            break
        else:
            print("Khotu option chhe, 1-5 ma thi select karo.")
