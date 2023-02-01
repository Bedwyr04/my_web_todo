# FILEPATH = "../textfiles/Todos.txt"
FILEPATH = "Todos.txt"


def get_todos(action, list_local, filepath=FILEPATH):
    """
    Read a text file and return the list of already existent to do items
    or write new to do in the list
    """
    if action == "r":
        with open(filepath, 'r') as file_local:
            todolist_local = file_local.readlines()
        return todolist_local
    elif action == "w":
        with open(filepath, 'w') as file_local:
            file_local.writelines(list_local)


def print_todo_onlist(new_todo):
    todolist = get_todos('r', 0)
    new_todo = new_todo.capitalize()
    todolist.append(new_todo + '\n')
    get_todos('w', todolist)
    return todolist


def edit_todo(old_todo, new_todo):
    new_todo = new_todo.capitalize()
    todolist = get_todos('r', 0)
    index = todolist.index(old_todo)
    todolist[index] = new_todo
    get_todos('w', todolist)
    return todolist


def complete(old_todo):
    todolist = get_todos('r', 0)
    todolist.remove(old_todo)
    get_todos('w', todolist)
    return todolist

