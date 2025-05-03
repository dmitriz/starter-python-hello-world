    GREETING = "Hello, world!"  # Centralized configuration

def hello() -> str:
    """Return standardized greeting message.

    Returns:
        str: Configured greeting string
    """
    return GREETING

    if __name__ == "__main__":
        try:
            print(hello())
        except Exception as e:  # Basic error containment
            print(f"Error generating greeting: {e}")
            raise SystemExit(1) from e
