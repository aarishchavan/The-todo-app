import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field

# streamlit run C:\Users\anish\PycharmProjects\web_app1\web.py [ARGUMENTS]

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

st.text_input(label = "", placeholder = "Add a new todo...",
              on_change=add_todo, key = 'new_todo')

for index, todo in enumerate(todos.copy()):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checkbox:
        # Get fresh todos list and remove the item
        current_todos = functions.get_todos()
        if index < len(current_todos):
            current_todos.pop(index)
            functions.write_todos(current_todos)
            st.rerun()



