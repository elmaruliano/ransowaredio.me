# ransowaredio.me
Simulando um Malware de Captura de Dados Simples em Python e Aprendendo a se Proteger
# Simulação Educativa: Ransomware & Keylogger (Ambiente Controlado)

**Aviso de segurança**  
Este projeto contém *simulações educacionais* de técnicas associadas a malwares. **Não** execute os scripts em máquinas de produção ou com dados reais. Execute **somente** em uma VM isolada com snapshot e em um diretório sandbox criado para testes.

# Simulação Educativa: Ransomware & Keylogger (Ambiente Controlado)


**Aviso de segurança**
Este projeto contém *simulações educacionais* de técnicas associadas a malwares. **Não** execute os scripts em máquinas de produção ou com dados reais. Execute **somente** em uma VM isolada com snapshot e em um diretório sandbox criado para testes.


## Estrutura do repositório
- `/code` — scripts educativos e seguros (ex.: encrypter_demo.py, fake_keylog_generator.py, analyzer.py)
- `/sandbox_samples` — arquivos de teste `.sample` (ex.: file1.sample)
- `/images` — capturas de tela do experimento
- `README.md` — este arquivo
- `lab_instructions.md` — instruções detalhadas para reproduzir o laboratório
- `analysis.md` — análise e reflexão sobre defesa
- `WARNING.md` — instrução de segurança curta


## Objetivos
1. Demonstrar, de forma controlada, o comportamento conceitual de um ransomware (criptografia reversível de arquivos de teste).
2. Demonstrar, de forma controlada, como dados de digitação poderiam ser gerados e analisados sem capturar teclas reais do sistema.
3. Documentar estratégias de defesa e detecção.


## Requisitos
- Python 3.9+
- Biblioteca: `cryptography` (`pip install cryptography`)


## Como executar (resumo)
1. Crie VM isolada e um diretório sandbox (ex.: `/tmp/malware_lab_sandbox` ou `C:\malware_lab_sandbox`).
2. Copie os arquivos `.sample` para o sandbox.
3. Rode `python3 code/encrypter_demo.py --sandbox /caminho/para/sandbox --mode genkey --keyfile /caminho/para/sandbox/key.key`
4. Rode `python3 code/encrypter_demo.py --sandbox /caminho/para/sandbox --mode encrypt --keyfile /caminho/para/sandbox/key.key`
5. Para descriptografar: `python3 code/encrypter_demo.py --sandbox /caminho/para/sandbox --mode decrypt --keyfile /caminho/para/sandbox/key.key --target /caminho/para/arquivo.sample.enc`
6. Rode `python3 code/fake_keylog_generator.py` para gerar logs simulados.
7. Rode `python3 code/analyzer.py` para analisar os logs gerados.


## Estrutura sugerida de commit
- `git init`
- `git add .`
- `git commit -m "Initial commit: educational malware simulation (safe)"


## Ética e uso
Este repositório é apenas para fins educacionais e de defesa. Qualquer uso malicioso é proibido.

