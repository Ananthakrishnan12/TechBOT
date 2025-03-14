## **TechBOT - IT Education Chatbot**
**A chatbot that provides IT learning resources, course recommendations, interview tips, and more using LSTM, FastAPI, and a frontend built with HTML & CSS.**

### 🚀 **Project Overview**
TechBOT is an AI-powered chatbot designed to assist users in the IT industry by answering queries about programming, certifications, job opportunities, and interview tips. It uses **LSTM** for intent classification, **FastAPI** for backend deployment, and an interactive **HTML/CSS frontend** for user interaction.

---

## 📌 **Features**
✅ **IT Course Recommendations** - Suggests IT courses & certifications.  
✅ **Programming Guidance** - Tips to learn Python, coding, and improving programming skills.  
✅ **Job Opportunities** - Provides insights into high-demand IT jobs.  
✅ **Interview Preparation** - Helps with coding interview strategies and system design concepts.  
✅ **LSTM-based Intent Recognition** - Uses deep learning (LSTM) for chatbot responses.  
✅ **FastAPI Backend** - API-driven chatbot with real-time responses.  
✅ **Frontend with HTML/CSS** - Interactive web-based chatbot UI.  

---

## 🛠️ **Tech Stack**
### **Backend**
- **Python 3.12.2**  
- **TensorFlow/Keras (LSTM model)**  
- **FastAPI**  
- **Joblib (for saving tokenizer & label encoder)**  

### **Frontend**
- **HTML, CSS**  
- **JavaScript (to communicate with FastAPI backend via AJAX)**  

### **Deployment**
- **FastAPI Server** (Backend API)  
- **HTML/CSS Frontend** (User Interface)  

---

## 🛠️ **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Ananthakrishnan12/TechBOT.git
cd TechBOT
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**  
```sh
python -m venv Techbot
source Techbot/bin/activate  # For Linux/Mac
Techbot\Scripts\activate     # For Windows
pip install -r requirements.txt
```

### **3️⃣ Train the LSTM Model & Save Artifacts**  
```sh
python train_model.py  # Train the chatbot model
```
This will generate:  
✅ `chatbot.h5` - Trained LSTM model  
✅ `tokenizer.joblib` - Tokenizer for text preprocessing  
✅ `label_encoder.joblib` - Label encoder for intent classification  

---

## 🚀 **Run the Chatbot API**  
```sh
uvicorn main:app --reload
```
The FastAPI server will start at **http://127.0.0.1:8000/**  

✅ Visit **http://127.0.0.1:8000/docs** for API documentation  

---


DEMO : ![Chatbot Demo](https://github.com/Ananthakrishnan12/TechBOT/blob/main/Techbot.gif)


