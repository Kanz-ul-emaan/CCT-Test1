# Stroop Test
import random
import time

# Set up the target stimuli and the number of trials
targets = ['X', 'O']
num_trials = 10

# Initialize counters for correct and incorrect responses
correct = 0
incorrect = 0
total_reaction_time = 0

# Start the CPT
print("Starting CPT. Press 'X' for target stimuli, 'O' for non-target stimuli.")
for i in range(num_trials):
  # Display a random stimulus
  stimulus = random.choice(targets + ['A', 'B', 'C'])
  print(stimulus)

  # Record the start time
  start_time = time.time()

  # Get the person's response
  response = input()

  # Record the end time
  end_time = time.time()

  # Calculate the reaction time
  reaction_time = end_time - start_time
  total_reaction_time += reaction_time

  # Check if the response was correct
  if stimulus == 'X' and response == 'X':
    correct += 1
  elif stimulus == 'O' and response == 'O':
    correct += 1
  else:
    incorrect += 1

# Calculate the overall accuracy
accuracy = correct / (correct + incorrect)

# Calculate the average reaction time
average_reaction_time = total_reaction_time / num_trials

# Print the results
print(f"Accuracy: {accuracy:.2f}")
print(f"Average reaction time: {average_reaction_time:.2f} seconds")
