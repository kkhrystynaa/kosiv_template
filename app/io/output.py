def output_text_in_console(text):
    """
     для виводу
     тексту у консоль
    """
    print(text)

def write_to_file_with_opportunities_python(text):
     """
     для запису до файлу за допомогою
      вбудованих можливостей python
     """
     with open("data/output.txt", "a") as file:
         file.write(text + "\n")