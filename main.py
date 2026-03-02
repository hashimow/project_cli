from models import User, Project, Task
from utils import load_data, save_data

def main():
    data = load_data()
    users = [User(**u) for u in data["users"]]
    projects = [Project(**p) for p in data["projects"]]
    tasks = [Task(**t) for t in data["tasks"]]

    while True:
        print("\n--- Project Management CLI ---")
        print("1. Add User")
        print("2. Edit User")
        print("3. Remove User")
        print("4. List Users")
        print("5. Add Project")
        print("6. Edit Project")
        print("7. List Projects")
        print("8. Add Task")
        print("9. Edit Task")
        print("10. Complete Task")
        print("11. List Tasks")
        print("12. Exit")

        choice = input("Choose an option: ")

        # ---------------- Add User ----------------
        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = User(name, email)
            users.append(user)
            print(f"User {name} added.")

        # ---------------- Edit User ----------------
        elif choice == "2":
            uid = int(input("Enter user ID to edit: "))
            user = next((u for u in users if u.id == uid), None)
            if user:
                new_name = input(f"New name ({user.name}): ") or user.name
                new_email = input(f"New email ({user.email}): ") or user.email
                user.name = new_name
                user.email = new_email
                print(f"User {uid} updated.")
            else:
                print("User not found.")

        # ---------------- Remove User ----------------
        elif choice == "3":
            uid = int(input("Enter user ID to remove: "))
            users = [u for u in users if u.id != uid]
            print(f"User {uid} removed.")

        # ---------------- List Users ----------------
        elif choice == "4":
            print("Users:")
            for u in users:
                user_projects = [p.title for p in projects if p.id in u.projects]
                print(f"{u.id}: {u.name} ({u.email}) - Projects: {', '.join(user_projects)}")

        # ---------------- Add Project ----------------
        elif choice == "5":
            title = input("Project title: ")
            desc = input("Project description: ")
            due = input("Project due date: ")
            owner_id = int(input("Owner user ID: "))
            project = Project(title, desc, due, owner_id=owner_id)
            projects.append(project)
            for u in users:
                if u.id == owner_id:
                    u.projects.append(project.id)
            print(f"Project '{title}' added.")

        # ---------------- Edit Project ----------------
        elif choice == "6":
            pid = int(input("Enter project ID to edit: "))
            project = next((p for p in projects if p.id == pid), None)
            if project:
                project.title = input(f"New title ({project.title}): ") or project.title
                project.description = input(f"New description ({project.description}): ") or project.description
                project.due_date = input(f"New due date ({project.due_date}): ") or project.due_date
                new_owner = input(f"New owner ID ({project.owner_id}): ")
                if new_owner:
                    project.owner_id = int(new_owner)
                print(f"Project {pid} updated.")
            else:
                print("Project not found.")

        # ---------------- List Projects ----------------
        elif choice == "7":
            print("Projects:")
            for p in projects:
                owner = next((u.name for u in users if u.id == p.owner_id), "Unknown")
                project_tasks = [t.title for t in tasks if t.id in p.tasks]
                print(f"{p.id}: {p.title} (Owner: {owner}) - Tasks: {', '.join(project_tasks)}")

        # ---------------- Add Task ----------------
        elif choice == "8":
            title = input("Task title: ")
            assigned_to = input("Assign to (user name, optional): ") or None
            project_id = int(input("Project ID: "))
            task = Task(title, assigned_to, project_id=project_id)
            tasks.append(task)
            for p in projects:
                if p.id == project_id:
                    p.tasks.append(task.id)
            print(f"Task '{title}' added.")

        # ---------------- Edit Task ----------------
        elif choice == "9":
            tid = int(input("Enter task ID to edit: "))
            task = next((t for t in tasks if t.id == tid), None)
            if task:
                task.title = input(f"New title ({task.title}): ") or task.title
                task.assigned_to = input(f"New assigned user ({task.assigned_to}): ") or task.assigned_to
                task.status = input(f"New status ({task.status}): ") or task.status
                print(f"Task {tid} updated.")
            else:
                print("Task not found.")

        # ---------------- Complete Task ----------------
        elif choice == "10":
            tid = int(input("Enter task ID to mark complete: "))
            task = next((t for t in tasks if t.id == tid), None)
            if task:
                task.mark_complete()
                print(f"Task '{task.title}' marked complete.")
            else:
                print("Task not found.")

        # ---------------- List Tasks ----------------
        elif choice == "11":
            print("Tasks:")
            for t in tasks:
                proj_title = next((p.title for p in projects if p.id == t.project_id), "Unknown")
                print(f"{t.id}: {t.title} (Project: {proj_title}, Assigned: {t.assigned_to}, Status: {t.status})")

        # ---------------- Exit ----------------
        elif choice == "12":
            data["users"] = [u.__dict__ for u in users]
            data["projects"] = [p.__dict__ for p in projects]
            data["tasks"] = [t.__dict__ for t in tasks]
            save_data(data)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()