from typing import Any

import yaml


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0
    for i in range(0, len(tickets)):
        m = min(tickets[i], tickets[k])
        if i > k and m == tickets[k]:
            m = m - 1
        seconds_elapsed += m

    return seconds_elapsed


if __name__ == "__main__":
    with open("../time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
