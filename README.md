# DIO Agent — Especialização em Cibersegurança (AppSec & DevSecOps)

Este projeto evolui o **DIO Agent** para atuar como um **Mentor de Cibersegurança**, capaz de conduzir triagens de risco, analisar vulnerabilidades em código e infraestrutura e revisar alterações antes do deploy em produção — tudo isso por meio de engenharia de contexto e arquivos estruturados em Markdown, sem retreinar modelos.

---

## Especialização Desenvolvida e Motivação

Assistentes de IA genéricos tendem a responder imediatamente com comandos ou trechos de código sem avaliar o contexto do ambiente. Na prática profissional de AppSec e SecOps, agir sem diagnóstico pode agravar incidentes ou gerar correções incompletas.

Para resolver isso, especializei o agente para:
1. **Investigar antes de agir:** Exigir contexto sobre exposição, dados sensíveis e controles existentes antes de propor qualquer comando ou correção.
2. **Padronizar a análise de risco:** Sempre classificar **Impacto**, **Probabilidade** e **Severidade**, conectando as falhas à **Tríade CIA**, **OWASP Top 10** e **MITRE ATT&CK**.
3. **Atuar preventivamente (Melhoria Escolhida):** Incluir uma segunda skill voltada para **DevSecOps (Security Gate)**, permitindo revisar alterações de código antes de chegarem à produção, além de manter um template fixo de saída para comparação entre diferentes vulnerabilidades.

---

## Arquivos Criados e Alterados

| Caminho | Tipo | Descrição |
| :--- | :--- | :--- |
| `skills/vulnerability-analysis/SKILL.md` | Novo | Roteiro operacional da skill de análise de vulnerabilidades, regras defensivas, perguntas de triagem e template fixo de relatório. |
| `skills/vulnerability-analysis/README.md` | Novo | Documentação humana explicando o propósito e exemplos de uso da skill principal. |
| `skills/devsecops-review/SKILL.md` | Novo | *(Melhoria)* Skill de revisão pré-produção (Shift-Left) com veredito de aprovação ou bloqueio de deploy. |
| `skills/devsecops-review/README.md` | Novo | Documentação da skill complementar de DevSecOps. |
| `agent/knowledge/security-basics.md` | Novo | Base conceitual com definições de Ativo, Vulnerabilidade, Ameaça, Risco, Tríade CIA, MITRE ATT&CK e Boas Práticas. |
| `agent/persona.md` | Alterado | Adicionada a postura de Mentor Sênior de Cibersegurança (analítico, didático e focado em triagem). |
| `AGENTS.md` | Alterado | Registradas as novas skills na tabela de roteamento do agente. |
| `lab-tests/app_vulnerable.py` | Novo | Aplicação Flask de laboratório com falha intencional de SQL Injection para validação. |
| `lab-tests/app_secure.py` | Novo | Versão corrigida com consultas parametrizadas e hash de senha para revalidação. |

---

## Como Executar o Agente no Hermes

1. **Clone este repositório e acesse a pasta do projeto:**
   ```bash
   git clone https://github.com/SEU-USUARIO/dio-agent-cybersecurity.git
   cd dio-agent-cybersecurity
   ```
   > **Importante:** Sempre execute o comando do Hermes a partir da raiz do projeto (`dio-agent-cybersecurity/`) para que ele carregue corretamente os arquivos `AGENTS.md`, `agent/` e `skills/`.

2. **Inicie o Hermes no terminal (ex: terminal integrado do VS Code):**
   ```bash
   hermes
   ```

3. **Roteiro de Testes Utilizado:**
   - **Teste 1 (Triagem de Contexto):** *"Tenho um servidor Ubuntu de laboratório exposto na internet. O que devo fazer?"* -> O agente questiona exposição, serviços ativos e controles antes de sugerir comandos.
   - **Teste 2 (Análise AppSec):** *"Analise o arquivo `lab-tests/app_vulnerable.py` como especialista em AppSec, explique o risco, cite o MITRE ATT&CK e oriente a correção."*
   - **Teste 3 (Revalidação):** *"Agora analise `lab-tests/app_secure.py` e confirme se o SQL Injection foi mitigado."*
   - **Teste 4 (Melhoria DevSecOps):** *"Faça uma revisão de Security Gate no `lab-tests/app_vulnerable.py` antes do deploy."*

---

## Evidências de Execução (Prints)

> *Adicione aqui os prints do seu terminal rodando o Hermes após executar os testes acima:*
> - `docs/print-triagem-ubuntu.png` — Agente fazendo perguntas de contexto antes de agir.
> - `docs/print-analise-vulneravel.png` — Diagnóstico padronizado do `app_vulnerable.py` com MITRE ATT&CK e Matriz de Risco.
> - `docs/print-validacao-segura.png` — Confirmação da mitigação no `app_secure.py`.
