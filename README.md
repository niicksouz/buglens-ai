# BugLens AI

API experimental que classifica relatos de bugs e usa a API do Gemini para gerar uma análise inicial em português.

## O que faz

- Recebe a descrição de um bug pelo endpoint `POST /analyze`.
- Sugere uma categoria usando um modelo de texto treinado com scikit-learn.
- Usa o Gemini para gerar um resumo, uma hipótese e passos para investigar.
- Oferece documentação interativa pela interface Swagger do FastAPI.

## Tecnologias

Python, FastAPI, scikit-learn, Google GenAI SDK e Swagger UI.

## Como executar localmente

1. Clone este repositório e acesse a pasta do projeto.
2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências: 

    ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo .env na pasta principal e adicione sua chave:

   ```
   GEMINI_API_KEY=sua_chave_aqui
   ```

Não compartilhe nem publique esse arquivo.

5. Treine o classificador:

    ```bash
    python train_model.py
    ```

6. Inicie a API:

    ```bash
    uvicorn main:app --reload
    ```

7. Acesse a documentação interativa em http://127.0.0.1:8000/docs.


## Exemplo de requisição

```json
{
"description": "Ao clicar em entrar, a página fica carregando e não abre."
}
```

## Limitações

    Este é um protótipo em desenvolvimento. O classificador usa uma base pequena de exemplos e ainda não foi validado com usuários ou em produção. A categoria e a análise geradas podem estar incorretas e devem ser revisadas por uma pessoa.

## Segurança

    Mantenha sua chave do Gemini no .env. Não publique credenciais ou dados privados.
