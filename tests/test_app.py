from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get the albums from the /albums page
"""
def test_get_albums(page, test_web_address, db_connection): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tag = page.locator("h2")
    paragraph_tag = page.locator("p")

    expect(h2_tag).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
        "Title: Waterloo",
        "Title: Super Trouper",
        "Title: Bossanova",
        "Title: Lover",
        "Title: Folklore",
        "Title: I Put a Spell on You",
        "Title: Baltimore",
        "Title: Here Comes the Sun",
        "Title: Fodder on My Wings",
        "Title: Ring Ring"
    ])

    expect(paragraph_tag).to_have_text([
        "Released: 1989",
        "Released: 1988",
        "Released: 1974",
        "Released: 1980",
        "Released: 1990",
        "Released: 2019",
        "Released: 2020",
        "Released: 1965",
        "Released: 1978",
        "Released: 1971",
        "Released: 1982",
        "Released: 1973"
    ])

"""
We can get the album by id from the /albums/<id> page
"""
def test_get_albums_by_id(page, test_web_address, db_connection): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")

    expect(h1_tag).to_have_text([
        "Doolittle"
    ])

    expect(paragraph_tag).to_have_text([
        "Release year: 1989\nArtist: Pixies"
    ])




# === End Example Code ===
