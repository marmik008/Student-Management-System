# Module: admin_module.py
# Made by: Marmik & Manan (JSON File Handling & Admin Controls)

import json
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("JSON file read karva ma locho thayo, navu list start karyu chhe.")
        return []


def save_data(students):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


def admin_menu(students):
    while True:
        print("\n--- ADMIN PORTAL ---")
        print("1. Navo Student Add Karo")
        print("2. Student ni Details Edit Karo")
        print("3. Student Delete Karo")
        print("4. Paccha Jao (Back)")
        choice = input("Admin option nakho (1-4): ").strip()

        if choice == "1":
            sid = input("Navo Student ID nakho: ").strip()
            if any(s["id"] == sid for s in students):
                print("Arey bhai, aa ID already exist kare chhe! Bijo ID aapo.")
                continue
            name = input("Student nu Naam: ").strip()
            branch = input("Branch (e.g. Computer Engineering): ").strip()
            try:
                marks = int(input("Initial Marks (0-100): "))
                att = int(input("Attendance % (0-100): "))
            except ValueError:
                print("Marks ane attendance number ma j nakho bhai!")
                continue

            students.append({
                "id": sid,
                "name": name,
                "branch": branch,
                "marks": marks,
                "attendance": att
            })
            save_data(students)
            print(f"Badhai ho! {name} ne system ma add kari didho chhe!")

        elif choice == "2":
            sid = input("Edit karva mate Student ID nakho: ").strip()
            found = False
            for s in students:
                if s["id"] == sid:
                    found = True
                    print(f"Current -> Name: {s['name']}, Branch: {s['branch']}")
                    new_name = input("Navu Naam (khali chhodo jo change na karvu hoy): ").strip()
                    new_branch = input("Navi Branch (khali chhodo jo change na karvu hoy): ").strip()
                    if new_name:
                        s["name"] = new_name
                    if new_branch:
                        s["branch"] = new_branch
                    save_data(students)
                    print("Details update thai gai chhe boss!")
                    break
            if not found:
                print("Aa ID no student malyo nahi!")

        elif choice == "3":
            sid = input("Delete karva mate Student ID nakho: ").strip()
            for i, s in enumerate(students):
                if s["id"] == sid:
                    removed = students.pop(i)
                    save_data(students)
                    print(f"Tata bye-bye! {removed['name']} no record delete thai gayo.")
                    break
            else:
                print("Koi student na malyo aa ID thi!")

        elif choice == "4":
            break
        else:
            print("1 thi 4 ma thi option select karo bhai!")
