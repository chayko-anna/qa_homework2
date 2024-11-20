from selene import browser, be, have


def test_first(browser_settings):
    browser.open("https://google.com/ncr")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_second(browser_settings):
    browser.open("https://google.com/ncr")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene; User-oreented web UI vrowser tests on Python'))