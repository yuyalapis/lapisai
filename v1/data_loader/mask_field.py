def mask_field(field, sight_level, center_y, center_x, width):
  sight = []
  if sight_level == 1:
    try:
      if field[(width+1) * (center_y - 1) + center_x] == "\n" or ((width+1) * (center_y - 1) + center_x) < 0:
        sight.append(" ")
      else:
        sight.append(field[(width+1) * (center_y - 1) + center_x])
    except Exception as e:
      sight.append(" ")
    #
    try:
      if field[(width+1) * (center_y) + (center_x - 1)] == "\n" or ((width+1) * (center_y) + (center_x - 1)) < 0:
        sight.append(" ")
      else:
        sight.append(field[(width+1) * (center_y) + (center_x - 1)])
    except Exception as e:
      sight.append(" ")
    #
    try:
      if field[(width+1) * (center_y + 1) + center_x] == "\n":
        sight.append(" ")
      else:
        sight.append(field[(width+1) * (center_y + 1) + center_x])
    except Exception as e:
      sight.append(" ")
    #
    try:
      if field[(width+1) * (center_y) + (center_x + 1)] == "\n":
        sight.append(" ")
      else:
        sight.append(field[(width+1) * (center_y) + (center_x + 1)])
    except Exception as e:
      sight.append(" ")
  return sight