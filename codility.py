def solution(S):
    idx = {}

    def digram(l):
        return len(idx[l]) > 1

    for i in range(len(S)):
        l = S[i]
        if l in idx.keys():
            idx[l].append(i)
        else:
            idx[l] = [i]

    digram_distance = -1
    digrams = list(filter(digram, idx.keys()))
    print(digrams)

    for k in digrams:
        indexes = idx[k]
        for i in sorted(indexes):
            if i <= len(S)-2:
                if S[i+1] in digrams:
                    next_l = S[i+1]
                    for j in idx[next_l]:
                        if S[j-1] == S[i] and j > i:
                            len_diff = abs(j - i - 1)
                            print(S[i],  i, next_l, j,
                                  digram_distance, len_diff)
                            if digram_distance < len_diff:
                                digram_distance = len_diff

    return digram_distance


print(solution("codility"))
