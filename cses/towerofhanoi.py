final_arr = []


def t_o_h(k: int, fromD: int, to: int, aux: int) -> None:
    """TOWER OF HANOI

    Args:
        k (int): no of disks

    Returns:
        int: minimum number of moves
    """
    if k == 1:
        final_arr.append([fromD, to])
        return
    t_o_h(k - 1, fromD, aux, to)
    final_arr.append([fromD, to])
    t_o_h(k - 1, aux, to, fromD)


if __name__ == "__main__":
    n = int(input())
    # exec
    t_o_h(n, 1, 3, 2)
    print(len(final_arr))
    for i in final_arr:
        print(*i)
