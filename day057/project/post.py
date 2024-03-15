class Post:

    def __init__(self, post_dict):
        self.post_id = post_dict["id"]
        self.title = post_dict["title"]
        self.subtitle = post_dict["subtitle"]
        self.body = post_dict["body"]
