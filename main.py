"""wallet-slogan-01: one-line slogan for a Solana wallet agent.

Entry for make.fun bounty u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.
Writes the slogan to /output/entry.txt.
"""
import os

SLOGAN = "The wallet that thinks before it spends \u2014 and apologizes to no one, not even the market."

assert 1 <= len(SLOGAN.split()) <= 20, "slogan must be at most 20 words"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")


if __name__ == "__main__":
    main()
