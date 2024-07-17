import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")

            model = load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")

            data_scaled = preprocessor.transform(features)
            print(data_scaled)
            
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        age:int,
        gender: str,
        race_ethnicity: str,
        parental_education:str,
        study_time_weekly: float,
        absent: int,
        tutor: str,
        parental_supp:str,
        extracurr: str,
        sports: str,
        music: str,
        volunteer: str,
        ):

        gend = {"Male" : 0, "Female" : 1}
        ethnicity = {"Caucasian" : 0, "African American" : 1,"Asian" : 2,"Other" : 3}
        parent = {"None" : 0, "High School" : 1,"Some College" : 2,"Bachelor's" : 3, "Higher" : 4}
        tut = {"No" : 0, "Yes" : 1}
        parent_supp = {"None" : 0, "Low" : 1,"Moderate" : 2,"High" : 3}
        extra = {"No" : 0, "Yes" : 1}
        sprt = {"No" : 0, "Yes" : 1}
        mus = {"No" : 0, "Yes" : 1}
        volunt = {"No" : 0, "Yes" : 1}

        self.age = age
        self.gender = int(gend[gender])
        self.race_ethnicity = int(ethnicity[race_ethnicity])
        self.parental_education = int(parent[parental_education])
        self.study_time_weekly = study_time_weekly
        self.absent = absent
        self.tutor = int(tut[tutor])
        self.parental_supp = int(parent_supp[parental_supp])
        self.extracurr = int(extra[extracurr])
        self.sports = int(sprt[sports])
        self.music = int(mus[music])
        self.volunteer = int(volunt[volunteer])

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'Age' : [self.age],
                'Gender' : [self.gender],
                'Ethnicity' : [self.race_ethnicity],
                'ParentalEducation' : [self.parental_education],
                'StudyTimeWeekly' : [self.study_time_weekly],
                'Absences' : [self.absent],
                'Tutoring' : [self.tutor],
                'ParentalSupport' : [self.parental_supp],
                'Extracurricular' : [self.extracurr],
                'Sports' : [self.sports],
                'Music' : [self.music],
                'Volunteering' : [self.volunteer],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)