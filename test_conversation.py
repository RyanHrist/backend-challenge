import requests


class Test:
    def __init__(self):
        self.run_all_tests()

    def test_incorrect_id(self):
        print("Testing incorrect ID exception...")
        print('Output:')
        resp = requests.post(f"http://localhost:5000/messages?sender=anson&message=I'm%20a%20teapot&conversation_id"
                             f"=incorrect_id_type")
        print(resp.text)

    def test_create_messsage(self):
        print("Testing create new message with POST...")
        print('Output:')
        resp = requests.post(f"http://localhost:5000/messages?sender=anson&message=I'm%20a%20teapot&conversation_id"
                             f"=f283048c-7f59-4c68-9d00-5ac2fc5222e4")
        print(resp.text)

    def test_create_conversation(self):
        print("Testing create conversation with POST...")
        print('Output:')
        resp = requests.post(f"http://localhost:5000/messages?sender=david&message=Short%20and%20stout&conversation_id"
                             f"=f283048c-7f59-4c68-9d00-5ac2fc5222e4")
        print(resp.text)

    def test_get_conversation(self):
        print("Testing retreive conversation by ID...")
        print('Output:')
        resp = requests.get(f"http://localhost:5000/conversations/f283048c-7f59-4c68-9d00-5ac2fc5222e4")
        print(resp.text)

    def run_all_tests(self):
        self.test_incorrect_id()
        self.test_create_messsage()
        self.test_create_conversation()
        self.test_get_conversation()


Test()
