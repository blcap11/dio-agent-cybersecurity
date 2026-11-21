# Fundamentos de Segurança da Informação (Base de Conhecimento)

Este documento serve como referência conceitual obrigatória para todas as análises e mentorias conduzidas pelo agente.

---

## 1. Conceitos Fundamentais de Risco

- **Ativo:** Qualquer recurso com valor para a organização ou sistema (banco de dados, servidor, credenciais, código-fonte, disponibilidade de um serviço).
- **Vulnerabilidade:** Fraqueza ou falha no design, implementação, operação ou controle interno de um sistema que pode ser explorada. *(Ex: consulta SQL concatenada sem sanitização).*
- **Ameaça:** Qualquer circunstância, agente ou evento com potencial de explorar uma vulnerabilidade e causar dano a um ativo. *(Ex: um ator malicioso automatizando buscas por formulários vulneráveis na internet).*
- **Risco:** A probabilidade de uma ameaça explorar uma vulnerabilidade multiplicada pelo impacto que isso causaria no negócio ou ambiente.
  $$\text{Risco} = \text{Probabilidade} \times \text{Impacto}$$

---

## 2. Tríade CIA (CID)

Toda análise deve identificar qual pilar da segurança está comprometido:

| Pilar | Significado | Exemplo de Violação |
| :--- | :--- | :--- |
| **Confidencialidade** | Garantia de que a informação seja acessada apenas por pessoas ou sistemas autorizados. | Vazamento de tabela de usuários via SQL Injection. |
| **Integridade** | Garantia de que os dados e sistemas não sejam alterados ou destruídos de forma não autorizada. | Modificação indevida de registros financeiros ou binários do sistema. |
| **Disponibilidade** | Garantia de que sistemas e dados estejam acessíveis quando necessários pelos usuários legítimos. | Ataque de negação de serviço (DoS) ou exclusão de banco de dados (`DROP TABLE`). |

---

## 3. Referenciais Técnicos

- **OWASP Top 10:** Lista padrão de conscientização sobre os riscos mais críticos em aplicações web (ex: *A01 Broken Access Control*, *A03 Injection*, *A05 Security Misconfiguration*).
- **MITRE ATT&CK:** Base de conhecimento global de táticas e técnicas adversárias baseadas em observações do mundo real (ex: *T1190 - Exploit Public-Facing Application*).
- **Defesa em Profundidade (Defense in Depth):** Aplicação de múltiplas camadas independentes de controle (rede, host, aplicação, dados), garantindo que a falha de uma camada não comprometa todo o sistema.

---

## 4. Boas Práticas Essenciais

1. **Princípio do Menor Privilégio:** Usuários, serviços e processos devem possuir apenas as permissões estritamente necessárias para executar suas funções.
2. **Nunca Confie na Entrada do Usuário:** Toda entrada externa (formulários, parâmetros de URL, headers, APIs) deve ser validada e tratada com consultas parametrizadas.
3. **Gestão Segura de Segredos:** Credenciais, chaves de API e tokens nunca devem ser gravados diretamente no código-fonte; utilize variáveis de ambiente ou cofres de segredos.
4. **Segurança por Padrão (Secure by Default):** Desabilite portas, serviços e usuários desnecessários antes de expor qualquer servidor à rede.
