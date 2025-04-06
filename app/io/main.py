from input import  write_text_from_console, read_text_with_opportunities_python,  read_with_library_pandas
from output import output_text_in_console, write_to_file_with_opportunities_python



def main():
     text1=write_text_from_console
     text2=read_text_with_opportunities_python
     text3=read_with_library_pandas

     output_text_in_console(text1)
     output_text_in_console(text2)
     output_text_in_console(text3)

     write_to_file_with_opportunities_python(text1)
     write_to_file_with_opportunities_python(text2)
     write_to_file_with_opportunities_python(text3)
if __name__=="__main__":
    main()