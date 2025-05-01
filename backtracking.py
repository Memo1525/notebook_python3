from random import choices


def backtrack(path, choices):
    if goal_reached(path):
        result.append(path[:])
        return
    for i in range(len(choices)):
        if is_invalid_choice(i, path):
            continue

        # Choose
        path.append(choices[i])

        # Explore
        backtrack(path, choices)

        # un-choose (backtrack)
        path.pop()

def backtrack(path, choices):
    result.append(path[:])
    return
for i in range(len(choices)):
    if is_invalid_choice(i, path):
        continue

    # Choose
    path.append(choices[i])

    # Explore
    backtrack(path, choices)

    # un-choose (backtrack)
    path.pop()