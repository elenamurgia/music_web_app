from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        return [Album(row['id'], row['title'], row['release_year'], row['artist_id']) for row in rows]
    
    def create(self, album):
        self._connection.execute("INSERT INTO albums(title, release_year, artist_id) VALUES(%s, %s, %s)", [album.title, album.release_year, album.artist_id])
        return None
    
    def get_album_by_id_with_artist_name(self, album_id):
        rows = self._connection.execute(
            "SELECT albums.title, albums.release_year, artists.name \
            FROM albums \
            JOIN artists \
            ON artists.id = albums.artist_id \
            WHERE albums.id = %s", [album_id])
        return Album(None, rows[0]['title'], rows[0]['release_year'], artist_name = rows[0]['name'])