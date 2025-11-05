# code/encrypter_demo.py
"""
Uso educativo: criptografa/descriptografa arquivos .sample dentro de um diretório sandbox.
REGRAS DE SEGURANÇA: apenas caminhos absolutos; exige confirmação; não apaga originais.
"""

import argparse
import os
from pathlib import Path
from cryptography.fernet import Fernet

def require_sandbox(path: Path):
    # exige que sandbox esteja em /tmp ou C:\sandbox_examples para segurança mínima
    allowed_roots = [Path("/tmp"), Path("C:/malware_lab_sandbox"), Path.home() / "malware_lab_sandbox"]
    if not any(str(path).startswith(str(root)) for root in allowed_roots):
        raise SystemExit(f"[ERROR] Por segurança, escolha um sandbox dentro de {allowed_roots}")

def generate_key(keyfile: Path):
    key = Fernet.generate_key()
    keyfile.write_bytes(key)
    print(f"[INFO] Chave salva em {keyfile}")
    return key

def load_key(keyfile: Path):
    return keyfile.read_bytes()

def encrypt_files(sandbox: Path, key: bytes):
    f = Fernet(key)
    for p in sandbox.rglob("*.sample"):
        data = p.read_bytes()
        token = f.encrypt(data)
        out = p.with_suffix(p.suffix + ".enc")
        out.write_bytes(token)
        print(f"[OK] {p} -> {out}")

def decrypt_file(enc_path: Path, key: bytes):
    f = Fernet(key)
    token = enc_path.read_bytes()
    plain = f.decrypt(token)
    orig = enc_path.with_suffix("")  # remove .enc
    # write as .decrypted.sample to avoid overwriting
    out = enc_path.with_suffix(".decrypted" + enc_path.suffix.replace(".enc", ""))
    out.write_bytes(plain)
    print(f"[OK] {enc_path} -> {out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypter demo (seguro)")
    parser.add_argument("--sandbox", required=True, help="Diretório sandbox absoluto")
    parser.add_argument("--keyfile", default="sandbox_key.key")
    parser.add_argument("--mode", choices=["genkey","encrypt","decrypt"], default="encrypt")
    parser.add_argument("--target", help="Arquivo .enc para descriptografar (use com --mode decrypt)")
    args = parser.parse_args()

    sandbox = Path(args.sandbox).resolve()
    require_sandbox(sandbox)
    keyfile = Path(args.keyfile).resolve()

    if args.mode == "genkey":
        generate_key(keyfile)
    elif args.mode == "encrypt":
        if not keyfile.exists():
            raise SystemExit("[ERROR] Gere a chave primeiro: --mode genkey")
        key = load_key(keyfile)
        encrypt_files(sandbox, key)
    elif args.mode == "decrypt":
        if not args.target:
            raise SystemExit("[ERROR] Especifique --target caminho/para/arquivo.sample.enc")
        if not keyfile.exists():
            raise SystemExit("[ERROR] Chave não encontrada.")
        key = load_key(keyfile)
        decrypt_file(Path(args.target), key)
