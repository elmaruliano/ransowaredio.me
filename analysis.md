# Como detectar (IOCs/behavioral):
## Monitorar criação de arquivos com novas extensões (.enc, .crypted), alteração massiva de timestamps.
## Elevação de uso de CPU/disk por processos em background; criação de processos filhos invocando ferramentas de criptografia.
## Egress traffic (exfiltration) — conexões DNS/HTTP/S para destinos anômalos.
## Regras YARA para strings usadas em executáveis (apenas como exemplo).

#Ferramentas de análise:
## strings, hexdump, volatility (para memória), Sysinternals (Windows), Wireshark (rede), EDR logs.

# Controles preventivos:
## Backups offline/immutáveis; EDR com rollback; least privilege; segmentação da rede; atualizações; aplicação de políticas de execução; MFA; training de usuário.

# Resposta a incidente (resumo):
## Isolar host, preservar evidências, identificar e bloquear C2, restaurar de backup, comunicar stakeholders.
