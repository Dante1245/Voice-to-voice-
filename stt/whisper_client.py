def get_live_stt():
    while True:
        text = input("You say: ")
        if text:
            yield text
