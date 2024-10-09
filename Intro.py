                                #INTRO

print(type(revenue_on_target))

# Create a string variable called name
name = "John Smith"

# Create an integer variable called age
age = 47

# Create a string variable called address
address = "The Shard, London, SE1 9SG"

# Print their information
print(name,age,address)

# Create a boolean variable called is_adult
is_adult = True

# Update John's address
address = "Buckingham Palace, London, SW1A 1AA"

# Print their information
print(is_adult,address)



                                #METHODS

#mutli-line comments/string
# Create review_one
review_one = """I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""

# Create review_two
review_two = """One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Print the two reviews individually
print(review_one)
print(review_two)

#replace 
most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)



                            # DATA STRUCTURES#
#LISTS

# Create the playlist variable
playlist = [1, "Blinding Lights", 2, "One Dance", 3, "Uptown Funk"]

# Print the list
print(playlist)

# Get the last song's artist
print(playlist[17])

# Print all songs in the playlist
print(playlist[1::3])



#DICTIONARIES

# Create the playlist dictionary
playlist = { "The Weeknd" : "Blinding Lights", "Drake" : "One Dance"}

# Print the playlist
print(playlist)

# Print the song by Coldplay
print(playlist["Coldplay"])

# Add a new song
playlist["Usher"] = "Yeah!"

# Print the songs in the playlist
print(playlist.values())



#SETS AND TUPLES

# Create a tuple
q3_financials = (325780,1041,4271599)

# Print the tuple
print(q3_financials)

hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]

# Create a set
indie_set = {"Kings of Leon", "MGMT", "Stereophonics"}

# Convert hip_hop to a set
hip_hop_set = set(hip_hop)

# Print the indie and hip_hop sets
print(indie_set)
print(hip_hop_set)



                    #CONDITIONAL STATEMENTS#