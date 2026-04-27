import datetime

def convert(date_time):
    format = r'%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str

file_path = r"C:\Users\bennd\OneDrive\Documents\VSC Projects\git_cli\M6A1_BenjaminHoogerwerf\today.txt"
# when "today.txt" is stored somewhere else, change file_path accordingly.

with open(file_path, 'r') as file:
    today_string = file.read()

date_time = today_string
print(convert(date_time))
print(type(convert(date_time)))