from queue import LifoQueue


class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def do(self):
        """
        Виконує завдання, за потреби розбиває його на підзавдання
        :return: список підзавдань
        """
        if self.subtasks:
            print(f"Виконую завдання: {self.name}. Розбиваю на підзавдання")
        else:
            print(f"Завершено завдання: {self.name}")

        return self.subtasks


class Project:
    def __init__(self, core_task: Task):
        if not isinstance(core_task, Task):
            raise TypeError('Use <Task> class object.\n')

        self.tasks = LifoQueue()
        self.tasks.put(core_task)

    def do_task(self):
        if self.tasks.qsize() == 0:
            print('No tasks and subtasks left.\n')
            return

        last_task = self.tasks.get()
        last_task_subs = last_task.do()

        if last_task_subs:
            for sub in last_task_subs:
                self.tasks.put(sub)

    def is_finished(self):
        return self.tasks.qsize() == 0