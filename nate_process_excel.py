"""
Process an Excel file to count occurrences of a specific word in a column.

"""

import pathlib
import openpyxl
from utils_logger import logger
import xlwings as xw
import pandas as pd
import statistics

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

Workbook=r"data/AnnualFoodImports.xlsx"
Sheet='Coffee'

def get_coffee_data_from_excel() -> dict:
    """this will open the data/AnnualFoodImports.xlsx sheet=Coffee and get specific coffee import data """
    try:
        data=pd.read_excel(Workbook,sheet_name=Sheet, usecols="C,E", skiprows=15, nrows=7, header=None)
        data_list = data[4].to_list()
        stats = {
            "min": min(data_list),
            "max": max(data_list),
            "mean": statistics.mean(data_list),
            "stdev": statistics.stdev(data_list) if len(data_list) > 1 else 0,
        }
        return stats
        
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """this will write the statics data to data_processed/Coffee_imports_results.txt"""

    input_file = pathlib.Path(fetched_folder_name, "AnnualFoodImports.xlsx")
    output_file = pathlib.Path(processed_folder_name, "Coffee_imports_results.txt")

    data= get_coffee_data_from_excel()

    with output_file.open('w') as file:
        file.write("2023 Coffee imports millions of dollars Statistics:\n")
        file.write(f"Minimum: {data['min']:.2f}\n")
        file.write(f"Maximum: {data['max']:.2f}\n")
        file.write(f"Mean: {data['mean']:.2f}\n")
        file.write(f"Standard Deviation: {data['stdev']:.2f}\n")
    
    logger.info(f"Processed Excel file: {input_file}, Results saved to: {output_file}")


 

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")