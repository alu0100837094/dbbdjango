from lettuce import step,world

@step(u'I am at "([^"]*)"')
def i_am_at_url(step, url):
    world.browser.get(url)
