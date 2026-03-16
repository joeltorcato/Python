import os

path = "pastateste"

try: 
  os.mkdir(path)
except OSError:
  print(f"directory '{path}' already exists.")
else:
  print(f"directory '{path}' created successfully.")