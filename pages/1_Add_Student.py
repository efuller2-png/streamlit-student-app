import streamlit as st
import psycopg2

st.set_page_config(page_title="Add Student", page_icon="👤")

def get_connection():
    return psycopg2.connect(st.secrets["DB_URL"])

st.title("👤 Add a New Student")

with st.form("add_student_form"):
    name = st.text_input("Student Name")
    email = st.text_input("Student Email")
    submitted = st.form_submit_button("Add Student")

if submitted:
    if not name or not email:
        st.warning("Please fill in both fields.")
    else:
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO students10 (name, email) VALUES (%s, %s);", (name, email))
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"✅ Student '{name}' added successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
