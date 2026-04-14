# FastAPI Excel Processor Assignment

## Overview

The primary goal of this assignment is to assess your understanding of API development using FastAPI, your problem-solving skills, your coding style, and your ability to present your work clearly and professionally.

You are tasked with creating a FastAPI application that can read data from a given Excel sheet and expose a few endpoints to interact with this data.

## Tasks

Your main task is to develop a FastAPI application with the following functionalities:

### 1. Excel Sheet Processing
The application must be able to read a provided Excel sheet and parse its contents (`/Data/capbudg.xls`).

### 2. API Endpoints
You need to implement the following FastAPI endpoints. Please use `http://localhost:9090` as the base URL for your endpoints.

#### a. `GET /list_tables`
   - **Functionality:** This endpoint should list all the table names present in the uploaded/specified Excel sheet.
   - **Response Example:**
     ```json
     {
       "tables": ["Initial Investment", "Revenue Projections", "Operating Expenses"]
     }
     ```

#### b. `GET /get_table_details`
   - **Parameters:**
     - `table_name: str` (Query parameter specifying the name of the table)
   - **Functionality:** This endpoint should return the names of the rows for the selected table. These row names are typically the values found in the first column of that table.
   - **Example:** If the user selects the "Initial Investment" table, the API should list the first column values like so:
     ```json
     {
       "table_name": "Initial Investment",
       "row_names": [
         "Initial Investment=",
         "Opportunity cost (if any)=",
         "Lifetime of the investment",
         "Salvage Value at end of project=",
         "Deprec. method(1:St.line;2:DDB)=",
         "Tax Credit (if any )=",
         "Other invest.(non-depreciable)="
       ]
     }
     ```

#### c. `GET /row_sum`
   - **Parameters:**
     - `table_name: str` (Query parameter specifying the name of the table)
     - `row_name: str` (Query parameter specifying the name of the row, which must be one of the names returned by `/get_table_details`)
   - **Functionality:** This endpoint should calculate and return the sum of all numerical data points in the specified row of the specified table.
   - **Example:** If the `row_name` is `"Tax Credit (if any )="` for a table where this row contains the value `10` (or `10%`), the output should be:
     ```json
     {
       "table_name": "Initial Investment",
       "row_name": "Tax Credit (if any )=",
       "sum": 10 
     }
     ```
     *(Note: You can decide whether to include units like '%' in the response or just return the numerical sum. Please clarify your approach in your documentation.)*

## Evaluation Criteria

We will be evaluating your submission based on the following:

*   **Problem-Solving Skills:** Your ability to understand the requirements and implement a functional solution.
*   **Coding Style:** Clarity, organization, and adherence to Python best practices. We expect well-structured, modular code, with docstrings, and robust error handling etc.
*   **Presentation Style:** The quality and completeness of this `README.md` file (which you will update with your insights) and the Postman collection.
*   **Documentation:** Ensure your code is well-documented.

## Your Insights

Please complete the following sections with your thoughts on the assignment.

### Potential Improvements
*(Describe any ideas you have on how this application or assignment could be improved or extended. For example, handling different Excel formats, more advanced data operations, UI integration, etc.)*

### Missed Edge Cases
*(Identify any edge cases or scenarios that your current implementation might not handle or that were not explicitly covered in the requirements. For example, empty Excel files, tables with no numerical data, malformed table names, etc.)*

## Testing

To help us quickly test your application, please provide a Postman collection JSON.

*   **Base URL:** `http://localhost:9090` and the given endpoint names.
*   **Postman Collection:** 
