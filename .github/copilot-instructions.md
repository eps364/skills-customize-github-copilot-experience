# GitHub Copilot Instructions

## Commit Message Guidelines

Sempre gere mensagens em ingles de commit seguindo a especificação Conventional Commits:


### Format
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

### Tipos de Commit

- **feat**: Uma nova funcionalidade
- **fix**: Correção de bug
- **docs**: Mudanças na documentação
- **style**: Mudanças que não afetam o significado do código (espaços em branco, formatação, etc.)
- **refactor**: Mudança de código que não corrige um bug nem adiciona uma funcionalidade
- **test**: Adicionando testes ausentes ou corrigindo testes existentes
- **chore**: Mudanças no processo de build ou ferramentas auxiliares

### Exemplos
- feat(assignments): add new assignment on data structures
- fix(template): correct typo in assignment template
- docs(readme): update project description
- style(css): format CSS files for consistency
- refactor(index): improve code structure for assignment listing
- test(assignment): add tests for assignment download feature
- chore(build): update build scripts for deployment


# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes