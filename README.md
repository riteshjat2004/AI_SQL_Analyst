# 🤖 AI SQL Data Analyst

An AI-powered SQL assistant that enables users to query PostgreSQL databases using natural language. The application leverages Large Language Models (LLMs) to translate user questions into SQL queries, validates them for safety, executes them on PostgreSQL, and displays the results through an interactive Streamlit interface.

---

## 🚀 Features (Current)

- Natural Language → SQL conversion using Llama 3.2 (Ollama)
- Automatic PostgreSQL schema discovery
- Schema-aware prompt engineering
- SQL validation for secure query execution
- Execute generated SQL on PostgreSQL
- Interactive Streamlit interface
- Display generated SQL and query results
- Query execution time and returned row count

---

## 🛠️ Tech Stack

### Backend
- Python
- SQLAlchemy
- PostgreSQL
- Ollama
- Llama 3.2

### Data Processing
- Pandas

### Frontend
- Streamlit

### Utilities
- Pydantic Settings
- Regular Expressions (Regex)

---

# Project Architecture

```
User Question
      │
      ▼
Prompt Builder
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Generated SQL
      │
      ▼
SQL Validator
      │
      ▼
PostgreSQL Database
      │
      ▼
Pandas DataFrame
      │
      ▼
Streamlit UI
```

---

# Project Structure

```
AI_SQL_Analyst/

│
├── src/
│   │
│   ├── ai/
│   │   ├── llm.py
│   │   ├── prompt_builder.py
│   │   ├── schema_reader.py
│   │   └── sql_validator.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── services/
│   │   └── query_executor.py
│   │
│   ├── utils/
│   │
│   └── app.py
│
├── data/
├── requirements.txt
└── README.md
```

---

# Workflow

### 1. User enters a question

Example

```
Show the top 5 products by revenue.
```

---

### 2. Read Database Schema

The application automatically reads:

- Tables
- Columns
- Primary Keys
- Foreign Keys

using SQLAlchemy Inspector.

---

### 3. Build Prompt

A schema-aware prompt is created containing:

- Database schema
- SQL generation rules
- User question

This significantly improves SQL generation accuracy.

---

### 4. Generate SQL

The prompt is sent to Llama 3.2 using Ollama.

Example:

```
SELECT
    product_name,
    SUM(quantity * price) AS revenue
FROM ...
```

---

### 5. Validate SQL

Before execution, every generated query is validated.

Allowed:

- SELECT
- WITH

Blocked:

- INSERT
- UPDATE
- DELETE
- DROP
- ALTER
- CREATE
- TRUNCATE
- GRANT
- REVOKE

This prevents destructive database operations.

---

### 6. Execute Query

Validated SQL is executed using SQLAlchemy.

Results are loaded into a Pandas DataFrame.

---

### 7. Display Results

The application displays:

- Generated SQL
- Execution Time
- Number of Rows Returned
- Query Results

inside the Streamlit application.

---

# Modules

## schema_reader.py

Responsible for automatically reading the PostgreSQL schema.

Responsibilities:

- Read tables
- Read columns
- Read primary keys
- Read foreign keys

Output:

A formatted schema string used by the LLM.

---

## prompt_builder.py

Creates a schema-aware prompt by combining:

- Database schema
- SQL generation rules
- User question

---

## llm.py

Responsible for:

- Connecting to Ollama
- Sending prompts
- Receiving generated SQL
- Cleaning model output

---

## sql_validator.py

Ensures only safe SQL queries are executed.

Rejects destructive SQL statements before they reach PostgreSQL.

---

## query_executor.py

Acts as the main service layer.

Responsibilities:

1. Generate SQL
2. Validate SQL
3. Execute SQL
4. Return SQL + DataFrame

---

## app.py

Provides the Streamlit interface.

Current features:

- Ask questions
- Display generated SQL
- Display results
- Execution time
- Row count

---

# Current Progress

## Completed

- PostgreSQL database
- SQLAlchemy integration
- Streamlit setup
- Ollama integration
- Schema Reader
- Prompt Builder
- LLM SQL Generation
- SQL Validation
- AI Query Execution
- Interactive UI

---

## In Progress

- Automatic Plotly visualizations
- AI-generated business insights
- Download results as CSV
- Query history

---

# Example

### User Question

```
Show all customers.
```

Generated SQL

```sql
SELECT *
FROM customers;
```

Results

| customer_id | name | email | city |
|--------------|------|-------|------|

---

# Future Enhancements

- Automatic chart generation
- AI-powered business insights
- Download query results
- Query history
- Follow-up question suggestions
- Conversation memory
- FastAPI REST API
- Docker support
- Authentication
- Multi-database support

---

# Learning Outcomes

Through this project, I learned:

- LLM prompt engineering
- Schema-aware SQL generation
- PostgreSQL integration with SQLAlchemy
- Streamlit application development
- Safe SQL validation
- AI application architecture
- Modular Python project design