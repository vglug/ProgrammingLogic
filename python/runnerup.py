# Input the number of scores
n = int(input("Enter the number of scores: "))

# Input the list of scores as space-separated values
scores = list(map(int, input("Enter the scores: ").split()))

# Sort the list in descending order
scores.sort(reverse=True)

# Find the runner-up score
runner_up = None

for score in scores:
    if score < scores[0]:
        runner_up = score
        break

# Output the runner-up score
print("Runner-up score:", runner_up)
