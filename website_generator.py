import json

def generate_website():
  """ This function will generate a html page based on the data stored in the data.json
  file."""

  with open('data.json', 'r') as file:
    data = json.load(file)

  with open('_static/index_template.html', 'r') as file:
    template = file.read()

  movie_grid = ''
  for movie_title, movie_data in data.items():
    rating = movie_data['rating']
    poster_url = movie_data['poster url']
    release_year = movie_data['year of release']

    movie_html = f"""
      <li class='movie'>
          <h2 class='movie-title'>{movie_title}</h2>
          <img class='movie-poster' src='{poster_url}' alt='{movie_title} Poster'>
          <p class='movie-text'>Release Year: {release_year}</p>
          <p class='movie-text'>Rating: {rating}</p>
      </li>
    """
    movie_grid += movie_html

  html = template.replace('__TEMPLATE_MOVIE_GRID__', movie_grid)

  title = 'My Movie App'
  html = html.replace('__TEMPLATE_TITLE__', title)

  with open('_static/index.html', 'w')as file:
    file.write(html)

  print('Website was generated successfully')

