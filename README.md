# **Business Information Systems - Data Analytics Lab Portfolio**
This repository contains a comprehensive collection of lab projects for the **Business Information Systems** course. The labs demonstrate practical implementation of key BIS concepts through hands-on data analytics, system integration, and business intelligence projects.

## 📊 **Course Focus Areas Implemented:**
- **Business Analytics & Predictive Modeling** - Linear regression for sales/profit prediction
- **Customer Segmentation & Clustering** - K-means clustering for market analysis
- **ETL Processes & Database Integration** - SQL Server connectivity and data management
- **Process Automation** - Batch scripting for system workflows
- **Strategic Data Analysis** - SQL queries and stored procedures for business intelligence
- **Data Visualization** - Power BI dashboards for financial institution reporting

## 💻 **Lab Projects Overview:**

### **Lab 2: Linear Regression for Predicting Profit and Transactions**
- **Objective:** Apply linear regression to predict Profit and Transactions based on Sales data
- **Technologies:** Python, pandas, scikit-learn, matplotlib
- **Key Features:** Missing value prediction, R² scoring, dual visualization
- **Output:** `lab2_predictions.png`, `Lab_2_Predicted_Output.xlsx`

### **Lab 3: K-Means Clustering on Customer Sales Data**
- **Objective:** Segment customers into groups based on sales and profit data
- **Technologies:** K-Means clustering, Elbow Method, StandardScaler
- **Key Features:** Optimal cluster determination (k=3), centroid visualization
- **Output:** `cluster_plot.png`, `elbow_plot.png`, `Lab_3_output.txt`

### **Lab 4: ETL Pipeline for Banking Statistics**
- **Objective:** Extract, cleanse, and load monthly banking statistics into SQL Server
- **Technologies:** Python, SQLAlchemy, pyodbc, SQL Server
- **Key Features:** Automated data import, column standardization, temporal tracking
- **Source Data:** NRB Nepal monthly banking statistics (Jestha, 2082)

### **Lab 5: Automation with Batch Scripting**
- **Objective:** Automate application launch and service management
- **Technologies:** Windows Batch Scripting, Task Scheduler
- **Key Features:** MSSQL service monitoring, application autostart, file validation
- **Automated Apps:** Chrome, VS Code, SSMS, Python lab files

### **Lab 6: SQL Data Aggregation & Stored Procedures**
- **Objective:** Aggregate, analyze, and automate financial institution reporting
- **Technologies:** SQL Server, T-SQL, Stored Procedures
- **Key Features:** 10 analytical queries combined into automated reporting procedure
- **Tables Created:** Province summaries, high-class branches, population leaders

### **Lab 7: Power BI Data Visualization**
- **Objective:** Transform and visualize financial institution data
- **Technologies:** Power BI, Power Query, SQL Server Integration
- **Key Features:** 5 visualization types, multi-source data integration
- **Visualizations:** Bar charts, pie charts, line charts, maps, stacked columns

## 🛠️ **Technology Stack:**
- **Programming:** Python 3.x, SQL (T-SQL), Batch Scripting
- **Libraries:** pandas, scikit-learn, matplotlib, SQLAlchemy, pyodbc
- **Databases:** Microsoft SQL Server
- **Visualization:** Power BI Desktop, matplotlib
- **Tools:** SSMS, VS Code, Windows Task Scheduler
 
## 📁 **Repository Structure:**
```
bis-data-analytics-labs/
├── Lab_2/                    # Linear Regression & Prediction
│   ├── Lab_2.py
│   ├── Lab_2_Data.csv
│   ├── lab2_predictions.png
│   └── Lab_2_Predicted_Output.xlsx
├── Lab_3/                    # Customer Segmentation (K-Means)
│   ├── Lab_3.py
│   ├── Lab_3_Data.txt
│   ├── Lab_3_output.txt
│   ├── cluster_plot.png
│   └── elbow_plot.png
├── Lab_4/                    # ETL & SQL Server Integration
│   ├── Lab_4.py
│   ├── Monthly_statistics.xlsx
│   └── Monthlystatistics.xlsx
├── Lab_5/                    # Automation & Scheduling
│   └── lab_5.bat
├── Lab_6/                    # SQL Queries & Stored Procedures
│   ├── Lab6.sql
│   └── Lab6_1.sql
├── Lab_7/                    # Power BI Visualization
│   └── (Power BI report files)
├── Documentation/            # Lab Reports
│   ├── BIS Lab 2.pdf
│   ├── BIS Lab 3.pdf
│   ├── BIS Lab 4.pdf
│   ├── BIS Lab 5.pdf
│   ├── BIS Lab 6.pdf
│   └── BIS Lab 7.pdf
├── images/                   # Generated visualizations
│   ├── cluster_plot.png
│   ├── elbow_plot.png
│   └── lab2_predictions.png
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## **🚀 Getting Started:**
### Prerequisites:
1. Python 3.x with pip
2. Microsoft SQL Server
3. Power BI Desktop (for Lab 7)
4. Required Python libraries: pip install -r requirements.txt

### **Installation:**
##### Clone the repository
git clone https://github.com/yourusername/bis-data-analytics-labs.git
cd bis-data-analytics-labs

##### Install Python dependencies
pip install -r requirements.txt

## 📈 **Learning Outcomes:**
Through these labs, students gain practical experience in:
- Implementing predictive analytics for business forecasting
- Applying machine learning algorithms for customer segmentation
- Building automated ETL pipelines for data integration
- Creating business intelligence reports with SQL and Power BI
- Developing automation scripts to streamline workflows
- Transforming raw data into actionable business insights

## 🔗 **Data Sources:**
- **Customer Sales Data:** Synthetic dataset for regression and clustering
- **Banking Statistics:** Nepal Rastra Bank monthly reports (Jestha, 2082)
- **Financial Institution Data:** District-wise branch distribution across Nepal

## 📚 **Course Alignment:**
These labs align with BIS course objectives by demonstrating:
- Business analytics application in real-world scenarios
- Strategic information systems for competitive advantage
- Data-driven decision making processes
- Integration of SCM, CRM, and ERP concepts through data analysis
- Cloud computing and automation infrastructure principles



*This portfolio showcases the practical application of Business Information Systems concepts through hands-on data analytics projects, bridging theoretical knowledge with real-world implementation.*
