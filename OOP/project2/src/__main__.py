# from eda_titanic import load_titanic_data

from eda_titanic_opp import DatasetLoader
from eda_titanic_opp import DataFrameAnalyzer

if __name__ == "__main__":
    # titanic = load_titanic_data()
    # print(titanic.head())

    # print()
    # create an instance of DatasetLoader with the specified directory path
    # and file name
    dir_path: str = "project2/datasets"
    input_csv_file = "train.csv"
    dataset_loader = DatasetLoader(dir_path=dir_path, file_name=input_csv_file)

    # load the Titanic dataset
    titanic_data = dataset_loader.load_data()
    print(titanic_data.head())

    analyzer = DataFrameAnalyzer(titanic_data)
    summary_info = analyzer.info()
    print(summary_info)

    print("Summary Statistics:")
    statistics = analyzer.summary_stats()
    print(statistics)

    print()
    number_rows, number_columns = analyzer.size_data()
    print(
        (
            f"The dimension of the inputed DataFrame:\n"
            f"number of rows={number_rows}  and "
            f"number of columns={number_columns} "
        )
    )
