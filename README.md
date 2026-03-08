# Latin America Socioeconomic Data Pipeline

## Project Overview

This project builds a complete data pipeline to collect, process, and analyze socioeconomic indicators from countries in Latin America.
The goal is to explore how investments in **education** and **health** relate to **GDP** across the region.

The pipeline extracts data from a public API, processes it through an ETL workflow, stores it in a PostgreSQL database, and exposes the results through an interactive dashboard.

The dashboard allows users to explore and compare indicators between countries and observe possible correlations between public investment and economic performance.

---

## Data Source

The data used in this project comes from the official IBGE country indicators API.

API documentation:
https://servicodados.ibge.gov.br/api/docs/paises

The API provides socioeconomic indicators such as GDP, education, and health statistics for countries around the world.

---

## Architecture

Data flows through the following stages:

```
API → ETL Pipeline → PostgreSQL → Dashboard
```

* **Extraction**: Socioeconomic indicators are retrieved from the IBGE API.
* **Transformation**: Data is cleaned and standardized.
* **Loading**: Processed data is stored in PostgreSQL.
* **Orchestration**: Airflow manages the pipeline schedule and execution.
* **Visualization**: A Streamlit dashboard provides interactive analysis.

---

## Technologies

* Python
* Apache Airflow
* PostgreSQL
* Docker Compose
* Streamlit

Python is used to implement the ETL pipeline and the dashboard.
Airflow orchestrates the data workflows.
PostgreSQL stores the processed data.
Docker ensures reproducible environments.

---

## Project Structure

```
project
│
├── dags/                 # Airflow workflows
├── data/                 # raw and intermediate data
├── logs/                 # pipeline logs
├── notebooks/            # exploratory analysis
│
├── src/                  # ETL scripts
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│
├── dashboard/            # Streamlit application
│   └── app.py
│   └── database.py
│   └── queries.py
│   └── config.py
│
├── docker-compose.yaml
├── pyproject.toml
└── README.md
```

---

## Dashboard

The dashboard provides an interactive interface to explore the data.

Main analyses include:

* GDP comparison across countries
* Investment in health and education
* Correlation between investment and GDP
* Country-level exploration of indicators

The application can be accessed through the public link:

```
[Dashboard URL]
```

---

## Running the Project Locally

Start the infrastructure:

```
docker compose up
```

Run the dashboard:

```
streamlit run dashboard/app.py
```

---

## Objective

This project demonstrates how a complete data workflow can be built, from **data ingestion to analytical visualization**, using common tools in modern data engineering.

It focuses on building a clear and reproducible pipeline that enables comparative socioeconomic analysis across Latin America.
