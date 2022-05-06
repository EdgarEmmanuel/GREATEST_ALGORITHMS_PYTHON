def match():
    score = 0

    while True:
        goal = yield score
        score += goal


match_coroutine = match()
print(next(match_coroutine))

print(match_coroutine.send(3))

print(match_coroutine.send(2))

