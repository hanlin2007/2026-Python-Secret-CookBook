def make_pizza(size: int,*tips: str) -> str:
    tip_list: list[str] = []
    for tip in tips:
        tip_list.append(tip)
    return f"{size}{tip_list}"