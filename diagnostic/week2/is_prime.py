def is_prime(n):
    if n<2:                          # when n is less than 2
        return False
    for i in range(2, n // 2 + 1):
        if i % n== 0:                      # when i divides n exactly
            return False
    return True

print(is_prime(1), is_prime(2), is_prime(15), is_prime(17))