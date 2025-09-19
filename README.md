# Student Dropout Prediction System

An intelligent web application built with Flask and Scikit-learn to predict the likelihood of student dropout. This system provides educators and administrators with actionable insights through an interactive dashboard, helping to identify at-risk students and facilitate timely interventions like counselling and attendance tracking.

##  Features

  - **Dual SVM Prediction Models**: Utilizes two distinct Support Vector Machine (SVM) models for predictions based on either 1-semester or 2-semester student data.
  - **Secure User Authentication**: A complete login/register system to protect access to the dashboard.
  - **Interactive Dashboard**: A dynamic dashboard built with Chart.js to visualize key metrics, including overall risk distribution, risk breakdown by course, and academic performance of high-risk students.
  - **Detailed Student Profiles**: Drill down into individual student reports showing academic, demographic, financial, and family details.
  - **Counselling Management**: Assign at-risk students to a counselling schedule and automatically notify parents via email.
  - **Attendance Tracking**: A dedicated module to update weekly, subject-wise attendance, with automatic email alerts for low attendance.
  - **Data Export**: Download prediction results and student data as a formatted and color-coded Excel (`.xlsx`) report.
  - **Bilingual & Theming**: Supports both English and Hindi, along with a user-friendly dark/light mode toggle.

-----

##  Tech Stack

| Backend                               | Frontend                             | Machine Learning / Data             |
| ------------------------------------- | ------------------------------------ | ----------------------------------- |
| Python / Flask                        | HTML / CSS                           | Scikit-learn                        |
| Flask-Login (Authentication)          | Tailwind CSS                         | Pandas                              |
| Flask-Session (Filesystem Sessions)   | Vanilla JavaScript                   | Openpyxl                            |

-----

##  Data File Requirements

For the prediction to work correctly, your uploaded `.csv` or `.xlsx` file must contain specific column headers.

**Important Notes:**

  * The file must **not** contain a column named `Target`.
  * For features like student details and email notifications, you **must** also include `Student ID`, `Student Name`, and `Parent Mail` columns.
  * The application homepage includes a detailed "Data File Reference Guide" explaining the integer codes required for categorical data.

### **For the 1-Semester Model**

```
- Marital status
- Course
- Daytime/evening attendance
- Previous qualification
- Previous qualification (grade)
- Mother's qualification
- Father's qualification
- Mother's occupation
- Father's occupation
- Displaced
- Educational special needs
- Debtor
- Tuition fees up to date
- Gender
- Scholarship holder
- Age at enrollment
- International
- Curricular units 1st sem (credited)
- Curricular units 1st sem (enrolled)
- Curricular units 1st sem (evaluations)
- Curricular units 1st sem (approved)
- Curricular units 1st sem (grade)
- Curricular units 1st sem (without evaluations)
```

### **For the 2-Semester Model**

This requires all columns from the 1-Semester model **plus** the following six columns:

```
- Curricular units 2nd sem (credited)
- Curricular units 2nd sem (enrolled)
- Curricular units 2nd sem (evaluations)
- Curricular units 2nd sem (approved)
- Curricular units 2nd sem (grade)
- Curricular units 2nd sem (without evaluations)
```

-----

##  Setup and Installation

### 1\. Prerequisites

  - Python 3.8+
  - `pip` (Python package installer)

### 2\. Clone the Repository

```bash
git clone https://github.com/your-username/student-dropout-prediction.git
cd student-dropout-prediction
```

### 3\. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4\. Install Dependencies

Create a `requirements.txt` file with the following content:

```
Flask
pandas
scikit-learn
openpyxl
Flask-Login
Flask-Session
Werkzeug
```

Then, run the installation command:

```bash
pip install -r requirements.txt
```

### 5\. Configure Email for Notifications

The application uses `smtplib` with Gmail. For this to work, you must configure your credentials in `app.py`.

  - Update `MAIL_USERNAME` with your Gmail address.
  - For `MAIL_PASSWORD`, use a **Google App Password**.

<!-- end list -->

```python
# In app.py
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_16_character_app_password'
```

### 6\. Place Training Data

Ensure the training datasets `Data(Nosem).csv` and `Data(Sem-2).csv` are in the project's root directory.

-----

##  Running the Application & Usage

### 1\. Start the Server

Execute the `app.py` script to start the Flask development server.

```bash
python app.py
```

The application will be accessible at **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

### 2\. User Registration

  - Create a new account using the "Register" link. The default credentials for an initial user are:
      - **Username**: `teacher`
      - **Password**: `password`

### 3\. Predict Student Data

  - Navigate to the homepage and select the data type (1 or 2 Semesters).
  - Upload your `.csv` or `.xlsx` student data file.
  - Click "Predict Dropout Risk" to be redirected to the dashboard.

### 4\. Analyze & Manage

  - On the dashboard, review summary statistics and charts.
  - Click on a student to view their detailed profile.
  - Use the "Counselling Schedule" and "Attendance Page" links to manage interventions.

-----

##  How It Works

1.  **Model Training**: On application startup, two distinct SVM models are trained using the provided `.csv` files. Data is preprocessed using `StandardScaler` and `LabelEncoder`, and the trained models are stored in memory.
2.  **Prediction Workflow**: A user uploads a data file. The Flask backend processes it with Pandas, applies the pre-fitted scalers and encoders, and uses the appropriate SVM model to calculate the dropout probability for each student.
3.  **Dynamic Frontend**: The frontend uses the `fetch` API to call various API endpoints in Flask. This allows for dynamic loading of dashboard data and charts without page reloads, creating a smooth user experience.

-----

##  Project Structure

```
.
├── app.py                      # Main Flask application file
├── Data(Nosem).csv             # Training data for the 1-semester model
├── Data(Sem-2).csv             # Training data for the 2-semester model
├── templates/
│   ├── base.html               # Base template with header and styles
│   ├── index.html              # Homepage for file upload
│   ├── dashboard.html          # Main dashboard for visualizations
│   ├── student_detail.html     # Detailed view for a single student
│   ├── counselling.html        # Counselling scheduling page
│   ├── attendance.html         # Attendance management page
│   ├── login.html              # Login page
│   └── register.html           # Registration page
└── ...
```

-----

##  License

This project is open source and available under the MIT License.