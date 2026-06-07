from behave import when


@when(u'Katalog-knappen är inaktiverad')
def step_katalog_button_is_disabled(context):
    context.page.get_by_test_id("catalog").is_disabled()
    context.page.wait_for_load_state("networkidle")
