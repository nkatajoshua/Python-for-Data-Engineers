                  #BUILT-IN FUNCTIONS#

course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Find the number of courses
num_courses = len(course_completions)
print(num_courses)

most_popular_course = "Introduction to dbt"

# How many characters are in most_popular_course?
title_length = len(most_popular_course)
print(title_length)

# Print the total number of course completions
print(sum(course_completions))