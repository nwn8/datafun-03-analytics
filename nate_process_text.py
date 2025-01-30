"""
Process a text file to count how many lines SAMPSON has and save the result.
"""


import pathlib
from utils_logger import logger


fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"


def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'SAMPSON', and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "Shakespere.txt")
    output_file = pathlib.Path(processed_folder_name, "SAMPSON.txt")
    word_to_count: str = "SAMPSON"
    word_count: int = count_word_occurrences(input_file, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Number of Lines for'{word_to_count}': {word_count}\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")