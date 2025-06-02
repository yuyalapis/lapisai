import time
import datetime

field = """
|-_
___
___
___
_-/
"""
field = field.strip()
print(field)

state_field = {
  "width": 3,
  "height": 5,
  "knight": (4,2),
  "enemy": (0,0),
  "castle": (4,1),
  "opponent": (0,1),
  "life_castle": 3,
  "life_opponent": 3
}

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
        field.append("-")
      else:
        field.append("_")
    if i is not state_field["height"] - 1:
      field.append("\n")
  return field

print("".join(generate_field(state_field)))

class RandomAgent(object):
  """Random-walk agent"""
  def __init__(self, y, x, field_width, field_height):
    self.x = x
    self.y = y
    self.field_width = field_width
    self.field_height = field_height
  def action(self):
    decision = (datetime.datetime.now().second + datetime.datetime.now().microsecond) % 5
    if decision == 1 and self.y > 0:
      self.y -= 1
    elif decision == 2 and self.x > 0:
      self.x -= 1
    elif decision == 3 and self.y < (self.field_height - 1) - 1:
      self.y += 1
    elif decision == 4 and self.x < (self.field_width - 1) - 1:
      self.x += 1


state_field = {
  "width": 3,
  "height": 5,
  "knight": (4,2),
  "enemy": (0,0),
  "castle": (4,1),
  "opponent": (0,1),
  "life_castle": 3,
  "life_opponent": 3
}

knight = RandomAgent(
  state_field["knight"][0], state_field["knight"][1],
  state_field["width"], state_field["height"]
)
print(knight.y, knight.x)
print("".join(generate_field(state_field)))

for i in range(10):
  time.sleep(1)
  knight.action()
  state_field["knight"] = (knight.y, knight.x)
  print("".join(generate_field(state_field)))
  print("knight: ", state_field["knight"][0], state_field["knight"][1])
  print("\n\nnew state")


def mask_field(field, sight_level, center_y, center_x, width):
  sight = []
  if sight_level == 1:
    try:
      if field[(width+1) * (center_y - 1) + center_x] == "\n":
        sight.append(" ")
      else:
        sight.append(field[(width+1) * (center_y - 1) + center_x])
    except Exception as e:
      sight.append(" ")
    #
    try:
      if field[(width+1) * (center_y) + (center_x - 1)] == "\n":
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

print(mask_field(generate_field(state_field), 1, 4,2, 3))

class AttackAgent(object):
  """Agent that Attacks"""
  def __init__(self, y, x, field_width, field_height, sight):
    self.x = x
    self.y = y
    self.field_width = field_width
    self.field_height = field_height
    self.sight = sight
    self.previous_decision = -1
  def action(self):
    slot = []
    if self.sight[0] != " ":
      slot.append(1)
    if self.sight[1] != " ":
      slot.append(2)
    if self.sight[2] != " ":
      slot.append(3)
    if self.sight[3] != " ":
      slot.append(4)
    result = (datetime.datetime.now().second + datetime.datetime.now().microsecond) % len(slot)
    decision = slot[result]
    self.previous_decision = decision
    if decision == 1 and self.y > 0:
      self.y -= 1
    elif decision == 2 and self.x > 0:
      self.x -= 1
    elif decision == 3 and self.y < (self.field_height - 1) - 1:
      self.y += 1
    elif decision == 4 and self.x < (self.field_width - 1) - 1:
      self.x += 1
  def update_sight(self, sight):
    self.sight = sight


state_field = {
  "width": 3,
  "height": 5,
  "knight": (4,2),
  "sight_level_knight": 1,
  "enemy": (0,0),
  "castle": (4,1),
  "opponent": (0,1),
  "life_castle": 3,
  "life_opponent": 3
}

knight = AttackAgent(
  state_field["knight"][0], state_field["knight"][1],
  state_field["width"], state_field["height"],
  mask_field(
    generate_field(state_field),
    state_field["sight_level_knight"], 
    state_field["knight"][0], state_field["knight"][1], 
    state_field["width"]
  )
)
print(knight.y, knight.x)
print(knight.sight)
print("".join(generate_field(state_field)))

for i in range(10):
  time.sleep(1)
  knight.action()
  print("\n\nnew state")
  state_field["knight"] = (knight.y, knight.x)
  print("".join(generate_field(state_field)))
  print("knight: ", state_field["knight"][0], state_field["knight"][1])
  print("previous_decision: ", knight.previous_decision)
  knight.update_sight(
    mask_field(
      generate_field(state_field),
      state_field["sight_level_knight"], 
      state_field["knight"][0], state_field["knight"][1], 
      state_field["width"]
    )
  )
  print(knight.sight)
