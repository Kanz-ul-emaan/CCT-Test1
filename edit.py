import random
import time

# Set up the target stimuli and the number of trials
targets = ['X', 'O']
num_trials = 10

# Initialize counters for correct and incorrect responses
correct = 0
incorrect = 0

# Start the CPT
print("Welcome to the Continuous Performance Test (CPT)!")
print("In this test, you will be presented with a series of stimuli on the screen.")
print("Your job is to press the corresponding keys on the keyboard as quickly and accurately as possible.")
print("")
print("Here are the details of the test:")
print("- Target stimuli: 'X' and 'O'")
print("- Non-target stimuli: 'A', 'B', and 'C'")
print("- Press 'X' for target stimuli and 'O' for non-target stimuli")
print("")
print("Are you ready to begin? Press any key to start the test.")
input()
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

  # Check if the response was correct
  if stimulus == 'X' and response == 'X':
    correct += 1
  elif stimulus == 'O' and response == 'O':
    correct += 1
  else:
    incorrect += 1

# Print the results
print(f"Average reaction time: {reaction_time:.2f} seconds")
