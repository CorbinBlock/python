import os.path
import sqlite3

from constants import TaskStatusE


class Database:
    PROJECT_SQL = """CREATE TABLE project (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name text, 
        description text NULL);"""
    TASK_SQL = """CREATE TABLE task (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title text, 
        description text, 
        status integer, 
        project_id integer, 
        FOREIGN KEY(project_id) REFERENCES project(id));"""
    PROJECT_LIST_SQL = """SELECT * FROM project;"""
    TASK_LIST_SQL = """SELECT * FROM task WHERE project_id=?;"""
    PROJECT_BY_NAME = """SELECT * FROM project WHERE name=?;"""
    PROJECT_BY_ID = """SELECT * FROM project WHERE id=?;"""
    TASK_BY_ID = """SELECT * FROM task WHERE id=?;"""
    SET_TASK_STATUS = """UPDATE task SET status=? WHERE id=?;"""
    CREATE_PROJECT = """INSERT INTO project (name, description) VALUES (?, ?);"""
    CREATE_TASK = """INSERT INTO task (title, description, status, project_id) VALUES (?, ?, ?, ?);"""

    def _db_exists(self):
        return os.path.exists("todos.db")

    def run_sql(self, query, args=None, commit=False, fetch=False):
        args = args or ()
        data = None
        with sqlite3.connect("todos.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query, args)
            if commit:
                connection.commit()
            if fetch:
                data = cursor.fetchall()
        return data

    def get_connection(self):
        return sqlite3.connect("todos.db")

    def initialize(self):
        if self._db_exists():
            return
        self.run_sql(self.PROJECT_SQL)
        self.run_sql(self.TASK_SQL)

    def get_project_list(self):
        return self.run_sql(query=self.PROJECT_LIST_SQL, fetch=True)

    def get_task_list(self, project_id):
        return self.run_sql(query=self.TASK_LIST_SQL, args=(project_id, ), fetch=True)

    def get_project_by_name(self, name):
        return self.run_sql(query=self.PROJECT_BY_NAME, args=(name, ), fetch=True)

    def get_project_by_id(self, project_id):
        return self.run_sql(query=self.PROJECT_BY_ID, args=(project_id, ), fetch=True)

    def get_task_by_id(self, task_id):
        return self.run_sql(query=self.TASK_BY_ID, args=(task_id, ), fetch=True)

    def set_task_status(self, task_id, status):
        return self.run_sql(query=self.SET_TASK_STATUS, args=(status, task_id), commit=True)

    def create_project(self, project):
        return self.run_sql(query=self.CREATE_PROJECT, args=(project.name, project.description or ""),
                            commit=True)

    def create_task(self, task):
        return self.run_sql(query=self.CREATE_TASK,
                            args=(task.title, task.description, TaskStatusE.OPEN, task.project_id),
                            commit=True)