import datetime


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
    elif decision == 3 and self.y < (self.field_height - 1):
      self.y += 1
    elif decision == 4 and self.x < (self.field_width - 1):
      self.x += 1
  def update_sight(self, sight):
    self.sight = sight