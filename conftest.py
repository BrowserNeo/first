@pytest.fixture()
def driver():
    pass



@pytest.fixture()
def config(driver):
    pass


@pytest.fixture()
def firefox(config):
    return ""

@pytest.fixture()
def chrome(config):
    return ""


@pytest.fixture()
def chrome_mobile(config):
    return ""