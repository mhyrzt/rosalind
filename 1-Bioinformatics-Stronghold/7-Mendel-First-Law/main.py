def prob(k, m, n):
    total = k + m + n
    total_pairs = total * (total - 1) / 2

    # Calculate probabilities for each mating pair
    prob_AA_AA = k * (k - 1) / 2 / total_pairs
    prob_AA_Aa = k * m / total_pairs
    prob_AA_aa = k * n / total_pairs
    prob_Aa_Aa = m * (m - 1) / 2 / total_pairs
    prob_Aa_aa = m * n / total_pairs

    return (
        prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa * 3 / 4 + prob_Aa_aa * 1 / 2
    )


k, m, n = list(map(int, input().split()))
print(prob(k, m, n))