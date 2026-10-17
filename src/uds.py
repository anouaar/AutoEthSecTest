def build_request(sid, data):
    return bytes([sid] + data)
