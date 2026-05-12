from playwright.sync_api import Page, expect

def test_has_form(page:Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The Chronicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator("li")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chronicles of Geronimo (the cat) by Geronimo"

    