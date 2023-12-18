def latest(scores):
    return scores[-1]


def personal_best(scores):
    max_score = 0
    for score in scores:
        max_score = score if max_score < score else max_score
    return max_score


def personal_top_three(scores):
    scores = sorted(scores, reverse=True)
    return scores[0:3]
