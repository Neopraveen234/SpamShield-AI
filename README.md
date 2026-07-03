# 🛡️ SpamShield AI

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikitlearn)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Version](https://img.shields.io/badge/Version-1.0-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

<p align="center">

### AI-Powered SMS Spam Detection using Machine Learning & NLP

Detect spam messages with confidence scores, AI explanations, keyword detection, prediction history, and interactive analytics.

</p>

---

# 📖 Project Overview

SpamShield AI is a Machine Learning web application that classifies SMS messages as **Spam** or **Ham** using **Natural Language Processing (NLP)**.

The project combines **TF-IDF Vectorization**, a **Linear Support Vector Machine (Linear SVM)** classifier, and an interactive **Streamlit** interface to deliver fast and reliable spam detection.

In addition to prediction, the application provides:

- AI-powered explanations
- Spam & Ham confidence scores
- Risk level analysis
- Suspicious keyword detection
- Prediction history
- Interactive statistics dashboard

---

# ✨ Features

### 🤖 Machine Learning

- Linear SVM Classifier
- TF-IDF Vectorization
- NLP Text Processing
- Fast Prediction Engine

### 🛡️ Spam Analysis

- Spam Probability
- Ham Probability
- Confidence Score
- Risk Level
- AI Explanation
- Keyword Detection

### 📊 Dashboard

- Prediction History
- Search & Sort
- Download History
- Statistics Dashboard
- Daily Prediction Trends

### 💾 Database

- SQLite Integration
- Automatic Prediction Storage

---

# 📸 Application Screenshots

## 🏠 Home

![Home](screenshots/01_Home.png)

---
## 🚨 Spam Prediction

![Spam](screenshots/02_Spam_Prediction_1.png)

---
## 📜 Prediction History

![History](screenshots/04_Prediction_History.png)
---
## 📊 Statistics Dashboard

![Statistics](screenshots/05_Statistics_1.png)

---
## 🧠 About Model

![About Model](screenshots/07_About_Model_1.png)
---
## 👨‍💻 About Developer

![Developer](screenshots/09_About_Developer_1.png)
---
# 🧠 Machine Learning Pipeline

```text
SMS Message
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Linear SVM Model
      │
      ▼
Spam / Ham Prediction
      │
      ▼
AI Explanation
      │
      ▼
SQLite Database
      │
      ▼
Statistics Dashboard
```

---

# 📂 Project Structure

```text
SpamShield-AI/
│
├── screenshots/
├── assets/
├── data/
├── database/
├── models/
├── src/
│   ├── pages/
│   ├── predict.py
│   ├── preprocess.py
│   ├── history.py
│   ├── database.py
│   ├── highlight.py
│   ├── explain.py
│   ├── keywords.py
│   ├── train.py
│   └── evaluate.py
│
├── tests/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
---
# 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF |
| Framework | Streamlit |
| Database | SQLite |
| Data Analysis | Pandas |
| Visualization | Plotly |
| Model Storage | Joblib |

---
# ⚙️ Installation
Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/SpamShield-AI.git
```

Navigate to the project folder:

```bash
cd SpamShield-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows (CMD)**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---
# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```
---
# 🚀 Usage
1. Launch the application.
2. Enter an SMS message.
3. Click **Predict Message**.
4. View:
   - Spam/Ham prediction
   - Confidence score
   - Risk level
   - AI explanation
   - Suspicious keywords
5. Browse previous predictions in **Prediction History**.
6. Analyze trends in the **Statistics Dashboard**.
---
# 📊 Model Information

| Item | Value |
|------|-------|
| Algorithm | Linear Support Vector Machine |
| Feature Extraction | TF-IDF |
| Dataset | SMS Spam Collection Dataset |
| Prediction | Spam / Ham |
| Storage | SQLite Database |

--
# 📈 Application Modules

| Module | Description |
|---------|-------------|
| 🏠 Home | Predict Spam or Ham messages |
| 📜 Prediction History | View and search previous predictions |
| 📊 Statistics | Visualize prediction analytics |
| 🧠 About Model | ML model information |
| 👨‍💻 About Developer | Project and developer details |
---
# 🔮 Future Scope

Planned improvements for future versions include:

- 📱 Android Application
- 📩 Live SMS Detection
- 🔐 Sender Verification
- 🤖 Improved Machine Learning Model
- 🌍 Multi-language Support
- ☁️ Cloud Deployment
- 🔄 Continuous Model Retraining
---
# 👨‍💻 About the Developer

SpamShield AI was developed as an end-to-end Machine Learning project to demonstrate practical skills in:

- Machine Learning
- Natural Language Processing
- Data Analytics
- Streamlit Development
- SQLite Database Integration
- Interactive Dashboard Design

This project showcases the complete ML lifecycle, from data preprocessing and model training to deployment as an interactive web application.
---
# 📚 Learning Outcomes

This project demonstrates:

- Data Preparation
- Feature Engineering
- Machine Learning Model Development
- Model Evaluation
- Explainable AI
- Database Management
- Data Visualization
- Interactive Application Development
---
# 🤝 Acknowledgements

This project uses the following open-source technologies:

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- SQLite

Dataset:

- SMS Spam Collection Dataset

Special thanks to the open-source community for providing the tools and resources that made this project possible.
---
# 📜 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Learn from
- Share

Please provide appropriate attribution if you redistribute this project.
---
# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🐛 Report issues
- 💡 Suggest new features

Your feedback and contributions are always welcome.
---
# 📬 Contact

For questions or suggestions, feel free to open an issue in this repository.
---
<p align="center">

## 🛡️ SpamShield AI v1.0

**AI-Powered SMS Spam Detection System**

Built with ❤️ using **Python • Streamlit • Scikit-learn • SQLite**
</p>