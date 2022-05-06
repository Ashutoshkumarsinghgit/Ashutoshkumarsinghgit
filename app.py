import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Meenakshi")
st.title("🎓 Free Certificates")

st.write(
    "We allow you to get free Certificates for you and your friends for all Coding related courses. "
)

left, right = st.columns(2)

right.write("This is how your certificate will look like")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill your details:")
form = left.form("template_form")
student = form.text_input("Your Name:")
course = form.selectbox(
    "Choose which course certificate do you want",
    ["Advanced Python", "Python Basics","Advanced Java","C++ basics","Advanced C++","Web Developer"],
    index=0,
)
grade = form.slider("You are free to give any marks to you.", 1, 100, 65)
submit = form.form_submit_button("Generate CERTIFICATE")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Your Certificate is generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download your Certificate",
        data=pdf,
        file_name="Certificate.pdf",
        mime="application/octet-stream",
    )
