from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When I call #all on the AlbumRepository
I get all the albums back in a list
'''
def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2), 
        Album(5, 'Bossanova', 1990, 1), 
        Album(6, 'Lover', 2019, 3), 
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

'''
When I call #create
I create an album in the database
'''
def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test title', 2025, 1)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2), 
        Album(5, 'Bossanova', 1990, 1), 
        Album(6, 'Lover', 2019, 3), 
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Test title', 2025, 1)
    ]

'''
When I call #get_album_by_id
I get that specific album
'''
def test_get_album_by_id_with_artist_name(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    album = repository.get_album_by_id_with_artist_name(1)
    assert album == Album(None, 'Doolittle', 1989, None, 'Pixies')

