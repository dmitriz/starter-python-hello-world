def hello():
    """Return a greeting message."""
    return "Hello, world!"
if __name__ == "__main__":
    try:
        print(hello())
    except Exception as e:
        print(f"Error generating greeting: {e}")
        raise SystemExit(1) from e
    print(hello())
