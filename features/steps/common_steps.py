from behave import given, when, then


@given(u'Användaren är på hemsidan Läslistan')
def step_user_on_laslistan(context):
    context.page.goto(context.url)
    context.page.wait_for_load_state("networkidle")


@given(u'Användaren är på Katalog-sidan')
@when(u'Användaren är på Katalog-sidan')
@then(u'Användaren är på Katalog-sidan')
def step_user_on_katalog(context):
    context.page.get_by_test_id("catalog")
    context.page.wait_for_load_state("networkidle")


@when(u'Användaren klickar på Katalog-knappen')
def step_user_clicks_katalog(context):
    context.page.get_by_test_id("catalog").click()
    context.page.wait_for_load_state("networkidle")


@when(u'Användaren klickar på Lägg till bok-knappen')
def step_user_clicks_lagg_till_bok(context):
    context.page.get_by_test_id("add-book").click()
    context.page.wait_for_load_state("networkidle")


@given(u'Användaren är på Lägg till bok-sidan')
@then(u'Användaren är på Lägg till bok-sidan')
def step_user_on_lagg_till_bok(context):
    context.page.goto(context.url)
    context.page.get_by_test_id("add-book").click()
    context.page.wait_for_load_state("domcontentloaded")


@when(u'användaren fyller i "Författare" med "{book_author}"')
def step_fyll_i_forfattare(context, book_author):
    forfattare_input = context.page.get_by_test_id("add-input-author")
    assert forfattare_input.count() > 0, "Författare fältet hittades inte"
    forfattare_input.fill(book_author)


@given(u'formuläret innehåller titel och författare')
@then(u'formulär med fält etiketten "Titel" och "Författare" visas')
def step_formular_falt_visas(context):
    titel_label = context.page.get_by_label("Titel")
    author_label = context.page.get_by_label("Författare")
    assert titel_label.is_visible()
    assert author_label.is_visible()


@given(u'användaren är på sidan "Mina böcker"')
@when(u'användaren navigerar till fliken "Mina böcker"')
def step_user_on_mina_bocker(context):
    context.page.goto(context.url)
    context.page.get_by_test_id("favorites").click()
    context.page.wait_for_load_state("domcontentloaded")


@then(u'ett välkomstmeddelande visas på skärmen')
def step_valkomstmeddelande(context):
    valkommen = context.page.locator("h2").filter(has_text="Välkommen!")
    assert valkommen.is_visible(), "Välkomstmeddelandet är inte synligt på skärmen"
    assert valkommen.count() > 0, "Välkomstmeddelandet hittades inte på skärmen"


@given(u'boken "{book_title}" inte är markerad som favorit')
def step_bok_inte_markerad_favorit(context, book_title):
    book_locator = context.page.locator(f"div.book:has-text('{book_title}')")
    assert book_locator.count() > 0, f"Boken '{book_title}' hittades inte i boklistan"
    heart = book_locator.locator("div.star.selected")
    assert heart.count() == 0, f"Boken '{book_title}' är markerad som favorit"


@when(u'användaren är på sidan "Statistik"')
def step_user_on_statistik(context):
    context.page.goto(context.url)
    context.page.get_by_test_id("statistics").click()
    context.page.wait_for_load_state("domcontentloaded")
