from lib.artist_repository import ArtistRepository
from lib.artist import Artist

'''
When I call #all artists method
I get a list of all artists
'''
def test_get_artists(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
        ]
    
'''
When I call #create
I can create a new artist
'''
def test_create_artist(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = ArtistRepository(db_connection)
    artist = Artist(None, 'Wild nothing', 'Indie')
    repository.create(artist)
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
        ]

# '''
# When I call #get_artist_by_id
# I get that artist 
# '''
# def test_get_artist_by_id(db_connection):
#     db_connection.seed('seeds/music_library.sql')
#     repository = ArtistRepository(db_connection)
#     artist = repository.get_artist_by_id(1)
#     assert artist == Artist(1, 'Pixies', 'Rock')