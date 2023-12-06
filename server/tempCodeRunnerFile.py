relative_path1 = "artifacts/class_dictionary.json"
   #  relative_path2 = "artifacts/saved_model.pkl"
   #    # Construct the absolute path
   #  file_path1 = os.path.abspath("artifacts/class_dictionary.json")
   #  file_path2 = os.path.join(current_directory, relative_path2)

   #  print("loading saved artifacts...start")
   #  global __class_name_to_number
   #  global __class_number_to_name
   #  with open(file_path1,'r') as f:
   #      __class_name_to_number = json.load(f)
   #      __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

   #  global __model
   #  if __model is None:
   #      with open(file_path2, 'rb') as f:
   #          __model = joblib.load(f)