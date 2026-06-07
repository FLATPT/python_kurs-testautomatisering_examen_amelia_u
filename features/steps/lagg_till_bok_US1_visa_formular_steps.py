from behave import then


@then(u'knappen med texten "Lägg till ny bok" visas')
def step_knapp_lagg_till_bok_visas(context):
    add_button = context.page.get_by_role("button", name="Lägg till ny bok")
    assert add_button is not None
