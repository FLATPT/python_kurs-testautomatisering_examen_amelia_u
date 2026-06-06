from behave import given, when, then
from src.laslistan.bookstore import Book, BookStore


@given(u'att katalogen innehåller boken "{book_title}" av "{book_author}"')
def step_katalog_innehaller_bok(context, book_title, book_author):
    # Användare är på Lägg till bok-sidan via "Given Användaren är på Lägg till bok-sidan"
    # Lägg till boken i katalogen via UI
    context.page.get_by_test_id("add-input-title").fill(book_title)
    context.page.get_by_test_id("add-input-author").fill(book_author)
    context.page.get_by_test_id("add-submit").click()
    context.page.wait_for_load_state("domcontentloaded")
    

@when(u'användaren fyller i "Titel" med "{book_title}"')
def step_fyll_i_titel(context, book_title):
    titel_input = context.page.get_by_test_id("add-input-title")
    assert titel_input.count() > 0, "Titel fältet hittades inte"
    titel_input.fill(book_title)


@when(u'användaren klickar på "Lägg till ny bok"-knappen')
def step_click_lagg_till_ny_bok_knapp(context):
    add_book_button = context.page.get_by_test_id("add-submit")
    assert add_book_button.count() > 0, "Lägg till bok-knappen hittades inte"
    add_book_button.click()
    context.page.wait_for_load_state("domcontentloaded")


@then(u'boken "{book_title}" sparas i katalogen igen')
def step_bok_sparas_i_katalogen_igen(context, book_title):
    # Navigera till Katalog-sida och verifiera att boken finns
    context.page.get_by_test_id("catalog").click()
    books = context.page.locator(f"text={book_title}")
    assert books.count() > 1, f"Katalogen innehåller 1 exemplar av '{book_title}'"


@then(u'felmeddelande om att boken redan finns i katalogen visas inte')
def step_felmeddelande_visas_inte(context):
    error_message = context.page.get_by_test_id("add-error")
    assert error_message.count() == 0, f"Felmeddelande visas men ska inte visas: '{error_message.inner_text()}'"