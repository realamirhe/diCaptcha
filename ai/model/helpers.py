def remove_duplicate_tuples(token_scores):
    return list(dict(reversed(token_scores)).items())