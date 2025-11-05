# Instruções de Laboratório (Passo-a-passo)


**Pré-requisitos**
- Máquina virtual (VirtualBox/VMware) com snapshot disponível
- Sistema operacional convidado (ex.: Debian minimal ou Windows isolado)
- Acesso à internet desabilitado ou rede isolada


## 1. Preparação da VM
1. Crie uma VM nova.
2. Instale Python 3.9+.
3. Instale o pacote `cryptography`: `pip install cryptography`.
4. Crie snapshot base: "clean-state".


## 2. Preparar sandbox
1. Crie um diretório sandbox: `/tmp/malware_lab_sandbox` (Linux) ou `C:\malware_lab_sandbox` (Windows).
2. Dentro do sandbox, crie 3 arquivos de teste com conteúdo simples e extensão `.sample`, por exemplo:
- `file1.sample` (texto)
- `notes.sample` (texto)
- `image.sample` (pode ser um arquivo binário pequeno renomeado)


## 3. Gerar chave e encriptar (demonstração segura)
1. `python3 code/encrypter_demo.py --sandbox /tmp/malware_lab_sandbox --mode genkey --keyfile /tmp/malware_lab_sandbox/key.key`
2. `python3 code/encrypter_demo.py --sandbox /tmp/malware_lab_sandbox --mode encrypt --keyfile /tmp/malware_lab_sandbox/key.key`
3. Observe que o script cria arquivos `.sample.enc` e NÃO apaga os originais.
4. Tire screenshots antes/depois (salve em `/images`).


## 4. Descriptografar (verificação)
1. `python3 code/encrypter_demo.py --sandbox /tmp/malware_lab_sandbox --mode decrypt --keyfile /tmp/malware_lab_sandbox/key.key --target /tmp/malware_lab_sandbox/file1.sample.enc`
2. Verifique o arquivo `.decrypted.sample` criado.


## 5. Gerar logs simulados e analisar
1. `python3 code/fake_keylog_generator.py`
2. `python3 code/analyzer.py`
3. Salve a saída do analisador em `/images` como evidência.


## 6. Reverter VM
1. Após os testes, reverta o snapshot "clean-state".


## Notas
- Não conectar a VM à rede externa sem necessidade.
- Documente cada passo para o relatório final.
