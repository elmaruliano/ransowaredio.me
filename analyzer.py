# code/analyzer.py
"""
Analisa logs simulados para contar palavras, detectar possíveis senhas (heurística) e gerar relatório.
"""
from pathlib import Path
import re

log = Path("sandbox_samples/fake_keylog.txt")
if not log.exists():
    raise SystemExit("[ERROR] Gere o fake_keylog primeiro.")

text = log.read_text()
lines = text.splitlines()
word_count = sum(len(re.findall(r"\w+", l)) for l in lines)
long_words = [w for w in re.findall(r"\w+", text) if len(w) >= 8]

print(f"Linhas: {len(lines)}")
print(f"Contagem de palavras: {word_count}")
print(f"Palavras longas (>=8): {set(long_words)[:20]}")
