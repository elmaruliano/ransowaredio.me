# code/fake_keylog_generator.py
"""
Gera dados simulados de 'keystrokes' para fins de análise.
Não captura teclas do sistema.
"""
import random
from datetime import datetime, timedelta
from pathlib import Path

chars = "abcdefghijklmnopqrstuvwxyz0123456789 .,@!#\n"
out = Path("sandbox_samples/fake_keylog.txt")
out.parent.mkdir(parents=True, exist_ok=True)

now = datetime.now()
lines = []
for session in range(5):
    t = now + timedelta(minutes=session*5)
    length = random.randint(20, 200)
    entry = ''.join(random.choice(chars) for _ in range(length))
    lines.append(f"{t.isoformat()} {entry}")

out.write_text("\n".join(lines))
print(f"[OK] Fake keylog gerado em {out}")
