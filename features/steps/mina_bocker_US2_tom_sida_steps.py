from behave import when, then


@when(u'att inga böcker är markerade som favoriter i katalogen')
def step_inga_favorit_bocker(context):
    book_list = context.page.locator("[data-testid^='fav-']").first
    assert book_list.count() == 0, 'Det finns böcker markerade som favoriter i katalogen'


@then(u'ska favoritlistan vara tom')
def step_favoritlistan_tom(context):
    favoritlistan = context.page.get_by_test_id("ol.book-list")
    assert favoritlistan.count() == 0, 'Favoritlistan är inte tom när inga böcker är markerade som favoriter'
