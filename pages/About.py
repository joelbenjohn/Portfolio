# File: pages/About.py
import streamlit as st

def main():
    st.title("About Me")
    st.write("Hi, I'm Joel Ben John. I have a diverse skill set in Structural Engineering, Data Science, and Software Development. My unique combination of skills allows me to approach projects from multiple perspectives and deliver effective solutions.")

    st.subheader("Structural Engineering")
    st.write("I have extensive experience in structural design, analysis, and construction projects, focusing on safety and efficiency.")

    st.subheader("Data Science")
    st.write("I'm passionate about extracting insights from data. My expertise includes data analysis, predictive modeling, and data visualization.")

    st.subheader("Software Development")
    st.write("I develop full-stack web applications, backend services, and automation tools. I focus on creating scalable, maintainable, and user-friendly software solutions.")

    st.write("Feel free to connect with me on [LinkedIn](https://linkedin.com) or check out my [GitHub](https://github.com).")

if __name__ == "__main__":
    main()