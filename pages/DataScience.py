import streamlit as st
st.set_page_config(layout="wide")

def generate_course_list(title, courses):

    with st.container(border = True):
        with st.expander(f"**{title}**"):
            st.write("\n".join([f"- {course}" for course in courses]))

def generate_experience_list(title, years, experience):
    
    with st.container(border = True):
        with st.expander(f"**{title}** : {years}"):
            st.write("\n".join([f"- {course}" for course in experience]))


def generate_projects_list(project, under, descrition):
    with st.container(border = True):
        with st.expander(f"**{project}** : {under}"):
            st.write("\n".join([f"- {course}" for course in descrition]))


def main():
    st.title("Data Science Portfolio")
    
    st.subheader("Education")
    left_column, right_column = st.columns([0.7, 0.3])

    with left_column:
        generate_course_list(
        "Massachusetts Institute of Technology: Data Science and Machine Learning Bootcamp",
        [
            "Python Foundations",
            "Making Sense of Unstructured Data",
            "Regression and Prediction",
            "Hypothesis Testing and Classification",
            "Deep Learning",
            "Recommendation Systems",
            "Networking and Graphical Modelling",
            "Intro to Artificial Intelligence",
            "Big Data Analytics",
            "Intro to Data Science and AI"
        ]
    )
        generate_course_list(
        "Johns Hopkins University: Master of Science",
        [            
            "Intro to Data Science",
            "Probabilistic Methods",
            "Mathematical Methods For Engineers",
            "Numerical Methods",
            "Operations Research"
        ]
    )
        generate_course_list(
        "Indian Institute of Technology, Madras: Bachelor + Master of Technology",
        [
            "Probability, Statistics and Stochastic Processes",
            "Calculus I Functions of One Variable",
            "Calculus II Functions of Several Variables",
            "Differential Equations",
            "Analytical Techniques in Transportation Engineering",
            "Fundamentals of Operations Research",
            "Advanced Operations Research",
            "Operations Management",
            "Structural Optimization"
        ]
    )
        

    # Create two columns: left for courses/projects, right for certifications
    # left_column, right_column = st.columns([0.7, 0.3])
    
    with right_column:
        st.write("**Certifications**")
        st.write("- [SQL](https://courses.edx.org/certificates/5cbbcee8c74d4f3f9da99b2b3efeb01a) (EdX, 2023)")
        st.write("- [Inference and Modelling](https://courses.edx.org/certificates/6c8f856660f243a2b71b165bc6ae9d9b) (EdX, 2023)")
        st.write("- [Machine Learning with Python](https://www.freecodecamp.org/certification/JoelBenJohn/machine-learning-with-python-v7) (FreeCodeCamp, 2022-2023)")
        st.write("- [Data Analysis with Python](https://www.freecodecamp.org/certification/JoelBenJohn/data-analysis-with-python-v7) (FreeCodeCamp, 2022-2023)")
    
    st.subheader("Work Experience")
    left_column, right_column = st.columns([0.5, 0.5])
    with left_column:
        generate_experience_list("ClarkDierich", "2021 - Present",
                [
                    "Leveraged data science techniques using the latest AI methods including Large Language Models, Deep Learning, and Reinforcement Learning to minimize operations costs through automation and maximize work quality",
                    "Solely developed and created a data platform that optimizes the daily operations of engineers and staff, reducing project timelines from months to weeks."
                ])
        
        generate_experience_list("Johns Hopkins University", "2019-2021",
                [
                    "Leveraged clustering algorithms to model polycrystaline and foam material geometries",
                    "Trained Statistical Models to improve predictive accuracy and correlate geometry to property",
                    "Contributed to open source eigenvalue analysis tool to predict behaviour of thin metals",
                ])
        
    with right_column:
        generate_experience_list("Indian Institute of Technology, Madras", "2017-2019",
                [
                    "Leveraged Linear Regression algorithms to develop methods that predict buckling failure of beams more accurately",
                    "Leveraged Optimization Techniques to achieve optimal shell thickness configurations for Oil Tank Shell Design",
                    "Translated Numerical Methods from MATLAB to C++ to leverage parallelization techniques"
                ])

    st.subheader("Projects")
    left_column, right_column = st.columns([0.5, 0.5])
    with left_column:
        generate_projects_list('Amazon Products Reccomendation System', 'MIT BootCamp Projects',
                               ['Objective: Built a personalized recommendation system using collaborative filtering on Amazon product reviews data.',
                                'Techniques: Implemented Rank-Based, User-User, Item-Item Collaborative Filtering, and Matrix Factorization (SVD) models.',
                                'Performance: Evaluated using Precision@K, Recall@K, F1-Score, and RMSE; improved model accuracy through GridSearchCV hyperparameter tuning.',
                                'Cold-Start Handling: Predicted ratings for new users with no prior interactions to assess model robustness.',
                                'Key Takeaways: Demonstrated real-world collaborative filtering techniques with optimized models, adding value to e-commerce user experience.',
                                'Link to e-portfolio : [link](https://www.mygreatlearning.com/eportfolio/joel-ben-john)']
                              )
        
        generate_projects_list('Youtube LLM Summarizer Web App', 'Personal', 
                               ['Developed web app on streamlit to summarize youtube videos',
                                "Leveraged Cohere LLM summarizer endpoint, youtube_transcipts API to summarize minute long chunks from video transcripts",
                                "Experiment to try implementing an LLM for various use cases",
                                "Use docx package to report summary in structured downloadable word document"
                                "Link to Web Application - [link](https://cohere-joelbenjohn.streamlit.app/)"]
                                )
        # generate_projects_list('')
        generate_projects_list('Test Image Classification, Sorting and Reporting', 'ClarkDietrich',
                               ['Trained a Convolutional Neural Network to classify images as whiteboards or not to identify test image boundaries from batch of images',
                                'Implemented algorithm leveraging chronology in image collection in Camera and test file collection in test systems to map images to respective test',
                                'Implemented win32 comclient program to paste images into approved excel picture file template for each test set, then print to pdf',
                                'Process automates classifying, sorting, reporting of 10000+ images saving 500 hours in a month ']
                                )
        
        generate_projects_list('Machine Learning w Python', 'FreeCodeCamp Course Projects',
                               ['Rock Paper Scissors - Reinforcement Learning Game Bot',
                                'Cat and Dog Image Classifier',
                                'Book Recommendation using KNN',
                                'Linear Regression Health Cost Calculator',
                                'Neural Network SMS Text Classifier'
                                '[Link](https://www.freecodecamp.org/certification/JoelBenJohn/machine-learning-with-python-v7) to projects:']
                                )
        
    with right_column:
        generate_projects_list('Customer Churn Predictor', 'MIT BootCamp Projects',
                               ['Analysed EdTech company dataset to predict factors leading to customer conversion',
                                'Performed Data Cleansing, Preprocessing and Exploratory Data Analysis on dataset',
                                'Trained and Pruned Decision Tree Models using CCP for Feature Importance and Interpretibility',
                                'Trained and Tuned Random Forest Trees using RandomizedSearchCV for Lead Conversion Prediction',
                                'Perfomed Hypothesis Tests on important features to test statistically significant relationship',
                                'Link to e-portfolio : [link](https://www.mygreatlearning.com/eportfolio/joel-ben-john)'])
        
        generate_projects_list('Data Platform', 'ClarkDietrich',
                               ['Developed full stack application on streamlit to automate data extraction, processing and reporting tasks',
                                'Extract scalar and vector data from a batch (100s or even 1000s) of test files of a project using pandas',
                                'Place data in appropriate data structures, databases and excel sheets for further processing, querying and updating needs',
                                'Automatically paste vector and scalar data into Macro Enabled Excel Sheets and then print to pdf for each set of test',
                                'Automatically classify images, sort images, and paste images into Template Excel File and print to pdfs',
                                'Save Project to Load Later',
                                'Platform used by all employees in department to complete what took months within a week']

                                )
        generate_projects_list('Structure to property corelation in metamaterials', 'Johns Hopkins University',
                               ['Leveraged Voronoi Clustering and Laguerre Clustering to generate lattices of cellular metamaterials',
                                'Developed alogrithms to model all 12 regular and semi regular tesselations found in nature using Power Diagrams',
                                'Introduced randomness in seed and weight distribution to generate all possible cellular microstructures',
                                'Optimized Statistical models such as Random Forest Trees to fit geometrical properties to mechanical properties',
                                'Published Paper in Science Advances : Applied Science in Mechanics']
                               )
        
        generate_projects_list('Data Analysis w Python', 'FreeCodeCamp Course Projects',
                               ['Mean-Variance-Standard Deviation Calculator',
                                'Demographic Data Analyzer',
                                'Medical Data Visualizer',
                                'Page View Time Series Visualizer',
                                'Sea Level Predictor'
                                '[Link](https://www.freecodecamp.org/certification/JoelBenJohn/data-analysis-with-python-v7) to projects:']
                                )

if __name__ == "__main__":
        main()