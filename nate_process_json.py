"""
Process a JSON file to get population data statistics
  

"""


import pathlib
import json
from utils_logger import logger
import statistics

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"


def get_populations(file_path: pathlib.Path) -> dict:
    """this will read from the data/population.json and return a list of populations"""
    try:
        with file_path.open('r') as file:
            pop_dictionary = json.load(file)  
            pop_dictionary_result = []
            pop_list: list = pop_dictionary.get("data", [])
         
            for each in pop_list:  
          
                number = each.get("Population")
                pop_dictionary_result.append(number)

            return pop_dictionary_result
           
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}
    

def calculate_statistics(info: list) -> dict:
      stats = {
            "min": min(info),
            "max": max(info),
            "mean": statistics.mean(info),
            "stdev": statistics.stdev(info) if len(info) > 1 else 0,
        }
      return stats

def process_json_file():
    """this will take the data and write it to a file in data_processed/population_process.txt"""

    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "population.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "population_process.txt")
    
    pop_info = get_populations(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)


    stats = calculate_statistics(pop_info)



    with output_file.open('w') as file:
        file.write("Population Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")



if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")