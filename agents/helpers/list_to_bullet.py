def list_to_bullet(input_list: list[str]):
    return "\n".join(f"* {item}" for item in input_list)
