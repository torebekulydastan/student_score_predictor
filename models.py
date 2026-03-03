from pydantic import BaseModel,Field
from typing import Literal


class input_features(BaseModel):
    Hours_Studied:int = Field(ge=0,description='how many hours students studyed')
    Attendance:int =Field(ge=0,description='how many classes attended')
    Parental_Involvement:Literal['Low','Medium','High'] = Field(description='the parental involvment')
    Access_to_Resources:Literal['Low','Medium','High']
    Extracurricular_Activities:Literal['Yes','No']
    Sleep_Hours:int = Field(gt=0,lt=24,description='time of sleep for a day')
    Previous_Scores:int = Field(ge= 0,description='scores of previous exam')
    Motivation_Level:Literal['Low','Medium','High']
    Internet_Access:Literal['Yes','No']
    Tutoring_Sessions:int = Field(ge= 0)
    Family_Income:Literal['Low','Medium','High']
    Teacher_Quality:Literal['Low','Medium','High']
    School_Type:Literal['Public','Private']
    Peer_Influence:Literal['Positive','Neutral','Negative']
    Physical_Activity:int =Field(ge= 0)
    Learning_Disabilities:Literal['Yes','No']
    Parental_Education_Level:Literal['High School','College','Postgraduate']
    Distance_from_Home:Literal['Near','Moderate','Far']
    Gender:Literal['Male','Female']
    class Config:
        extra = "forbid"
        str_strip_whitespace = True
        json_schema_extra = {
            "example": {
                "Hours_Studied": 5,
                "Attendance": 90,
                "Parental_Involvement": "High",
                "Access_to_Resources": "Medium",
                "Extracurricular_Activities": "Yes",
                "Sleep_Hours": 7,
                "Previous_Scores": 75,
                "Motivation_Level": "High",
                "Internet_Access": "Yes",
                "Tutoring_Sessions": 2,
                "Family_Income": "Medium",
                "Teacher_Quality": "High",
                "School_Type": "Public",
                "Physical_Activity": 3,
                "Learning_Disabilities": "No",
                "Parental_Education_Level": "College",
                "Distance_from_Home": "Near",
                "Gender": "Male",
                'Peer_Influence':'Positive'
            }
        }

class prediction(BaseModel):
    exam_score: float = Field(..., example=100)
    model_version: str = "1.0"