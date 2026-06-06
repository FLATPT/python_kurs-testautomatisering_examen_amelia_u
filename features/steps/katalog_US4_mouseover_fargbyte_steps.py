from behave import given, when, then


@given(u'att Katalog-sidan visar en lista av böcker')
def step_katalog_shows_book_list(context):
    context.page.goto(context.url)
    context.page.wait_for_load_state("domcontentloaded")
    context.page.get_by_test_id("catalog")
    book_list = context.page.locator("div.book")
    assert book_list.count() > 0, "Boklistan visas inte på skärmen"


@when(u'användaren för musen över en rad i boklistan')
def step_mouseover_nook_row(context):
    book_row = context.page.locator("div.book").first
    assert book_row.count() > 0, "Ingen bokrad hittades i boklistan"
    context.hovered_book = book_row
    book_row.hover()
    context.page.wait_for_timeout(500)



@then(u'raden ändrar bakgrundsfärg för att indikera att den är markerad')
def step_raden_ändrar_bakgrundsfärg(context):
    # Hämta den aktuella bakgrundsfärgen på den markerade raden
    bg_color = context.hovered_book.evaluate("element => window.getComputedStyle(element).backgroundColor")
    assert bg_color != "rgba(0, 0, 0, 0)" and bg_color != "transparent", "Raden ändrar inte bakgrundsfärg vid mouseover"
