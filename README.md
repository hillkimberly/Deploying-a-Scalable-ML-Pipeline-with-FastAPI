# 🚀 Deploying a Scalable ML Pipeline with FastAPI

This project demonstrates how to build, train, and deploy a machine learning pipeline using **FastAPI** and **MLflow**. It includes reusable components for model training, inference, evaluation, and deployment via an API. The goal is to deliver real-time predictions through a reliable and scalable interface.

---

## 📌 Project Highlights

- Trains a classification model using U.S. Census Income Data
- Logs models and artifacts with **MLflow**
- Serves predictions through a **FastAPI** REST API
- Evaluates model fairness using **performance on categorical slices**
- CI/CD integrated using **GitHub Actions**
- Includes automated testing with **pytest** and code linting with **flake8**

---

## 📂 Folder Structure



├── main.py # FastAPI application
├── train_model.py # Train and save model artifacts
├── inference.py # Run model inference
├── performance_on_categorical_slice.py # Evaluate performance on slices
├── model/
│ ├── model.pkl
│ ├── encoder.pkl
│ └── label_binarizer.pkl
├── tests/ # Unit tests
├── slice_output.txt # Output of slice performance analysis
├── requirements.txt
├── .github/workflows/ # GitHub Actions workflow files
└── README.md


---

## 🔍 Dataset

This project uses publicly available data from the [U.S. Census Bureau](https://www.census.gov/).  
The dataset includes demographic and employment features, and the task is to classify whether an individual's income exceeds $50K per year.

Example features:
- Age, education, marital status
- Occupation, hours-per-week, sex, native country

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
git clone https://github.com/hillkimberly/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git
cd Deploying-a-Scalable-ML-Pipeline-with-FastAPI

2.  Install dependencies
   pip install -r requirements.txt

3. Train the model
   python train_model.py

4. Start the FastAPI Server
   uvicorn main:app --reload

Access the interactive Swagger UI at http://127.0.0.1:8000/docs
```

🧪 Example API Input
POST /predict
#json

{
  "age": 38,
  "workclass": "Private",
  "education": "Masters",
  "marital_status": "Single",
  "occupation": "Tech-support",
  "relationship": "Not-in-family",
  "race": "White",
  "sex": "Female",
  "hours_per_week": 40,
  "native_country": "United-States"
}

Response:
#json
{
  "prediction": "<=50K"
}

✅ Testing & CI/CD
To run tests:
#bash
pytest
flake8 .

This project includes a GitHub Actions workflow for automatic linting and testing on every push.

👩‍💻 Author
Kimberly Hill
📌 GitHub Portfolio - https://hillkimberly.github.io/
🔗 LinkedIn - https://www.linkedin.com/in/kimberlyhill-dataanalyst/

📄 License
This project is for educational and portfolio purposes using publicly available data.
