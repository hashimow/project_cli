from utils import load_data, save_data

class User:
    _id_counter = 1
    def __init__(self, name, email, _id=None):
        self.id = _id or User._id_counter
        User._id_counter = max(User._id_counter, self.id + 1)
        self.name = name
        self.email = email
        self.projects = []

    def __str__(self):
        return f"User({self.id}): {self.name}, Email: {self.email}"

class Project:
    _id_counter = 1
    def __init__(self, title, description="", due_date=None, _id=None, owner_id=None):
        self.id = _id or Project._id_counter
        Project._id_counter = max(Project._id_counter, self.id + 1)
        self.title = title
        self.description = description
        self.due_date = due_date
        self.owner_id = owner_id
        self.tasks = []

    def __str__(self):
        return f"Project({self.id}): {self.title} - Due: {self.due_date}"

class Task:
    _id_counter = 1
    def __init__(self, title, assigned_to=None, status="Pending", _id=None, project_id=None):
        self.id = _id or Task._id_counter
        Task._id_counter = max(Task._id_counter, self.id + 1)
        self.title = title
        self.assigned_to = assigned_to
        self.status = status
        self.project_id = project_id

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task({self.id}): {self.title} - {self.status}"