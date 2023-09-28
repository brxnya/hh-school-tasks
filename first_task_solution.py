def find_min_cookies(n, m, cookies):
    min_cookies = 1
    max_cookies = max(cookies)
    result = 0

    while min_cookies <= max_cookies:
        k = (min_cookies + max_cookies) // 2
        eating_time = 0
        for cookie_count in cookies:
            eating_time += (cookie_count // k)
            if cookie_count % k != 0:
                eating_time += 1

        if eating_time <= m:
            result = k
            max_cookies = k - 1
        else:
            min_cookies = k + 1

    return result


n, m = map(int, input().split())
cookies = []
for _ in range(n):
    cookies.append(int(input()))

print(find_min_cookies(n, m, cookies))
