import typer

from database import Database
from data import Project, Task
from constants import TaskStatusE

app = typer.Typer()
project_app = typer.Typer()
task_app = typer.Typer()
project_app.add_typer(task_app, name="tasks")
app.add_typer(project_app, name="projects")

database = Database()


@project_app.command("list")
def project_list():
    """List of the available projects."""
    projects = [Project(id=row[0], name=row[1], description=row[2]) for row in database.get_project_list()]
    if not projects:
        typer.echo("No projects defined.")
        return
    for project in projects:
        typer.echo(f"Project: {project.name}, description: {project.description}, ID: {project.id}")


@project_app.command("create")
def project_create(project_name: str, description: str = None):
    """Create the new project."""
    project = Project(id=None, name=project_name, description=description)
    database.create_project(project)
    typer.echo(f"Project `{project_name}` created.")


@task_app.command("list")
def task_list(project_name: str):
    """List of the available tasks in given project."""
    project_data = database.get_project_by_name(name=project_name)
    project = Project(id=project_data[0][0], name=project_data[0][1], description=project_data[0][2])
    tasks = [Task(id=row[0], title=row[1], description=row[2], status=row[3], project_id=row[4])
             for row in database.get_task_list(project_id=project.id)]
    if not tasks:
        typer.echo(f"No tasks defined for project {project.name}.")
        return
    for task in tasks:
        typer.echo(f"Task: {task.title}, status: {task.get_display_status()}, description: {task.description}, "
                   f"project: {project.name}/{project.id}")


@task_app.command("open")
def task_open(task_id: int):
    """Open the task with task_id."""
    database.set_task_status(task_id=task_id, status=TaskStatusE.OPEN)
    typer.echo(f"Opening the task: {task_id}")


@task_app.command("close")
def task_close(task_id: int):
    """Close the task with task_id."""
    database.set_task_status(task_id=task_id, status=TaskStatusE.CLOSED)
    typer.echo(f"Closing the task: {task_id}")


@task_app.command("show")
def task_show(task_id: int):
    """Show the task details with task_id."""
    task_data = database.get_task_by_id(task_id=task_id)
    task = Task(id=task_data[0][0], title=task_data[0][1], description=task_data[0][2], status=task_data[0][3],
                project_id=task_data[0][4])
    project_data = database.get_project_by_id(project_id=task.project_id)
    project = Project(id=project_data[0][0], name=project_data[0][1], description=project_data[0][2])
    typer.echo(f"Task: {task.title}, status: {task.get_display_status()}, description: {task.description}, "
               f"project: {project.name}/{project.id}")


@task_app.command("create")
def task_create(project_name: str, title: str, description: str = None):
    """Create new task."""
    project_data = database.get_project_by_name(name=project_name)
    project = Project(id=project_data[0][0], name=project_data[0][1], description=project_data[0][2])
    task = Task(id=None, title=title, description=description, status=TaskStatusE.OPEN, project_id=project.id)
    database.create_task(task)
    typer.echo(f"Task created: {title} in project {project.name}")


if __name__ == "__main__":
    database.initialize()
    app()