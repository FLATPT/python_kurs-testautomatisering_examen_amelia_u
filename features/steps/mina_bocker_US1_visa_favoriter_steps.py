from behave import given, then


@given(u'att användaren har markerat minst en bok som favorit i katalogen')
def step_bok_markerad_favorit(context):
    context.fav_book_locator = context.page.locator("li.book[data-testid^='fav-']")
    if context.fav_book_locator.count() == 0:
        # Om ingen favoritbok är markerad, markera den första boken i katalogen som favorit
        context.page.get_by_test_id("catalog").click()
        context.page.wait_for_load_state("domcontentloaded")
        hjartikon_locator = context.page.locator("[data-testid^='star-']").first
        if hjartikon_locator.count() > 0:
            hjartikon_locator.click()
            context.page.wait_for_timeout(500)  # Vänta en kort stund för att säkerställa att klicket har registrerats
            # Gå till "Mina böcker" sidan för att se den markerade favoritboken
            context.page.get_by_test_id("favorites").click()
            context.page.wait_for_load_state("domcontentloaded")
            context.fav_book_locator.first.wait_for(state="visible")
    assert context.fav_book_locator.count() > 0, "Ingen favoritbok visas"


@then(u'en ordnade lista över favoritböcker visas')
def step_favoritbocker_visas(context):
    book_list = context.page.get_by_test_id("ol.book-list")
    if context.fav_book_locator.count() > 0:
        # återanvänder koden i @given för att säkerställa att favoritböckerna är synliga
        assert context.fav_book_locator.first.is_visible(), "Favoritböckerna är inte synliga på skärmen"
    else:
        # Om ingen favoritbok är markerad, markera den första boken i katalogen som favorit
        context.page.get_by_test_id("catalog").click()
        context.page.wait_for_load_state("domcontentloaded")
        hjartikon_locator = context.page.locator("[data-testid^='star-']").first
        hjartikon_locator.click()
        context.page.wait_for_timeout(500)
        context.page.get_by_test_id("favorites").click()
        context.page.wait_for_load_state("domcontentloaded")
        context.fav_book_locator.first.wait_for(state="visible")
        # Gå till "Mina böcker" sidan visa en ordnad lista på markerade favorit böckerna
        assert book_list.count() > 0, "Ingen ordnad boklista visas"
