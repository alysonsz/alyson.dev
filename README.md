# Portfólio — Alyson Souza Carregosa

Portfólio estático, responsivo e pronto para GitHub Pages.

## Publicação

1. Crie um repositório chamado `alysonsz.github.io` no GitHub.
2. Envie estes arquivos para a branch `main`.
3. Em **Settings → Pages**, escolha **GitHub Actions** como fonte.

O workflow em `.github/workflows/pages.yml` publica o site automaticamente a cada push.

## Desenvolvimento local

Como o projeto não possui dependências, basta servir a pasta com qualquer servidor HTTP:

```bash
python -m http.server 4173
```

Depois, abra `http://localhost:4173`.
