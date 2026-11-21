# DIO Agent — Roteamento e Instruções

Este arquivo define as diretrizes operacionais e o roteamento de habilidades (*skills*) do agente.

## Regras Gerais
- Sempre consulte os arquivos de conhecimento em `agent/knowledge/` e siga a postura definida em `agent/persona.md`.
- Ao identificar uma demanda compatível com uma das skills abaixo, leia o respectivo `SKILL.md` e siga rigorosamente o fluxo e formato definidos nele.

## Tabela de Skills

| Skill | Quando Usar | Caminho |
| :--- | :--- | :--- |
| `vulnerability-analysis` | Sempre que o usuário pedir análise de vulnerabilidades em código, servidores, configurações ou cenários de risco em cibersegurança. | `skills/vulnerability-analysis/SKILL.md` |
| `devsecops-review` | Sempre que o usuário pedir revisão preventiva de código, PR ou configuração antes de subir para produção (Security Gate). | `skills/devsecops-review/SKILL.md` |
