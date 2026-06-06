from behave import given, then


@given(u'att katalogen innehåller {antal:d} böcker')
def step_katalog_innehaller_antal_bocker(context, antal):
    context.page.get_by_test_id("catalog").click(force=True)
    book_items = context.page.locator("div.book")
    actual_count = book_items.count()
    assert actual_count == antal, f"Förväntade {antal} böcker i katalogen"
    context.book_count = actual_count # Sparar det faktiska antalet böcker i katalogen för senare jämförelse

@then(u'ska texten "Listan har {antal:d} böcker." visas')
def step_texten_visas(context, antal):
    actual_count = context.book_count # Hämtar det faktiska antalet böcker som sparades i @given-steget
    assert actual_count == antal, f"Förväntade {antal} böcker men hittade {actual_count}"
    expected_text = f"Listan har {actual_count} böcker."
    text_element = context.page.locator("p").filter(has_text=expected_text)
    assert text_element.is_visible(), f'Antal böcker i Statistiken matchar inte antalet i Katalogen'