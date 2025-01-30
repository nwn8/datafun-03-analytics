"""
Process a JSON file to count 
  

"""


import pathlib
import json
from utils_logger import logger

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"


def count_astronauts_by_craft(file_path: pathlib.Path) -> dict:
    """Count the number of astronauts on each spacecraft from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            pop_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            craft_counts_dictionary = {}
            # people is a list of dictionaries in the JSON file
            pop_list: list = pop_dictionary.get("population", [])
           
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "population.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "population_process.txt")
    
    craft_counts = count_astronauts_by_craft(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Astronauts by spacecraft:\n")
        for craft, count in craft_counts.items():
            file.write(f"{craft}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")



if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")