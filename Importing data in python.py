# Open a file as read-only and bind it to file
with open('moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())