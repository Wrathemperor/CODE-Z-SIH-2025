# Student Dropout Prediction System

An advanced web application designed for educational institutions to proactively identify and manage students at risk of dropping out. This tool uses pre-trained Support Vector Machine (SVM) models to deliver instant predictions and provides a comprehensive suite of tools for teacher intervention.

## Features

**Dual Pre-trained Models:** Choose between prediction models trained on either 1-semester or 2-semesters of student data for flexible analysis.

**Secure Authentication**: A complete user registration and login system (Flask-Login) to protect student data.

*Interactive Dashboard*: A dynamic dashboard (Chart.js) summarizing total students, risk levels, and visualizing risk distribution by course and the academic performance of high-risk students.

**Detailed Student Profiles**: Drill down into individual student profiles to view all academic, demographic, and financial data points that contributed to their risk score.

**Counselling Management**:Schedule at-risk students for counselling sessions directly from their profile.View, manage, and reschedule appointments on a dedicated counselling calendar.Automatic email notifications to parents upon scheduling and rescheduling.

**Attendance Tracking**: Upload weekly, subject-wise attendance for all students via a simple interface on the dashboard.

**Bilingual & Theming**:Seamless English/Hindi language switching.A user-friendly Light/Dark mode theme toggle.

**Data Export**: Download a full, color-coded report of all student predictions in Excel format.


## Tech Stack
**Backend**: Flask, SQLAlchemy, Flask-Login

**Machine Learning**: Scikit-learn, Pandas, NumPy

**Frontend**: Tailwind CSS, Chart.js, Lucide Icons

**Database**: SQLite

## Required Dataset Columns

Your CSV file must contain the following columns:

- `Age`: Student age (numeric)
- `Gender`: Student gender (Male/Female)
- `Previous_Qualification_Grade`: Previous qualification grade (numeric, 0-100)
- `Admission_Grade`: Admission grade (numeric, 0-100)
- `Tuition_Fees_Up_to_Date`: Fee payment status (Yes/No)
- `Scholarship_Holder`: Scholarship status (Yes/No)
- `Displaced`: Displacement status (Yes/No)
- `Debtor`: Debt status (Yes/No)
- `Unemployment_Rate`: Regional unemployment rate (numeric)
- `Inflation_Rate`: Regional inflation rate (numeric)
- `Dropout`: Target variable (0=continue, 1=dropout)

## Setup and Installation
Follow these steps to get the application running on your local machine.

1. **Prerequisites**
Python 3.8+

pip (Python package installer)

2. **Clone the Repository Bash**

   ```git clone https://github.com/your-username/student-dropout-prediction.git
   cd student-dropout-prediction```

3. **Create a Virtual Environment**
   It's highly recommended to use a virtual environment to manage project dependencies.

   # For Windows
   ```python -m venv venv\Scripts\activate
       ```

   # For macOS/Linux
   ```python3 -m venv venv
      source venv/bin/activate
      ```

4. **Install Dependencies**
   ```Install all the required Python packages from the requirements.txt file.
      pip install Flask pandas scikit-learn openpyxl Flask-Login Flask-Session Werkzeug
      Note: You can also save this list in a requirements.txt file and run pip install -r requirements.txt.```

### Configure Email for Notifications
   ```The application uses smtplib with Gmail to send email notifications for counselling and low attendance.Open the app.py file.Locate the app.config section for mail settings.Update MAIL_USERNAME with your Gmail address.
   For MAIL_PASSWORD, it is highly recommended to use a Google App Password instead of your regular password. You can generate one here: [Google App Passwords](https://gemini.google.com/app/13708c208c9978bd#:~:text=Configure%20Email%20for,App%20Passwords.).```

### In app.py
   ```app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your_16_character_app_password' # e.g., 'zdtm bruu chis fbgz'```

### Run the Application
   ```Execute the app.py script to start the Flask development server.
   python app.py```
   The application will be accessible at http://127.0.0.1:5000.
   
## Training Data
Ensure the training datasets Data(Nosem).csv and Data(Sem-2).csv are present in the root directory of the project. The models are trained automatically when the application starts.

### Procedure
   1. Register & Login: Create a new account using the "Register" link. The default credentials for an initial user are:
         Username: teacher
         Password: password

   2.Upload Data:
      Navigate to the homepage.
      Select the data type (1 Semester or 2 Semesters) that matches your file.
      Drag and drop or browse to upload your .csv or .xlsx student data file.
      Click "Predict Dropout Risk".

   3.Analyze Dashboard: You will be redirected to the dashboard where you can view summary statistics, charts, and a table of all students with their predicted risk levels.

   4.Manage Counselling & Attendance:
      Use the "Counselling Schedule" button on the dashboard or the link on the upload page to manage counselling sessions.
      Use the "Go to Attendance Page" link on the upload page to update student attendance records.


### Project Structure
.
├── app.py                      # Main Flask application file
├── Data(Nosem).csv             # Training data for the 1-semester model
├── Data(Sem-2).csv             # Training data for the 2-semester model
├── sample_student_data.csv     # Sample data file for user to test
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

## Model Details

- **Algorithm**: Support Vector Machine (SVM) with RBF kernel
- **Preprocessing**: Automatic handling of categorical variables and feature scaling
- **Risk Levels**:
  - **High Risk**: Dropout probability > 70%
  - **Medium Risk**: Dropout probability 40-70%
  - **Low Risk**: Dropout probability < 40%

## Web Interface Features

### Upload Page
- Drag-and-drop file upload interface
- Column requirements display
- File validation

### Dashboard
- Summary statistics cards
- Model performance metrics
- High-risk student alerts
- Interactive Plotly visualizations
- Comprehensive results table


## API Endpoints

- `GET /`: Main upload page
- `POST /upload`: Handle file upload and processing
- `GET /dashboard`: Display results dashboard
- `GET /api/data`: JSON API for processed data

## Technical Specifications

- **Backend**: Flask 2.3.3
- **Machine Learning**: scikit-learn 1.3.0
- **Data Processing**: pandas 2.0.3, numpy 1.24.3
- **Visualizations**: Plotly 5.15.0, Matplotlib 3.7.2
- **Frontend**: Bootstrap 5.1.3, Font Awesome 6.0.0

## Troubleshooting

### Common Issues

1. **Module not found errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

2. **File upload errors**: Check that your CSV has all required columns with correct names

3. **Memory issues**: For large datasets, consider increasing system memory or using data sampling

4. **Port conflicts**: If port 5000 is busy, modify the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=8080)


### How It Works
   1.The application's workflow is centered around a robust backend and a dynamic frontend.

   2.Model Training: On application startup, two distinct SVM models are trained using the provided .csv files. The data is preprocessed using         StandardScaler for feature scaling and LabelEncoder for categorical variables. The trained models and scalers are stored in global variables.

   3.Prediction Workflow:
      A user uploads a student data file (.csv or .xlsx).The Flask backend processes the file using Pandas.The data is passed through a preprocessing pipeline that uses the previously fitted scalers and encoders to ensure consistency.The appropriate SVM model (model.predict_proba) is used to calculate the dropout probability for each student.

   4.A Risk_Level ('Low', 'Medium', 'High') is assigned based on the probability score.The results are stored in the user's session and displayed on the dashboard.

   5.Dynamic Frontend: The frontend uses AJAX (fetch API) to call various API endpoints (/api/...) in the Flask app. This allows for dynamic loading of dashboard data, charts, and student tables without requiring page reloads, creating a smooth user experience.

   ```

### Performance Optimization

- For datasets > 10,000 records, consider using SVM with linear kernel
- Enable data caching for repeated analysis
- Use feature selection for high-dimensional datasets

## Security Notes

- File upload is restricted to CSV format only
- Maximum file size is limited to 16MB
- Uploaded files are stored temporarily and can be cleared periodically

## License

This project is open source and available under the MIT License.
