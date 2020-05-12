def test_title(browser, get_url):
    browser.get(get_url)
    title = browser.title
    exp_title = 'Your Store'
    assert title == exp_title, 'Title does not match. Expected: {}. Got: {}'.format(exp_title, title)

