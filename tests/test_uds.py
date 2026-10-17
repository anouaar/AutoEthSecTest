from src.uds import build_request

def test_build_request():
    assert build_request(0x10, [0x01]) == b'\x10\x01'
