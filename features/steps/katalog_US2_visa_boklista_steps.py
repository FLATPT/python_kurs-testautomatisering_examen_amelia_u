from behave import then


@then(u'en boklistan visas på skärmen')
def step_show_book_list(context):
    book_list = context.page.locator("div.book")
    assert book_list.count() > 0, "Boklistan visas inte på skärmen"
