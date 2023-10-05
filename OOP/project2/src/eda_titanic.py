from pathlib import Path
import pandas as pd


def load_titanic_data() -> pd.DataFrame:
    """
    Load the Titanic dataset into a pandas DataFrame.

    The function checks whether the dataset already exists in the
    'datasets' folder within the project directory. If it exists,
    it loads the CSV file into a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the Titanic dataset.
    """
    # Define the relative path to the CSV file within the project directory
    # Define the directory and file path
    dir_path = Path("project2/datasets")
    csv_path = Path(dir_path / "train.csv")

    # Check if the CSV file exists
    if not csv_path.is_file():
        raise FileNotFoundError(
            f"The file {csv_path} does not exist.\
        Please ensure the dataset is in the 'datasets' folder."
        )

    # Load and return the CSV file as a DataFrame
    return pd.read_csv(csv_path)
