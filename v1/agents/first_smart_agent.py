import datetime
import pickle
import glob


class FirstSmartAgent(object):
  """Agent that Attacks in a smart way using Long-term Memory"""
  def __init__(self, y, x, field_width, field_height, sight):
    self.x = x
    self.y = y
    self.field_width = field_width
    self.field_height = field_height
    self.sight = sight
    self.previous_decision = -1
    self.valid_logs = []
    self.valid_log = []
    self.load_valid_logs()
    self.logs_this_iteration = []
  def action(self):
    if self.replayable():
      result = (datetime.datetime.now().second + datetime.datetime.now().microsecond) % 2
      if result == 0:
        print("\n\nREPLAY")
        self.replay()
        return
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
  def save_valid_logs(self, logs):
    if logs in self.valid_logs:
      return
    for each_valid_log in self.valid_logs:
      if set(logs) & set(each_valid_log) == set(logs):
        return
    if not logs:
      return
    clock = str(datetime.datetime.now().date()) + "-" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    with open("data/logs-"+clock, "wb") as f:
      pickle.dump(logs, f)
  def load_valid_logs(self):
    list_file_path = glob.glob("data/*")
    valid_logs = []
    for file_path in list_file_path:
      with open(file_path, 'rb') as f:
        log = pickle.load(f)
        if log:
          valid_logs.append(log)
    valid_logs = sorted(valid_logs, key=lambda x: len(x), reverse=False)
    self.valid_logs = valid_logs
    valid_log = []
    for each_valid_log in valid_logs:
      valid_log += each_valid_log
    # replay
    self.valid_log = valid_log
  def replayable(self):
    for sight_dicision_pair in self.valid_log:
      sight = sight_dicision_pair[0]
      if tuple(sight) == tuple(self.sight):
        return True
    return False
  def replay(self):
    for sight_dicision_pair in self.valid_log:
      sight = sight_dicision_pair[0]
      if tuple(sight) == tuple(self.sight):
        decision = sight_dicision_pair[1]
        self.previous_decision = decision
        if decision == 1 and self.y > 0:
          self.y -= 1
        elif decision == 2 and self.x > 0:
          self.x -= 1
        elif decision == 3 and self.y < (self.field_height - 1):
          self.y += 1
        elif decision == 4 and self.x < (self.field_width - 1):
          self.x += 1
        break