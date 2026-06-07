from behave import given, when, then


@given(u'att en boklista lista visas på Katalog-sidan')
def step_show_book_list(context):
    context.page.get_by_test_id("catalog")
    book_list = context.page.locator("div.book")
    assert book_list.count() > 0, "Boklistan visas inte på skärmen"


@when(u'Användaren klickar på raden där "{book_title}" finns på listan')
def step_click_bok_rad(context, book_title):
    book_locator = context.page.get_by_test_id(f"star-{book_title}")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    book_locator.first.click()
    context.page.wait_for_timeout(500)  # Vänta en kort stund för att säkerställa att klicket har registrerats


@then(u'ett hjärtikon visas bredvid "{book_title}" i boklistan')
def step_hjartikon_visas(context, book_title):
    book_locator = context.page.get_by_test_id(f"star-{book_title}")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    book_locator.first.wait_for(state="visible")
    heart = book_locator.first.get_attribute("class")
    assert "selected" in heart, f"Hjärtikonen visas inte bredvid '{book_title}'"


@then(u'markerar på så sätt boken "{book_title}" som favorit')
def step_bok_markerad_favorit(context, book_title):
    book_locator = context.page.locator(f"div.book:has-text('{book_title}')")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    heart = book_locator.locator("div.star.selected")
    assert heart.count() > 0, f"Boken '{book_title}' är inte markerad som favorit"
