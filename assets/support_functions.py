import datetime
from assets.colors import *

def formated_print(text_type, text_data, text_full_data):
  now = datetime.datetime.now()
  formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
  print(f'{GREY}{formatted_datetime}{RESET} {BLUE}{text_type}{RESET}     {GREEN}{text_data} {RESET}' + f'{text_full_data}', end="")
