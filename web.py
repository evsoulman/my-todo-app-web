import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo1 = st.session_state["new_todo"]
    todos.append(todo1 + "\n")
    Functions.write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
