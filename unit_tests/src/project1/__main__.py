from typing import List
from src.project1.data_transform import clean_data_lower

input: List[str] = ["Python", " Fabio Carvalho Lima", "Hello World  ", "PYTHON IS NICE"]

if __name__ == "__main__":
    for word in input:
        output = clean_data_lower(word)
        print(f"input word: {word}, processed word: {output}\n")
