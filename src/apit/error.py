class ApitError(Exception):
    pass


class ApitStoreConnectionError(ApitError):
    def __init__(self, error_message: str) -> None:
        super().__init__(
            f"Connection to Apple Music/iTunes Store failed due to error: ${error_message}"
        )
