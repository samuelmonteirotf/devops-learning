# DevOps Learning Project

Este projeto foi criado como prática para a disciplina de DevOps. O objetivo é demonstrar a configuração de um fluxo básico de integração contínua (CI).

## Estrutura do Projeto

- `app.py`: Contém funções matemáticas básicas (soma, subtração, multiplicação).
- `tests/test_app.py`: Contém testes unitários utilizando o `pytest`.
- `requirements.txt`: Dependências do projeto.
- `.github/workflows/ci.yml`: Pipeline de CI/CD para execução automática dos testes no GitHub Actions.

## Fluxo de Trabalho (Git Flow)

Para este projeto, utilizamos as seguintes práticas:
1. **Branches**: Desenvolvimento de novas funcionalidades em branches isoladas (ex: `feature/add-tests-and-ci`).
2. **Commits**: Histórico de commits claro, seguindo convenções (ex: `feat:`, `test:`, `docs:`, `ci:`).
3. **Pull Requests (PR)**: Integração do código via PR para a branch `main`, garantindo revisão e execução prévia da pipeline de CI.
4. **CI/CD com GitHub Actions**: Os testes definidos com `pytest` rodam automaticamente a cada push ou PR.

## Pipelines de CI/CD

Este projeto utiliza um fluxo (workflow) contínuo no GitHub Actions (`build-and-deploy.yml`) dividido em dois *jobs*:
- **Build (CI)**: Responsável por validar o código rodando testes automatizados com `pytest`.
- **Deploy (CD)**: Executado logo após o *Build* ser bem-sucedido, é responsável por empacotar a aplicação e publicá-la como um artefato `.zip` (`devops-learning-artifact`).
