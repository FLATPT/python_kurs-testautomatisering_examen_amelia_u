from playwright.sync_api import sync_playwright


# Körs innan alla scenarier startar - starta Playwright och webbläsaren här, stäng den i after_all
def before_all(context):
    #  Starta Playwright och webbläsaren här, stäng den i after_all
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)


# Körs innan varje scenario startar - öppna en ny sida, stäng den i after_scenario
def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_default_timeout(10000)
    context.url = "https://tap-ht25-testverktyg.github.io/exam/"
    context.page.goto(context.url)


# Kör direct efter varje scenario - clean up
def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()


# Kör efter alla scenarios are avslutats - clean up
def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
