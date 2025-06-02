from v1.agents.attack_agent import AttackAgent
from v1.data_loader.mask_field import mask_field
from v1.states.state_field_3x5 import state_field
from v1.data_loader.generate_field import generate_field

import time
import datetime


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
