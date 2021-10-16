from application import echo, hello

def test_echo():
    assert echo("John") == {"name": "John"}