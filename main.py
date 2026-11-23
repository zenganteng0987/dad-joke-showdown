"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt.

Chosen joke beats the runner-up ("My son asked why I talk to the
toaster every morning. I said someone has to butter it up before
breakfast.", 108 chars): its steaks/stakes pun lands on first read,
the ladder-to-dinner setup is fresher than the worn "butter up" idiom,
it is tighter at 88 chars, and its two-beat rhythm reads naturally
aloud across a dinner table, punchline last.
"""

JOKE = "I asked my son why he brought a ladder to dinner. He said he heard the steaks were high."


def main() -> None:
    joke = JOKE
    if not joke or not joke.strip():
        raise SystemExit("entry must not be empty")
    if len(joke) > 200:
        raise SystemExit(f"entry too long: {len(joke)} characters (max 200)")
    print(joke)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
