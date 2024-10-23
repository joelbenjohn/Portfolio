# File: Home.py
import streamlit as st

def main():
    st.title("Welcome to My Portfolio")
    st.write("Hello! I'm Joel Ben John, and I specialize in Structural Engineering, Data Science, and Software Development. Below are my key projects and experiences in these domains.")

    st.subheader("Explore My Skills")
    st.write("- [Structural Engineering](?page=StructuralEngineering)")
    st.write("- [Data Science](?page=DataScience)")
    st.write("- [Software Development](?page=SoftwareDevelopment)")

    st.write("For more about me, go to the [About](?page=About) page.")

if __name__ == "__main__":
    main()
