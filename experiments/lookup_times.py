"""Compare membership-test cost of a set (hash lookup) versus a list (linear scan).

Motivation: solver candidates are tracked as sets so that "is digit d still
possible?" is O(1) on average rather than O(n).
"""
import timeit

SIZES = (9, 100, 10_000)

print(f"{'n':>8} {'set (µs)':>10} {'list (µs)':>11}")
for n in SIZES:
    items = list(range(n))
    as_set = set(items)
    missing = -1  # worst case for the list: scans every element
    t_set = timeit.timeit(lambda: missing in as_set, number=100_000) * 10
    t_list = timeit.timeit(lambda: missing in items, number=100_000) * 10
    print(f"{n:>8} {t_set:>10.3f} {t_list:>11.3f}")
