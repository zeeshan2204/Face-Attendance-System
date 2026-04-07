#  Face Attendance System  

AI-powered Face Recognition based Attendance System with Live Dashboard  

---

##  Features

- Real-time face detection & recognition  
- Automatic attendance marking  
- Duplicate attendance prevention  
- Live dashboard using Flask  
- CSV-based attendance storage  
- Person-wise attendance tracking  

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python |
| Computer Vision | OpenCV |
| Face Recognition | face_recognition |
| Backend | Flask |
| Data Handling | Pandas |
| Frontend | HTML + CSS |

---

## 📂 Project Structure

```bash
Face-Attendance-System/
│── capture_faces.py      # Capture images from webcam
│── trainfaces.py         # Train face recognition model
│── main.py               # Run face detection & attendance
│── app.py                # Flask backend server
│── dashboard.html        # Web dashboard UI
│── attendance.csv        # Attendance records
│── encodings.pkl         # Trained face data
│── requirements.txt      # Dependencies
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/zeeshan2204/Face-Attendance-System.git
cd Face-Attendance-System

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Capture faces
python capture_faces.py

# 5. Train model
python trainfaces.py

# 6. Run attendance system
python main.py

# 7. Start dashboard (new terminal)
python app.py

# 8. Open browser
http://127.0.0.1:5000
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | `/` | Dashboard UI |
| GET | `/api/attendance` | Get attendance data |
| GET | `/api/stats` | Get attendance statistics |

---

## 🔐 How It Works

1. Capture face images using webcam  
2. Train model using face encodings  
3. Detect & recognize faces in real-time  
4. Mark attendance in CSV file  
5. Display records on dashboard  

---

## ⚡ Future Improvements

- Login system (Admin/User)  
- Export attendance to Excel  
- Mobile camera support  
- Cloud deployment  
- Accuracy optimization  

---

## 👨‍💻 Developer

**Zeeshan**  
GitHub: https://github.com/zeeshan2204  

---

## 📄 License

MIT License — Free to use
