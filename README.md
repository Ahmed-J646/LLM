# Chatbot Fine-Tuning & Deployment 🚀

This project fine-tunes a pre-trained language model using **Parameter-Efficient Fine-Tuning (PEFT)** techniques, containerizes it with Docker, and deploys it using **FastAPI** (backend) and **Streamlit** (frontend).  

## 📌 Features  
✅ Fine-tune a chatbot using **LoRA, Adapters, Prefix-Tuning, or BitFit**  
✅ Deploy the chatbot API using **FastAPI**  
✅ Create a user-friendly **Streamlit frontend**  
✅ Containerize the app using **Docker**  

## 🛠️ Tech Stack  
- **Python**  
- **Hugging Face Transformers** (Model Fine-Tuning)  
- **PEFT Library** (Efficient Model Training)  
- **FastAPI** (Backend API)  
- **Streamlit** (Frontend UI)  
- **Docker** (Containerization)  

## 🏗️ Setup Instructions  

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/chatbot-finetuning.git
cd chatbot-finetuning
2️⃣ Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Fine-Tune the Model
Run the script to fine-tune the chatbot using LoRA (or another PEFT technique).


python finetune.py

5️⃣ Run FastAPI Backend
uvicorn app:app --host 0.0.0.0 --port 8000

6️⃣ Run Streamlit Frontend
streamlit run frontend.py

7️⃣ Build & Run Docker Container
docker build -t chatbot-app .
docker run -p 8000:8000 chatbot-app
🎯 Endpoints
FastAPI Backend: http://localhost:8000
Streamlit UI: http://localhost:8501
📌 Future Improvements
Add multi-turn conversation memory
Deploy using Kubernetes or AWS Lambda
🚀 Happy Coding!
