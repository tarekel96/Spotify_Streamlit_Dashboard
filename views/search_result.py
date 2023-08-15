import random

def artist_search_result(item) -> str:
    name, genres, images, followers = item['name'], item['genres'], item['images'], item['followers']
    image = random.choices(images)[0]
    genres_list = ''
    for genre in genres:
        genres_list += f'<li>{genre}</li>'
    return f'''
    <div>
        <h3>Name: {name}</h3>
        <img src={image['url']} width={image['width']} height={image['height']}/>
        <h4>Followers: {followers}</h4>
        <ul>Genres: {genres}</ul>
    </div>
    '''