def knapsack_with_reps(w, weight_, cell_):
    d = [0] * (w + 1)
    for w in range(1, w + 1):
        for i in range(len(weight_)):
            if weight_[i] <= w:
                d[w] = max(d[w], d[w - weight_[i]] + cell_[i])
    return d[w]


def knapsack_without_reps(w, weight_, cell_):
    d = [[0] * (len(weight_) + 1) for _ in range(w + 1)]

    for i in range(len(weight_)):
        for w in range(1, w + 1):
            d[w][i + 1] = d[w][i]
            if weight_[i] <= w:
                d[w][i + 1] = max(d[w][i + 1], d[w - weight_[i]][i] + cell_[i])

    solution = []
    w = w
    elem = len(weight_)
    for i in range(len(weight_), 0, -1):
        if d[w][i] == d[w - weight_[i - 1]][i - 1] + cell_[i - 1]:
            solution.append(1)
            w -= weight_[i - 1]
        else:
            solution.append(0)
    solution.reverse()
    return d[w][len(weight_)], solution


def knapsack_bu(w, weight_, cell_):
    with_rep = knapsack_with_reps(w, weight_, cell_)
    without_rep = knapsack_without_reps(w, weight_, cell_)
    return with_rep, without_rep


if __name__ == "__main__":
    W = 10
    weight = [6, 3, 4, 2]
    cell = [30, 14, 16, 9]
    result = knapsack_bu(W, weight, cell)
    print("С повторением =", result[0])
    print("Без повторения =", result[1][0])
    print("Решение =", result[1][1])
