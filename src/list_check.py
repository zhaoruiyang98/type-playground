def plus_one(x: list[int]) -> None:
    for i, _ in enumerate(x):
        x[i] += 1


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [1, "a"]  # type auto inference, list[Any]
    c = ["a", "b"]
    plus_one(a)
    plus_one(b)
    plus_one(c)  # error
