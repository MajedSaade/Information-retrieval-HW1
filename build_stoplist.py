from pathlib import Path
from collections import Counter
import re

# --- Folder configuration ---
# "." = current directory (build_stoplist)
# ".." = go one level up (IR_HW1_315273102)
# "wiki_docs" = folder containing your Wikipedia files
DOCS_DIR = Path(".") /"wiki_docs"
OUT_FILE = Path(".") / "stoplist_top50.txt"

# --- Tokenization pattern (letters only) ---
TOKEN_RE = re.compile(r"[A-Za-z]+")

def tokenize(text: str):
    """Convert text into lowercase tokens containing only A-Z letters."""
    return TOKEN_RE.findall(text.lower())

def main():
    print(f"Looking for text files in: {DOCS_DIR.resolve()}")
    if not DOCS_DIR.exists():
        raise SystemExit(f"❌ Folder not found: {DOCS_DIR.resolve()}")

    counter = Counter()
    files = sorted([p for p in DOCS_DIR.iterdir() if p.is_file()])
    if not files:
        raise SystemExit(f"❌ No text files found inside {DOCS_DIR.resolve()}")

    # --- Process all documents ---
    for p in files:
        print(f"Processing: {p.name}")
        text = p.read_text(encoding="utf-8", errors="ignore")
        tokens = tokenize(text)
        counter.update(tokens)

    # --- Get top 50 most frequent words ---
    top50 = counter.most_common(50)

    # --- Write results to file ---
    with OUT_FILE.open("w", encoding="utf-8") as f:
        for i, (w, c) in enumerate(top50, 1):
            f.write(f"{i:2d}. {w}\t{c}\n")

    # --- Print results ---
    print("\n✅ Top 50 most frequent words (stop-list):\n")
    for i, (w, c) in enumerate(top50, 1):
        print(f"{i:2d}. {w:15s} {c}")

    print(f"\nResults saved to: {OUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
