import streamlit as st
import functions

# Initialize session state for editing
if 'editing_index' not in st.session_state:
    st.session_state.editing_index = None

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo.strip():  # Only add non-empty todos
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear the input field


def start_edit(index):
    st.session_state.editing_index = index
    st.session_state[f"edit_todo_{index}"] = todos[index].strip()


def save_edit(index):
    new_todo = st.session_state[f"edit_todo_{index}"].strip()
    if new_todo:
        current_todos = functions.get_todos()
        current_todos[index] = new_todo + "\n"
        functions.write_todos(current_todos)
    st.session_state.editing_index = None
    st.rerun()


def cancel_edit():
    st.session_state.editing_index = None
    st.rerun()


# streamlit run C:\Users\anish\PycharmProjects\web_app1\web.py [ARGUMENTS]

st.title("The Todo App")
st.subheader("This is my todo app")

st.write("This app is to increase your productivity")
st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos.copy()):
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        if st.session_state.editing_index == index:
            # Show text input for editing
            st.text_input(
                label="",
                value=todo.strip(),
                key=f"edit_todo_{index}",
                label_visibility="collapsed"
            )
        else:
            # Show checkbox for normal display
            checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
            if checkbox:
                # Get fresh todos list and remove the item
                current_todos = functions.get_todos()
                if index < len(current_todos):
                    current_todos.pop(index)
                    functions.write_todos(current_todos)
                    st.rerun()

    with col2:
        if st.session_state.editing_index == index:
            # Show save button during editing
            if st.button("Save", key=f"save_{index}"):
                save_edit(index)
        else:
            # Show edit button normally
            if st.button("Edit", key=f"edit_{index}"):
                start_edit(index)

    with col3:
        if st.session_state.editing_index == index:
            # Show cancel button during editing
            if st.button("Cancel", key=f"cancel_{index}"):
                cancel_edit()

