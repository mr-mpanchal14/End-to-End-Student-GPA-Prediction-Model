
# End-to-End-Student-GPA-Prediction-App

In this project, I have explored various factors influencing Student's Performance by building various Regression Machine Learning Models like  `Multiple Linear Regression, Ridge, CatBoost Regressor, XGBoost Regressor and more` and conducted in-depth data preprocessing and exploratory analysis on the `Student's Performance Dataset` including student demographics, parental involvement, and academic performance. I have also engineered features to enhance model performance. Successfully predicted `Student GPA` with `Linear Regression`, achieving an impressive accuracy of `95.32%`.

To expand this project's utility, I transformed the model into a modular Python structure. I then created a Flask web application to serve the model, containerized it using Docker for efficient deployment, and established a CI/CD pipeline with GitHub Actions to automate the deployment process on Amazon AWS.




## About the Dataset

The dataset comprises detailed information on 2,392 high school students. It offers a comprehensive view of student life, including demographics, study habits, parental involvement, extracurricular activities, and academic performance. The target variable, GradeClass, categorizes students based on their grades, making it a valuable resource for educational research, predictive modeling, and statistical analysis.

>### [DATASET LINK](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)

### Columns in Dataset:

1. `Student ID ->`                           A unique identifier assigned to each student (1001 to 3392).
2. `Age ->`	        The age of the students ranges from 15 to 18 years.
3. `Gender ->`	        Gender of the students, where 0 represents Male and 1 represents Female.
4. `Ethnicity ->`                              The ethnicity of the students, coded as follows: 0: Caucasian 1: African American 2: Asian 3: Other
5. `Parental Education ->`               The education level of the parents, coded as follows: 0: None 1: High School 2: Some College 3: Bachelor's 4: Higher
6. `Study Time Weekly ->`                           Weekly study time in hours, ranging from 0 to 20.
7. `Absences ->`                                  Number of absences during the school year, ranging from 0 to 30.
8.  `Tutoring ->`                         Tutoring status, where 0 indicates No and 1 indicates Yes.
9. `Parental Support ->`        The level of parental support, coded as follows: 0: None 1: Low 2: Moderate 3: High 4: Very High
10. `Extracurricular ->`                         Participation in extracurricular activities, where 0 indicates No and 1 indicates Yes.
11. `Sports ->`                           Participation in sports, where 0 indicates No and 1 indicates Yes.
12. `Music ->`                       Participation in music activities, where 0 indicates No and 1 indicates Yes.
13. `Volunteering ->`                  Participation in volunteering, where 0 indicates No and 1 indicates Yes.

### Target variable:

1. `GPA ->`                           Grade Point Average on a scale from 2.0 to 4.0, influenced by study habits, parental involvement, and extracurricular activities.

## Built With

- Numpy
- Pandas
- Matplotlib
- Seaborn
- Scipy
- Scikit-learn
- Catboost
- XGboost
- Flask
- Docker
- Amazon AWS
## Getting Started

This will help you understand how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

## Installation steps

### Option 1: Installation from Github

Follow these steps to install and set up the project directly from the GitHub repository:

1. Clone the Repository

- Open your terminal or command prompt.
- Navigate to the directory where you want to install the project.
- Run the following command to clone the GitHub repository: 

##
        git clone https://github.com/mr-mpanchal14/End-to-End-Student-GPA-Prediction-Model.git

2. Create a Virtual Environment (Optional but recommended)

- It's a good practice to create a virtual environment to manage project dependencies. Run the following command: 

##
        conda create -p <Environment_Name> python==<python version> -y

3. Activate the Virtual Environment (Optional)

- Activate the virtual environment based on your operating system: 

##
        conda activate <Environment_Name>/

4. Install Dependencies

-Navigate to the project directory: 
##
        cd [project_directory]
- Run the following command to install project dependencies: 
##
        pip install -r requirements.txt

5. Run the Project

- Start the project by running the appropriate command. 
##
        python app.py

6. Access the Project

- Open a web browser or the appropriate client to access the project and set port to .8080
##
        localhost:8080


### Option 2: Installation from DockerHub

If you prefer to use Docker, you can install and run the project using a Docker container from DockerHub:

1. Pull the Docker Image
- Open your terminal or command prompt.
- Run the following command to pull the Docker image from DockerHub: 
##
        docker pull mpanchal14/student-gpa-prediction-model

2. Run the Docker Container
- Start the Docker container by running the following command, and mapping any necessary ports: 
##
        docker run -d -p 8080:8080 mpanchal14/student-gpa-prediction-model:latest

3. Access the Project
- Open a web browser or the appropriate client to access the project.
## License

Distributed under the MIT License. See `License.txt` for more information.




## Contact

Mann Panchal - @panchalmann541@gmail.com \
Visit my [Kaggle](https://www.kaggle.com/mannpanchal) profile. Or connect with me on [LinkedIn](https://www.linkedin.com/in/mann-panchal-13a22a202/)


