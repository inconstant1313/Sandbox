'''Напишите функцию task_manager, которая принимает список задач для нескольких серверов. 
Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).
Функция должна создавать словарь и заполнять его задачами по следующему принципу: 
название сервера — ключ, по которому хранится очередь задач для конкретного сервера. 
Если поступает задача без высокого приоритета (последний элемент кортежа — False), 
добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.
Для словаря используйте defaultdict, для очереди — deque.
Функция возвращает полученный словарь с задачами.'''

from collections import defaultdict
from collections import deque

def task_manager(tasks):
    task_dict = defaultdict(deque)
    for num_task, name_server,priority_server in tasks:
        if priority_server is False:
            task_dict[name_server].append(num_task)
        else:
            task_dict[name_server].appendleft(num_task)
    return(task_dict)
        
    # Напишите код функции
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})