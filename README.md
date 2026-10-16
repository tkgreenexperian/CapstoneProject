# Open Library Intelligence & Catalog Automation System

## Overview

The Open Library Intelligence & Catalog Automation System is a Python-based automation solution that integrates with the Open Library REST API to retrieve, process, store, analyze, and report on book data.

The application leverages object-oriented programming, SQLite, pandas, HTTPX, OpenPyXL, and pytest to provide a complete workflow for managing and analyzing library catalog information.

---

## Features

- Open Library API Integration
- Synchronous API Client
- Asynchronous API Client
- SQLite Database Storage
- Data Cleaning and Normalization
- Book Search Functionality
- Pandas Analytics and Reporting
- CSV Export
- Excel Export
- Interactive CLI Menu
- Custom Exception Handling
- Pytest Test Suite

---

## Project Structure

```text
CapstoneProject/
│
├── data/
│   ├── books.csv
│   ├── books.xlsx
│   └── library.db
│
├── src/
│   ├── api/
│   │   ├── sync_client.py
│   │   └── async_client.py
│   │
│   ├── db/
│   │   └── library_db.py
│   │
│   ├── processing/
│   │   └── data_cleaner.py
│   │
│   ├── reporting/
│  