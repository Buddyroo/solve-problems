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
        if not self.status:
            self.status = True
            print(f"\n----Задача '{self.description}' успешно выполнена.----")
        else:
            print("\nЗадача не была помечена, так как уже имеет статус 'Выполнена'")

    def info(self):
        print(
            f"Задача {self.description} со сроком исполнения {self.due_date} и статусом '{'В процессе' if not self.status else 'Выполнена'}'")


tasks_list = []


def add_task(task):
    tasks_list.append(task)
    print(f"\nЗадача {task.description} со сроком исполнения {task.due_date} "
          f"добавлена в список задач")


#Вариант вывода активных задач
#def print_active():
#     print("\nСписок текущих задач")
#     task_active = []
#     for task in tasks_list:
#         if not task.status:
#             task_active.append(task)  # добавляем задачу в список активных задач. потом проверим, пустой ли список
#             task.info()
#     if not task_active:  # если список пустой
#         print("Все задачи списка были выполнены")

def print_active():
    active_tasks=[task for task in tasks_list if not task.status]
    if active_tasks:
        print("\nСписок текущих задач:")
        for task in active_tasks:
            task.info()
    else:
        print("\nВсе задачи списка были выполнены")


task1 = Task("Present monthly plan", "12/24", )
task2 = Task("Prepare budget", "11/24", )
task3 = Task("Renovate office space", "12/25", )

add_task(task1)
add_task(task2)
add_task(task3)

print_active()
task1.mark_done()
task1.mark_done()
print_active()
task2.mark_done()
task3.mark_done()
print_active()
