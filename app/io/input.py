import pandas as pd
def write_text_from_console():
    """
    для вводу тексту
    з консолі
    """
    return input()

def read_text_with_opportunities_python():
    """
    для зчитування з файлу за допомогою
    вбудованих можливостей python
    """
    with open("data/input.txt", "r") as file:
        return file.read()

def read_with_library_pandas():
    """
    для зчитування з файлу
    за допомогою бібліотеки pandas
    """
    df = pd.read_csv("data/input.csv")
    return df.to_string(index=False)