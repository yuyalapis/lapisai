def generate_field(state_field):
  field = []
  for i in range(state_field["height"]):
    for j in range(state_field["width"]):
      if (i,j) == state_field["knight"]:
        field.append("/")
      elif (i,j) == state_field["enemy"]:
        field.append("|")
      elif (i,j) == state_field["castle"]:
        field.append("-")
      elif (i,j) == state_field["opponent"]:
        field.append("o")
      else:
        field.append("_")
    if i is not state_field["height"] - 1:
      field.append("\n")
  return field