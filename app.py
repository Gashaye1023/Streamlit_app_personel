from pathlib import Path
import streamlit as st
from PIL import Image

# setting pathh
current_path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_path / "css" / "main.css"
resume_file = current_path / "asset" / "CV.pdf"
profile_pic = current_path / "asset" / "gashaye.jpg"



#general settings
PAGE_TITLE = "Gashaye's CV"
PAGE_ICON = ":wave:"
NAME = "Gashaye"
DESCRIPTION = """
I am a passionate and dedicated software engineer with a strong foundation in computer science and a keen interest in developing innovative solutions. I have experience in various programming languages and frameworks, and I am always eager to learn new technologies and improve my skills. My goal is to contribute to impactful projects that make a difference in people's lives.
"""
EMAIL = "gasha.como@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gashaye-adugna-161b72ab/",
    "GitHub": " https://github.com/Gashaye1023",
}
#phone number
PHONE = "+251920458761"
PROJECTS = {
  
    }

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# Load CSS,PDF, and image files
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
image = Image.open(profile_pic)

# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL        )



    # section for social media
    st.write("#")
    col1= st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with col1[index]:
            st.write(f"[{platform}]({link})")

#phone number
st.write("#")
st.subheader("Phone Number")
st.write(f"📞 {PHONE}")
# exprience and qualification
st.write("#")
st.subheader("Experience and Qualification")
st.write(
    """
    - Data Science and Machine Learning Intern 
    - Software Engineer Intern 
    - Bachelor and master of Science in Computer Science 
    - Completed various online courses in Data Science, Machine Learning, and Software Development
    """
)
# Projects
st.write("#")
st.subheader("Projects")
for project, link in PROJECTS.items():
    st.write(f"- [{project}]({link})")
# Skills
st.write("#")
st.subheader("Skills")              
st.write(
    """
    - Programming Languages: Python, Java, C++
    - Web Development: HTML, CSS, JavaScript, Flask
    - Data Science: Pandas, NumPy, Matplotlib, Scikit-learn
    - Machine Learning: TensorFlow, Keras
    - Database Management: SQL, MongoDB
    - Version Control: Git
    """
)
# Contact
st.write("#")
st.subheader("Contact")
st.write(
    """
    If you would like to get in touch, feel free to reach out via email or connect with me on LinkedIn or GitHub.
    """
)
# Footer
st.write("#")                   