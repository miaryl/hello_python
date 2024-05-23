import json

def read_json_file(file_name):
    data = ""
    try:
      with open(file_name) as json_file:
          data = json.load(json_file)
    except IOError:
      print("Could not read file")
    return data

read_json_file('c:/Users/gusw0/Desktop/hello_python/14:126/files/insulin.json')
