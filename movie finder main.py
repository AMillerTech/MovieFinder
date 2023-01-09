movie = "0"

def find_movie(movie):
  with open(r"Movies_collection.txt", 'r') as file:
    for one_no, line in enumerate(file):
      if movie in line.lower():
        print(line)
        continue
      if line == "":
        break

def user_tree():
  movie = input("Please type part of the movie title you're looking for and press enter. \n When you are done, type /e: ")
  print()
  if movie == "":
    exit()
  else:
    movie = movie.lower()
    find_movie(movie)
    
while not movie == "/e":
  user_tree()