import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k in kwargs:
      for i in range(kwargs[k]):
        self.contents.append(k)

  def draw(self, n_balls):
    if n_balls > len(self.contents):
      n_balls = len(self.contents)
    balls_drawn = random.sample(self.contents, n_balls)
    #Removes all the balls drawn from the "contents" attribute
    for ball in balls_drawn:
      self.contents.remove(ball)
    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #Create list to store results from experimet: 1 for true and 0 for false. Taking the average from this list will give the probability.
  draw_results = []
  
  #Loop to run the specified number of experiments
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat) #makes a copy of hat,in order to not alter the original "contents" and use in the next experiment.
    experiment_result = hat_copy.draw(num_balls_drawn)
    dict_result = dict()
    
    #Makes a dict from the list experiment_result
    for ball in experiment_result:
      dict_result[ball] = dict_result.get(ball,0) + 1
    
    #Comparison between the two dictionaries (expected and experiment)
    comparison = []
    for k in expected_balls:
      if k in dict_result.keys(): #to avoid a KeyError
        #if the number of balls of that color drawn from the hat its equal or greater than the expected, stores a 1 in comparison list.
        if dict_result.get(k) >= expected_balls.get(k):
          comparison.append(1)
        else: #if its smaller stores a 0
          comparison.append(0)
      else: #no ball of that color has been drawn, so stores a 0 in the comparison list.
        comparison.append(0)
    if all(comparison): #if all items in comparison list are 1 stores 1 in the experiment results list, if not stores a 0
      draw_results.append(1)
    else:
      draw_results.append(0)
  
  #Calculate a return the average from the results list, i.e. the probability.
  return (sum(draw_results) / len(draw_results))
