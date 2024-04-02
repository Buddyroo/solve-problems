# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.


class Task():
    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status
    def mark_done(self):
        self.status = True

    def info(self):
        print(f"Задача {self.description} со сроком исполнения {self.due_date} и статусом {'В процессе' if not self.status else 'Выполнена'}")



tasks_list = []

def add_task(task):
    tasks_list.append(task)

def print_active():
    for task in tasks_list:
        if not task.status:
            task.info()


task1=Task("Present monthly plan","12/24",)
task2=Task("Prepare budget","11/24",)
task3=Task("Renovate office space","12/25",)


add_task(task1)
add_task(task2)
add_task(task3)

print_active()






