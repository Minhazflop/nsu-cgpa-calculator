# 🎓 NSU CGPA Calculator

A sleek and user-friendly Streamlit web app that helps **North South University (NSU)** students calculate their **updated CGPA** and **semester GPA** based on the official grading policy.

![Streamlit App Screenshot](https://img.shields.io/badge/Streamlit-App-brightgreen?logo=streamlit)

---

## 🚀 Features

- 📌 Input your **current CGPA** and **total completed credits**
- ➕ Add as many courses as you want using the **"Add Course"** button
- 📝 Choose grades from NSU's official grading scale
- 🧮 Select valid credit hours: `1.0`, `1.5`, or `3.0`
- 📊 View:
  - Your **semester CGPA**
  - Your **updated overall CGPA**
  - Your **total credit count**

---

## 🏫 NSU Grading Policy Used

| Grade | Point |
|-------|-------|
| A     | 4.0   |
| A−    | 3.7   |
| B+    | 3.3   |
| B     | 3.0   |
| B−    | 2.7   |
| C+    | 2.3   |
| C     | 2.0   |
| C−    | 1.7   |
| D+    | 1.3   |
| D     | 1.0   |
| F     | 0.0   |

---

## 💻 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/Minhazflop/nsu-cgpa-calculator.git
   cd nsu-cgpa-calculator
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # For Windows
   source .venv/bin/activate  # For macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run cgpa_calculator.py
   ```

---

## 🌐 Deployment (Optional)

You can deploy this app to:

- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Vercel](https://vercel.com/)

---

## 📁 Project Structure

```
nsu-cgpa-calculator/
│
├── cgpa_calculator.py     # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

---

## 📄 License

This project is open-source and free to use. Attribution is appreciated. 😊

---

## 🙌 Acknowledgment

Created with ❤️ by [Minhaz Rahman](https://github.com/Minhazflop)  
Built for students of **North South University** 🇧🇩
