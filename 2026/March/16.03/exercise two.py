import os

path = "pastateste/"

try:
  os.makedirs(path)
except OSError:
  print(f"directory '{path}' already exists.")
else:
  print(f"directory '{path}' created successfully.")