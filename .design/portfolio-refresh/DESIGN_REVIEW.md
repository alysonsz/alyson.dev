# Design review — Portfolio

Revisado contra DESIGN_BRIEF.md em 14/10/2026. Direção: editorial técnico.

## Screenshots Captured

- screenshots/hero-desktop-1280.png — abertura desktop
- screenshots/hero-tablet-768.png — abertura tablet
- screenshots/hero-mobile-375.png — abertura mobile
- screenshots/review-homepage-desktop-1280.png — página completa desktop
- screenshots/review-homepage-tablet-768.png — página completa tablet
- screenshots/review-homepage-mobile-375.png — página completa mobile
- screenshots/work-desktop-1280.png — case desktop
- screenshots/work-tablet-768.png — case tablet
- screenshots/work-mobile-375.png — case mobile
- screenshots/reduced-motion-mobile.png — movimento reduzido

## Resultado

Identidade escura e verde ácido preservada. Hero ganha hierarquia mais clara e composição de engenharia; manifesto reforça a relação backend/produto. Cards e tipografia têm acabamento consistente. Layout se reorganiza em coluna única em tablet/mobile. Capturas completas finais usam movimento reduzido para registrar todo o conteúdo em estado legível.

## Correções realizadas

A incorporação externa do Nucleus apareceu vazia durante a revisão. Foi substituída por captura local existente, com rolagem interna e link para o produto real. Preview desktop acompanha a leitura do case com posicionamento sticky. Links ganham foco visível, alvos do cabeçalho têm 44px e animações respeitam prefers-reduced-motion.

## Validação

JavaScript passou node --check. git diff --check passou. Navegação renderizada nas três larguras sem overflow horizontal nem exceções JavaScript. Terminal fica imediatamente legível com movimento reduzido. Capturas de hero, tablet e vitrine inspecionadas visualmente.

## Limites

A prévia local representa a captura fornecida no repositório; alterações futuras no Nucleus exigem atualizar essa imagem. Fontes remotas dependem de acesso ao Google Fonts, com fallbacks locais definidos.
