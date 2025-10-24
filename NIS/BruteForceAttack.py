import itertools
import time
import sys

def attempt_bruteforce(secret, max_len=6, alphabet='abcdefghijklmnopqrstuvwxyz0123456789'):
    t0 = time.perf_counter()
    tries = 0

    for length in range(1, max_len + 1):
        for chars in itertools.product(alphabet, repeat=length):
            tries += 1
            candidate = ''.join(chars)
            if candidate == secret:
                elapsed = time.perf_counter() - t0
                return True, tries, elapsed, candidate

    elapsed = time.perf_counter() - t0
    return False, tries, elapsed, None


pw = input("Enter password to search for (max 6 chars): ").strip()

if len(pw) == 0:
    print("No password entered. Exiting.")
    sys.exit(1)
if len(pw) > 6:
    print("Password longer than 6 characters. Please run again with a password of length ≤ 6.")
    sys.exit(1)

charset = "abcdefghijklmnopqrstuvwxyz0123456789"
max_length = 6

try:
    found, attempts, elapsed, matched = attempt_bruteforce(pw, max_length, charset)
except KeyboardInterrupt:
    print("\nInterrupted by user. Partial results may be incomplete.")
    sys.exit(1)

if found:
    print(f"Password found: '{matched}'")
    print(f"Attempts: {attempts}")
    print(f"Elapsed time: {elapsed:.4f} seconds")
else:
    print("Password NOT found with current charset/max_length.")
    print(f"Attempts performed: {attempts}")
    print(f"Elapsed time: {elapsed:.4f} seconds")