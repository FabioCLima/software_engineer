from pathlib import Path
import pandas as pd


class DatasetLoader:
    """
    A class used to represent a Dataset Loader.

    ...

    Attributes
    ----------
    dir_path : Path
        a Path object representing the directory path where the dataset is
        located
    file_name : str
        the name of the dataset file

    Methods
    -------
    load_data():
        Loads the dataset into a pandas DataFrame and returns it.
    """

    def __init__(self, dir_path: str, file_name: str) -> None:
        """
        Constructs all the necessary attributes for the DatasetLoader object.

        Parameters
        ----------
        dir_path : str
            The directory path where the dataset is located.
        file_name : str
            The name of the dataset file.
        """
        self.dir_path = Path(dir_path)
        self.file_name = file_name

    def load_data(self) -> pd.DataFrame:
        """
        Loads the dataset into a pandas DataFrame.

        The method checks whether the dataset file exists in the specified
        directory.
        If it exists, it loads the CSV file into a pandas DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the dataset.

        Raises
        ------
        FileNotFoundError
            If the file does not exist in the specified directory.
        """
        csv_path = self.dir_path / self.file_name

        if not csv_path.is_file():
            raise FileNotFoundError(
                f"The file {csv_path} does not exist.\
            Please ensure the dataset is in the correct folder."
            )

        return pd.read_csv(csv_path)


class DataFrameAnalyzer:
    def __init__(self, data):
        self.data = data

    def info(self) -> str:
        summary = self.data.info()
        return str(summary)

    def summary_stats(self) -> pd.DataFrame:
        summary_stats = self.data.describe()
        return summary_stats

    def size_data(self) -> tuple:
        return self.data.shape
