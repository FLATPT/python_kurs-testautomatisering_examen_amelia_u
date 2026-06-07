from behave import then


@then(u'Lägg till ny bok-knappen ska vara inaktiverad')
def step_knappen_inaktiverad(context):
    add_book_button = context.page.get_by_test_id("add-submit")
    assert add_book_button.is_disabled(), "Lägg till ny bok-knappen är inte inaktiverad när fälten är tomma"
