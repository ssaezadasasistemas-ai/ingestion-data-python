# Data Ingestion into MySQL using Python

## Overview

This project contains a collection of practical exercises focused on ingesting data into a MySQL database using different sources, formats, and tools.

The goal of this work is to understand and practice the most common data ingestion patterns used in real-world backend and data engineering scenarios.  
The exercises cover Python-based ETL pipelines, native MySQL ingestion mechanisms, and GUI-based imports for ad-hoc operations.

---

## Objectives

- Learn how to ingest data into MySQL from multiple data sources
- Understand when to use Python-based ETL pipelines versus native MySQL features
- Practice real-world ingestion patterns used in production systems
- Work with CSV, XML, TXT, and REST API data sources
- Understand bulk loading and GUI-based imports
- Avoid manual database schema creation by generating schemas automatically from data

---

## Technologies Used

- **Python 3**
- **MySQL 8**
- **MySQL Workbench**
- **MySQL CLI**
- **Python Libraries**
  - pandas
  - requests
  - mysql-connector-python
  - pymysql
  - python-dotenv

---

## Environment Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```bash
pip install pandas requests mysql-connector-python pymysql python-dotenv
```

### 3. Environment variables

Create a `.env` file:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=1234

DB_EMPLOYEES=myempdb
DB_POKEMON=pokemon_db
DB_ETL=etl_demo
DB_AUTO_SCHEMA=auto_schema_db
```

---

## Ingestion Scenarios Covered

### 1. CSV File → MySQL (Python ETL)

**Description**  
A local CSV file is read using Python, optionally transformed, and inserted into MySQL using parameterized SQL queries.

**Key concepts**
- CSV parsing with Python
- Data type conversion
- Batch inserts using `executemany`
- Idempotent inserts using `ON DUPLICATE KEY UPDATE`

**Use case**
- Small to medium datasets
- Validation or transformation before loading

---

### 2. XML File → MySQL (Python ETL)

**Description**  
An XML file is parsed using Python, transformed into structured records, and loaded into MySQL.

**Key concepts**
- XML parsing
- Data normalization
- Handling duplicate primary keys
- Transaction handling (`commit` / `rollback`)

**Use case**
- Legacy systems
- Hierarchical but structured data sources

---

### 3. REST API → MySQL (Python ETL)

**Description**  
Data is retrieved from an external REST API, transformed into a tabular structure, and stored in MySQL.

**API used**
- PokéAPI (public, no authentication): https://pokeapi.co/

**Key concepts**
- HTTP requests using `requests`
- JSON parsing
- Environment variables (`.env`)
- Incremental and idempotent loading
- API error handling (HTTP errors, timeouts)

**Use case**
- External services
- Microservice integrations
- Periodic data refresh pipelines

---

### 4. TXT File → MySQL (Bulk Load using LOAD DATA INFILE)

**Description**  
A tab-delimited TXT file is loaded directly into MySQL using the native `LOAD DATA LOCAL INFILE` command.

**Key concepts**
- Bulk data loading
- `LOAD DATA LOCAL INFILE`
- Handling NULL values using `\N`
- Line terminators (`\r\n` on Windows)
- MySQL security restrictions (`local_infile`)

**Use case**
- Large datasets
- High-performance ingestion
- Nightly batch jobs
- Legacy flat-file integrations

---

### 5. CSV → MySQL using MySQL Workbench (GUI)

**Description**  
A CSV file is imported using the MySQL Workbench Table Data Import Wizard.

**Key concepts**
- GUI-based ingestion
- Column mapping
- Handling headers
- Encoding selection

**Use case**
- One-off imports
- Manual or ad-hoc operations
- Non-technical users
- Data validation and inspection

---

### 6. Automatic Schema Creation → MySQL (Python)

**Description**  
The database schema is generated automatically from the source data instead of being created manually.

A Python script analyzes the input CSV file, infers column names and data types, dynamically generates a `CREATE TABLE` SQL statement, and executes it against MySQL.

**Key concepts**
- Schema inference from source data
- Dynamic SQL generation
- Automated database modeling
- Data-driven schema creation
- Integration with ETL pipelines

**Use case**
- Initial data migrations
- Rapid prototyping
- Unknown or evolving data structures
- Automated ingestion pipelines

---

## Comparison of Ingestion Methods

| Source      | Method | Tool |
|------------|--------|------|
| CSV        | ETL    | Python |
| XML        | ETL    | Python |
| REST API   | ETL    | Python |
| TXT (bulk) | Native | MySQL (`LOAD DATA`) |
| CSV        | GUI    | MySQL Workbench |

---

## Key Learnings

- Not all ingestion problems require Python
- Bulk loading (`LOAD DATA INFILE`) is significantly faster than row-by-row inserts
- Python is best used when:
  - Data validation is required
  - Transformation is needed
  - Ingestion must be automated
- GUI tools are useful for ad-hoc operations but not suitable for production pipelines
- MySQL security settings can affect ingestion workflows
- Idempotent loading is critical for reliable pipelines
- Database schemas can be generated automatically from data, avoiding manual setup

---

## Conclusion

This project provides hands-on experience with multiple data ingestion strategies that closely resemble real-world backend and data engineering scenarios.

By combining Python-based ETL pipelines, MySQL native bulk loading, GUI-based imports, and automatic schema generation, a comprehensive overview of practical ingestion techniques has been achieved.

This work forms a solid foundation for:
- Junior Data Engineering roles
- Backend development involving data pipelines
- Understanding production-grade ingestion architectures
