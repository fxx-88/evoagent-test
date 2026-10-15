def greet(name: str) -> str:
    return f"Hello, {name.strip() or 'Guest'}!"


if __name__ == "__main__":
    print(greet("EvoAgent"))
