from fastapi import FastAPI
import pandas as pd
from enum import Enum



list_tables = [] # LIST OF TABLE NAMES
table_details = {} # DICTIONARY OF TABLES (PANDAS DATAFRAMES)


#-------------------FUNCTION FOR EXTRACTING DESIRABLE TABLE----------------------------#

def extract_table(header, n_rows, start_col, end_col, name):
    df = pd.read_excel('capbudg.xls', engine = 'xlrd', header = header, nrows = n_rows)
    df = df.iloc[:, start_col:end_col]
    df = df.fillna('')

# Clearing Nans and 'Unnamed:' cells
    df.dropna(how='all', axis = 1, inplace = True)
    df.columns = [col if not 'Unnamed:' in col else '' for col in df.columns]
    if name != "no" :
        list_tables.append(name) # Parallely appends the name of table in the list
        table_details.update({name : df}) # updates detail dictionary
    return df

# -----------------------------WHOLE DATA EXTRACTED-------------------------------------#

InitialInvestment_df = extract_table(2, 7, 0, 3, "Initial Investment" )
CashflowDetails_df = extract_table(2,4,4,7, "Cashflow Details" )
DiscountRate_df = extract_table(2,8,8,11, "Discount Rate")
WorkingCapital_df = extract_table(11, 3, 0, 3, "Working Capital")
GrowthRates_df = extract_table(16, 3, 0, 12, "Growth Rates")
InitialInvestment_1_df = extract_table(23, 7, 0, 2, "Initial Investments")
SalvageValue_df = extract_table(32, 2, 0, 12, "Salvage Value")
OperatingCashflows_df = extract_table(36, 14, 0, 12, "Operating Cashflows")
InvestmentMeasures_df = extract_table(52, 3, 1, 3, "Investment Measures")
BookValueAndDepreciation_df = extract_table(58, 3, 0, 12, "Book Value & Depreciation")
Total_df = extract_table(21, 41, 0, 12, "no")

#--------------------------------------------------------------------------------------------------#

dict_tables = {"tables" : list_tables}

class AvailableTables(str, Enum) : # To show available tables
    InitialInvestment = "Initial Investment"
    CashflowDetails = "Cashflow Details"
    Discount = "Discount"
    WorkingCapital = "Working Capital"
    GrowthRates = "Growth Rates"
    InitialInvestments = "Initial Investments"
    SalvageValue = "Salvage Value"
    OperatingCashflows = "Operating Cashflows"
    InvestmentMeasures = "Investment Measures"
    BookValueAndDepreciation = "Book Value & Depreciation"

app = FastAPI()

@app.get("/")
async def root() :
    return {"Project" : "Equity Analysis"}

@app.get("/list_tables")
async def list_tables() :
    return dict_tables

@app.get("/get_table_details")
async def get_table_details(table_name : AvailableTables) :
    row_dict = {
        "table_name" : table_name,
        "row names" : table_details[table_name].iloc[:,0].tolist(),
    }
    return row_dict

@app.get("/row_sum")
async def get_table_sum(table_name : AvailableTables, row_name : str) :

    y = table_details[table_name]
    k = 0

    # Getting index of cell named "row_name"
    for i in range(len(y)):
        if y.iloc[i, 0] == row_name :
            k = i
            break

    # list to store the data of that row for further manipulation
    temp_list = []
    for i in range(len(y.columns)):
        temp_list.append(y.iloc[k, i])

        # getting sum of all 'Numerical' values in the row
        total = 0
        for item in temp_list :
            if type(item) != str:
                total += item
    return {
        "table_name" : table_name,
        "row_name" : row_name,
        "sum" : total,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9090)



