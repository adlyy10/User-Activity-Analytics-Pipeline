# User-Activity-Analytics-Pipeline

## Project Overview

This project is a beginner-friendly ETL (Extract, Transform, Load) pipeline built using Python and Pandas.

The pipeline reads user activity data from CSV files, cleans and validates the data, performs transformations and aggregations, and exports analytics reports as CSV files.

---

## Technologies Used

- Python
- Pandas

---

## Features

- Extract data from CSV files
- Validate missing and invalid data
- Clean timestamps and null values
- Merge multiple datasets
- Generate analytics reports
- Export processed results to CSV files

---

## Project Structure

```text
user-activity-pipeline/

│
├── data/
│   ├── activity.csv
│   ├── users.csv
│   └── devices.csv
│
├── output/
│   ├── top_countries.csv
│   ├── most_used_devices.csv
│   └── country_device_activity.csv
│
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## Generated Reports

The pipeline generates:

- Actions per country
- Most used devices
- Activity by country and device
- Most active country

---

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the pipeline

```bash
python pipeline.py
```

---

## Learning Goals

This project was created to practice:

- Pandas fundamentals
- ETL pipeline structure
- Data cleaning
- Data transformation
- Data aggregation
- CSV file handling
- Modular Python functions

---

## Future Improvements

- Add logging system
- Add automated tests
- Add database integration
- Add scheduling support
