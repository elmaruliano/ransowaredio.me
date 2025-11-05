# Análise e Reflexão sobre Defesa


## Resumo do exercício
Este laboratório apresentou simulações controladas de duas técnicas associadas a malwares: encriptação de arquivos (ransomware) e captura de entradas (keylogging). As simulações foram projetadas para operar **apenas** em arquivos de teste dentro de um sandbox e não capturam dados reais do sistema.


## Observações técnicas
- **Ransomware (simulado)**: utiliza criptografia simétrica (Fernet). Comportamentos observáveis incluem criação de novos arquivos com extensão `.enc`, alteração de timestamps e possível pico de I/O durante a operação.
- **Keylogger (simulado)**: em vez de capturar entradas físicas, o laboratório gera logs sintéticos que reproduzem o formato e o conteúdo esperado de um keylogger, permitindo testar heurísticas e filtros sem comprometer a privacidade.


## Indicadores de Comprometimento (IOCs)
- Arquivos com extensões incomuns (`.enc`, `.locked`) criados em massa.
- Aumento súbito de operações de escrita no disco por processos não usuais.
- Processos com comportamento de cifragem (leitura recursiva + escrita de novos arquivos).
- Tráfego de saída anômalo para serviços de C2 ou servidores de pagamento.


## Estratégias de Detecção
- Endpoint Detection and Response (EDR) com rules de comportamento (mass file writes, file rename patterns).
- Monitoramento de integridade (tripwire) para detectar alteração em dados críticos.
- Regras IDS/IPS para detectar padrões de exfil (DNS tunneling, HTTP POST para destinos não autorizados).


## Controles Preventivos
1. Backup off-line e verificável; rotação e testes de restore.
2. Política de least privilege e segmentação de rede.
3. Whitelisting de aplicações e controle de execução.
4. Treinamento de usuários e simulações de phishing.
5. Patching e gestão de vulnerabilidades.


## Resposta a Incidentes (fluxo resumido)
1. Isolar o host afetado.
2. Preservar evidências (imagens, logs).
3. Identificar alcance (quais sistemas e dados foram cifrados/exfiltrados).
4. Remoção do vetor (bloquear contas, rotas, atualizar regras de firewall).
5. Restaurar a partir de backups validados.


## Conclusão
Simulações seguras permitem testar e validar controles sem riscos legais ou de privacidade. A combinação de prevenção (backups, whitelisting), detecção (EDR, IDS) e resposta (procedimentos, comunicação) é essencial para minimizar impacto de ataques reais.
