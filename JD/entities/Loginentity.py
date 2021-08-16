from infrastructure.entity.request import RequestEntity


class LoginEntity(RequestEntity):
    def __init__(self) -> None:
        super().__init__()
        self.login_success = False