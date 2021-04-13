def make_bricks(small, big, goal):
  Flag = goal - big*5 > 0 
  if small + big*5 < goal:
    return False
  if small + big * 5 == goal:
    return True
  if big*5 >= goal and goal % 5 == 0: 
    return True
  
  if Flag:
    if (goal-big*5) - small <= 0:
      return True
  if (goal - small) % 5 == 0 and big * 5 >= goal: 
    return True
  else:
    return False
    
