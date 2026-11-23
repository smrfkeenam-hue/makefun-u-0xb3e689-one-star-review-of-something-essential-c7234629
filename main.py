import os

LINE = (
    "One star. Gravity has never once let me drop something gently. "
    "It just waits all day for the one thing I cannot afford to break."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
