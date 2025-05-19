
def add_problem():
    title = input("Enter problem title: ")
    topic = input("Enter topic: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")
    status = "To Do"  

    with open("problems.txt", "a") as file:
        file.write(f"{title} | {topic} | {difficulty} | {status}\n")
    print("✅ Problem added successfully!\n")


def view_all_problems():
    print("\n📘 All Problems:\n")
    try:
        with open("problems.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No problems added yet.")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No problems found. Please add some first.")


def mark_as_solved():
    title_to_mark = input("Enter the title of the problem to mark as solved: ")
    updated_lines = []
    found = False

    try:
        with open("problems.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            parts = line.strip().split(" | ")
            if len(parts) == 4 and parts[0].lower() == title_to_mark.lower():
                parts[3] = "Solved"
                found = True
                print(f"✅ Marked '{parts[0]}' as Solved.")
            updated_lines.append(" | ".join(parts) + "\n")

        with open("problems.txt", "w") as file:
            file.writelines(updated_lines)

        if not found:
            print("❌ Problem not found.")
    except FileNotFoundError:
        print("No problems file found. Please add a problem first.")


def filter_by_topic():
    topic_to_search = input("Enter topic to filter by: ").lower()
    print(f"\n📂 Problems under topic: {topic_to_search.title()}\n")
    found = False

    try:
        with open("problems.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" | ")
                if len(parts) == 4 and parts[1].lower() == topic_to_search:
                    print(line.strip())
                    found = True
        if not found:
            print("No problems found under this topic.")
    except FileNotFoundError:
        print("No problems file found.")


def export_solved_problems():
    solved_problems = []
    try:
        with open("problems.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Solved" in line:
                    solved_problems.append(line)

        with open("solved_problems.txt", "w") as file:
            file.writelines(solved_problems)

        print(f"📤 Exported {len(solved_problems)} solved problems to 'solved_problems.txt'")
    except FileNotFoundError:
        print("No problems file found.")


# === Main Menu ===
while True:
    print("\n🎯 === AlgoPro Tracker ===")
    print("1. Add Problem")
    print("2. View All Problems")
    print("3. Mark Problem as Solved")
    print("4. Filter by Topic")
    print("5. Export Solved Problems")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        add_problem()
    elif choice == "2":
        view_all_problems()
    elif choice == "3":
        mark_as_solved()
    elif choice == "4":
        filter_by_topic()
    elif choice == "5":
        export_solved_problems()
    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid option. Try again.")
