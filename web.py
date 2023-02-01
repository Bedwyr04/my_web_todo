import streamlit as file
import functions

todolist = functions.get_todos('r', 0)


def add_todo_web():
    text = file.session_state["new_todo"]
    functions.print_todo_onlist(text)


file.title("My To-do App")
file.subheader("This is my to-do app")
file.write("This app is for increase your productivity")

for todo in todolist:
    checkbox = file.checkbox(todo, key=todo)
    if checkbox:
        functions.complete(todo)
        del file.session_state[todo]
        file.experimental_rerun()

file.text_input(label="Input", placeholder="Enter a new todo",
                on_change=add_todo_web, key="new_todo")
