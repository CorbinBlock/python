from dataclasses import dataclass
from typing import Union

from constants import TaskStatusE


@dataclass
class Project:
    id: Union[int, None]  # this is because when creating we do not have the ID yet
    name: str
    description: Union[str, None]  # description is optional


@dataclass
class Task:
    id: Union[int, None]  # this is because when creating we do not have the ID yet
    title: str
    description: Union[str, None]  # description is optional
    status: int
    project_id: int

    def get_display_status(self):
        return TaskStatusE(self.status).name