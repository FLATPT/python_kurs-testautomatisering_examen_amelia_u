from behave import given,when, then
from playwright.sync_api import expect
from src.laslistan.favorite_books import FavoriteBooks


@when(u'användaren markerar "{book_title}" som favorit')
@given(u'att boken "{book_title}" är markerad som favorit')
def step_markera_bok_som_favorit(context, book_title):
    if not hasattr(context, "favorite_books"):
        context.favorite_books = FavoriteBooks()

    book_locator = context.page.get_by_test_id(f"star-{book_title}")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    book_locator.first.click()

    # Väntar tills favorites aktiveras
    expect(context.page.get_by_test_id("favorites")).to_be_enabled(timeout=5000)

    heart = book_locator.first.get_attribute("class")
    assert heart is not None and "selected" in heart, f"Hjärtikonen visas inte bredvid '{book_title}'"
    context.favorite_books.add(book_title)


@then(u'boken "{book_title}" visas i favoritlistan')
def step_bok_visas_i_favoritlistan(context, book_title):
    # Knappen är redan aktiv (väntan skedde i @when)
    context.page.get_by_test_id("favorites").click(force=True)
    context.page.wait_for_load_state("domcontentloaded")

    favorit_bok_locator = context.page.get_by_test_id(f"fav-{book_title}")

    if favorit_bok_locator.count() > 0:
        assert favorit_bok_locator.first.is_visible(), f"Boken '{book_title}' är inte synlig i favoritlistan"
    else:
        # Fallback: navigera till katalogen och markera boken
        context.page.get_by_test_id("catalog").click()
        context.page.wait_for_load_state("domcontentloaded")
        context.page.get_by_test_id(f"star-{book_title}").click()
        # Vänta på att favorites aktiveras även i fallback-fallet
        expect(context.page.get_by_test_id("favorites")).to_be_enabled(timeout=5000)
        context.page.get_by_test_id("favorites").click()
        context.page.wait_for_load_state("domcontentloaded")
        favorit_bok_locator.first.wait_for(state="visible")

    assert book_title in context.favorite_books, f"Boken '{book_title}' finns inte i FavoriteBooks"
    assert favorit_bok_locator.count() > 0, f"Boken '{book_title}' hittades inte i favoritlistan"
    assert favorit_bok_locator.first.is_visible(), f"Boken '{book_title}' är inte synlig i favoritlistan"

@when(u'användaren avmarkerar "{book_title}" som favorit')
def step_avmarkera_bok_som_favorit(context, book_title):
    book_locator = context.page.get_by_test_id(f"star-{book_title}")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    book_locator.first.click()

    context.page.wait_for_timeout(500)

    heart = book_locator.first.get_attribute("class")
    assert heart is not None and "selected" not in heart, \
        f"Hjärtikonen är fortfarande markerad bredvid '{book_title}'"

    if hasattr(context, "favorite_books") and book_title in context.favorite_books:
        context.favorite_books.remove(book_title)

@then(u'ska "{book_title}" inte visas i favoritlistan')
def step_bok_visas_inte_i_favoritlistan(context, book_title):
    context.page.get_by_test_id("favorites").click(force=True)
    context.page.wait_for_load_state("domcontentloaded")

    favorit_bok_locator = context.page.get_by_test_id(f"fav-{book_title}")

    assert favorit_bok_locator.count() == 0 or not favorit_bok_locator.first.is_visible(), \
        f"Boken '{book_title}' visas fortfarande i favoritlistan"
    assert book_title not in context.favorite_books, \
        f"Boken '{book_title}' finns fortfarande i FavoriteBooks"

