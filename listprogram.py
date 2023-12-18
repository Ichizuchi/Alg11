def list_bottom_up(x):
    n = len(a)
    D = [1] * n

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1

    return max(D)


def with_prev(prev, m_index):
    l = []
    while True:
        l.append(m_index)
        if prev[m_index] == -1:
            break
        m_index = prev[m_index]
    l.reverse()
    return l


def without_prev(d, ans, m_index, x):
    l = []
    while True:
        l.append(m_index)
        if ans == 1:
            break
        ans -= 1
        while True:
            m_index -= 1
            if d[m_index] == ans and x[m_index] < x[l[-1]]:
                break
    l.reverse()
    return l


def list_bottom_up_2(x):
    n = len(a)
    d = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j

    ans = 0
    max_index = 0
    for i in range(n):
        if ans < d[i]:
            ans = d[i]
            max_index = i

    list_using_prev = with_prev(prev, max_index)
    list_without_prev = without_prev(d, ans, max_index, a)

    return ans, (list_using_prev, list_without_prev)


if __name__ == "__main__":
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    print(list_bottom_up(a))
    result = list_bottom_up_2(a)
    print(result[0])
    print("C повторением:", result[1][0])
    print("Без повторения:", result[1][1])
