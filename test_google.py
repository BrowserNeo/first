
import pytest


@pytest.fixture()
def before_each(request):
    print("Called before each test " + request.node.name)



@pytest.fixture(scope='session', autouse=True)
def init_browser(request):
    print("Called before test " + request.node.name)


@pytest.fixture()
def message():
    return "This is fIrst message"


def firefox():
    return ""


def chrome():
    return ""


def chrome_mobile():
    return ""


@pytest.fixture()
def client():
    client = 123
    print("Client ready")
    yield client
    print("Delete client")




def test_first(before_each):
    assert 1 == 1


def test_second(before_each):
    assert 1 == 2, "One not true two!"


def test_message(message):
    print(message)
    assert "message" in message


def test_client(client):
    assert client == 321