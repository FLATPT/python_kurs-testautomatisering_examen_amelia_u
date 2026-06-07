from behave import given, when, then


@given(u'Användaren filler i titel och författare i formuläret')
def step_fill_in_title_and_author(context):
    context.page.get_by_test_id("add-input-title").fill("Why Your Tests Are Lying to You")
    context.page.get_by_test_id("add-input-author").fill("Kent Backdoor")


@when(u'användaren klickar på knappen "Lägg till ny bok"')
def step_klicka_lagg_till_ny_bok(context):
    add_button = context.page.get_by_role("button", name="Lägg till ny bok")
    assert add_button.is_enabled(), "Knappen 'Lägg till ny bok' är inaktiverad"
    add_button.click()


@then(u'boken sparas i katalogen')
def step_sparas_i_katalogen(context):
    book_title = "Why Your Tests Are Lying to You"
    book_author = "Kent Backdoor"
    context.page.get_by_test_id("catalog").click()
    books = context.page.locator(f"text={book_title}")
    author = context.page.locator(f"text={book_author}")
    books.first.wait_for(state="visible")
    assert books.count() > 0, f"Boken '{book_title}' sparades inte i katalogen"
    assert author.count() > 0, f"Författaren '{book_author}' sparades inte i katalogen"


@then(u'Formuläret rensas/återställs så att fälten "Titel" och "Författare" är tomma')
def step_formularet_rensas(context):
    context.page.get_by_test_id("add-book").click()
    title = context.page.get_by_test_id("add-input-title")
    author = context.page.get_by_test_id("add-input-author")
    assert title.input_value() == "", "Titel-fältet är inte tomt efter att ha lagt till en bok"
    assert author.input_value() == "", "Författare-fältet är inte tomt efter att ha lagt till en bok"
