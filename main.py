from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
import random


# Load trained model and Preprocessing file..
model=tf.keras.models.load_model(r"E:\Github\NLP\chatbot.h5")
tokenizer=joblib.load(r"E:\Github\NLP\tokenizer.joblib")
label_encoder=joblib.load(r"E:\Github\NLP\label_encoder.joblib")
responses={
    "greeting":["Hello! How can I assist you with IT learning?", "Hi there! How can I help you today?"],
    "course_recommendation":[
                "It depends on your interest! For web development, try HTML, CSS, and JavaScript. For Data Science, try Python and Machine Learning.",
                "Some popular certifications include AWS Certified Solutions Architect, Google Cloud Engineer, and CompTIA Security+."
            ],
    "programming_help":[
        "Start with basic syntax and practice problems on platforms like LeetCode and HackerRank.",
                "You can take online courses from Coursera, Udemy, or freeCodeCamp."
    ],
    "job_opportunities":[
        "Some in-demand IT jobs include Software Developer, Data Scientist, Cybersecurity Analyst, and Cloud Engineer.",
                "To get a job in IT, build projects, learn relevant skills, and create a strong LinkedIn and GitHub profile."
    ],
    "interview_tips":[
        "Practice coding problems on LeetCode, understand data structures and algorithms, and revise system design concepts.",
                "Mock interviews and real-world projects can help boost confidence in IT interviews."
    ],
    "certification_info":[
        "AWS Certification helps in cloud computing jobs and is valuable in the IT industry.",
                "Google Cloud certifications are beneficial if you're interested in cloud engineering roles.",
                "CompTIA Security+ is great for cybersecurity careers."
    ],
    "goodbye":[
        "Goodbye! Happy learning!", "See you soon! Keep coding."
    ]
}

max_length=25

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class UserInput(BaseModel):
    message:str
    
    
@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/chat/")
def techbot(user_input:UserInput):
    text=user_input.message.lower()

    seq=tokenizer.texts_to_sequences([text])
    padded=pad_sequences(seq,maxlen=max_length,padding="post")
    prediction=model.predict(padded)

    tag=label_encoder.inverse_transform([np.argmax(prediction)])[0]
    return {"response":random.choice(responses.get(tag,["Sorry, I didn't understand that."]))}