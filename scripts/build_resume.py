"""Generate the portfolio resume. Run with Python + reportlab + pypdfium2."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
import shutil
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/AlysonCarregosa-atualizado.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
styles = {
    'name': ParagraphStyle('name', fontName='Times-Bold', fontSize=20, leading=23, spaceAfter=4, alignment=1, textColor=colors.HexColor('#21475c')),
    'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#444444')),
    'body': ParagraphStyle('body', fontName='Times-Roman', fontSize=9, leading=10.4, spaceAfter=3),
    'role': ParagraphStyle('role', fontName='Times-Bold', fontSize=9.5, leading=11, textColor=colors.HexColor('#21475c'), spaceBefore=4, spaceAfter=3),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.HexColor('#21475c'), spaceBefore=7, spaceAfter=3),
    'bullet': ParagraphStyle('bullet', fontName='Times-Roman', fontSize=9, leading=10.4, leftIndent=9, firstLineIndent=-7, spaceAfter=3),
}
story=[]
def p(text, style='body'):
    text = re.sub(r'<a href="([^"]+)">(.*?)</a>', lambda m: '<a href="'+m.group(1)+'" color="#145a85"><u>'+m.group(2)+'</u></a>', text)
    story.append(Paragraph(text,styles[style]))
def section(text):
    p(text,'section')
    story.append(HRFlowable(width='100%',thickness=.5,color=colors.HexColor('#7894a4'),spaceAfter=3))
def bullet(text): p('&#8226; '+text,'bullet')
p('ALYSON SOUZA CARREGOSA','name')
p('+55 79 998823882 | <a href="mailto:alysonsouza36@gmail.com">alysonsouza36@gmail.com</a>','meta')
p('<a href="https://alysonsz.github.io/alyson.dev/">Portfólio: alysonsz.github.io/alyson.dev</a> | <a href="https://github.com/alysonsz">GitHub: alysonsz</a> | <a href="https://www.linkedin.com/in/alyson-carregosa/">LinkedIn: alyson-carregosa</a>','meta')
section('RESUMO PROFISSIONAL')
p('Desenvolvedor com experiência em backend .NET, aplicações full-stack e integrações. Atuação com APIs REST, arquitetura, mensageria, bancos relacionais e cloud. Fundador do Nucleus, plataforma de finanças pessoais com Open Finance e IA, com aplicativo mobile, aplicação web e backend compartilhado.')
section('EXPERIÊNCIA PROFISSIONAL')
p('Desenvolvedor Full-Stack | Support Informática | 01/2025 - Atual','role')
bullet('Reduzi consumo de recursos e latência sob alta carga no sistema de comandas ao migrar o backend de Node.js para .NET 9, com Clean Architecture e implantação em Docker e Kubernetes no GCP.')
bullet('Reduzi o acoplamento entre camadas das APIs ao separar casos de uso com CQRS e MediatR, utilizando Entity Framework Core e SQL Server para persistência e manutenção das regras de negócio.')
bullet('Automatizei a atualização de produtos e pedidos entre o portal de vendas e o Mercado Livre com OAuth 2.0 e sincronização bidirecional, reduzindo etapas manuais da operação.')
bullet('Contribuí para o portal B2B/B2C com React, Next.js e Tailwind CSS e para o painel administrativo com React e Material UI, integrados às APIs .NET.')
bullet('Melhorei a rastreabilidade de falhas com logs estruturados em Serilog e desacoplei fluxos de integração com Kafka, RabbitMQ e tarefas em segundo plano no Hangfire.')
p('Desenvolvedor Backend | Escariz | 06/2024 - 12/2024','role')
bullet('Reduzi a dependência de atualizações manuais ao centralizar catálogo, estoque e pedidos de Amazon, Mercado Livre e Shopee com APIs orientadas a eventos, RabbitMQ e Kafka; automatizei metadados e precificação com Book Info e Keepa.')
bullet('Reduzi de 10 para 1 minuto o intervalo de varredura de um catálogo com mais de 20.000 produtos ao substituir verificações integrais por identificação de novos itens, evitando reprocessamento desnecessário e agilizando a publicação em lote nos e-commerces.')
section('PROJETO AUTORAL')
p('<a href="https://nucleusbrasil.com.br">Nucleus</a> | Finanças pessoais com IA | Fundador e Desenvolvedor Full-Stack','role')
bullet('Unifiquei dados de conexões bancárias e extratos em um modelo financeiro compartilhado ao construir o aplicativo React Native/Expo, a API .NET e a landing page Next.js, com normalização, categorização e sincronização de transações.')
bullet('<b><a href="https://app.nucleusbrasil.com.br/">Nucleus Web</a>:</b> estendi o produto ao navegador com Next.js, React e TypeScript, reutilizando regras e dados da API mobile para fluxo de caixa, cartões, patrimônio e agente Terra. Implementei camada Backend for Frontend (BFF), sessões protegidas, Celcoin e Stripe; versão em preparação para homologação.')
bullet('Tornei as orientações de IA rastreáveis aos dados financeiros com contexto estruturado e ações validadas; protegi o acesso com autorização, armazenamento seguro no mobile e rate limiting, integrando assinaturas RevenueCat e Stripe.')
bullet('Reduzi a latência de uma integração com API parceira de aproximadamente 40 segundos para menos de 200 milissegundos com resolução IPv4 no nível de socket, contornando falhas de conectividade IPv6.')
bullet('Protegi retentativas de checkout contra criação duplicada de sessões com chaves de idempotência por usuário e requisição no Stripe; impedi reiniciar a mesma execução de ferramenta de IA com registro persistente e restrição de unicidade no PostgreSQL.')
section('COMPETÊNCIAS TÉCNICAS')
p('<b>Linguagens e backend:</b> C#, TypeScript, JavaScript, SQL, .NET 6/8/9, ASP.NET Core, REST, Clean Architecture, CQRS, MediatR, Entity Framework Core, Dapper.<br/><b>Dados e mensageria:</b> SQL Server, PostgreSQL, Redis, RabbitMQ, Kafka.<br/><b>Web e mobile:</b> React, Next.js, React Native, Expo, Tailwind CSS, Material UI, Radix UI.<br/><b>Cloud e qualidade:</b> Docker, Kubernetes, GCP, GitHub Actions, SonarQube, xUnit, FluentValidation, Polly, Hangfire, Serilog, OpenTelemetry.<br/><b>Integrações e IA:</b> JWT, OAuth 2.0, Open Finance, Celcoin, Stripe, RevenueCat, marketplaces, LLMs, engenharia de prompts e agentes de IA.')
section('FORMAÇÃO ACADÊMICA')
p('<b>Bacharelado em Ciência da Computação - Estácio</b> | 01/2025 - 12/2027 | Média: 9,39<br/><b>Tecnólogo em Análise e Desenvolvimento de Sistemas - UNINASSAU</b> | 01/2024 - 12/2025 | Média: 9,38')
section('ATIVIDADES EXTRACURRICULARES')
p('<b>Organizador | <a href="https://gdg.community.dev/gdg-aracaju/">Google Developer Groups (GDG) Aracaju</a> | 09/2024 - Atual</b><br/>Organizo eventos técnicos e workshops e articulo palestrantes e parceiros: Jetsales, Universidade Federal de Sergipe (UFS), Rocketseat, UNINASSAU, Quero Delivery, FWK, Acelera-SE Aventures, Get Info, Caju Hub e Jovem Tech.')
section('IDIOMAS')
p('<b>Idiomas:</b> Português nativo · Inglês intermediário-avançado · Espanhol intermediário')
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=34,leftMargin=34,topMargin=26,bottomMargin=25,title='Alyson Souza Carregosa | Desenvolvedor Full-Stack',author='Alyson Souza Carregosa')
doc.build(story)
shutil.copy2(OUT,ROOT/'assets/curriculo-alyson-carregosa.pdf')
print(OUT)

