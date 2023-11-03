def waterjug(s, t, m, n):
    while s != 0 and t != n:
        if s > t:
            s, t = t, s
            m, n = n, m
        t = t - min(t, n - s)
        s = s + min(t, m - s)
    return t

if __name__ == "__main__":
    jug1_capacity = 3
    jug2_capacity = 5
    target_amount = 4
    result = waterjug(0, target_amount, jug1_capacity, jug2_capacity)
    print(f"Minimum steps required to measure {target_amount} liters: {result}")
