# StoryTeller AI

StoryTeller AI é um projeto em Python que gera histórias curtas e criativas usando a API da OpenAI e, em seguida, converte essas histórias em áudio. Basta informar um personagem principal e um cenário, e o programa cria automaticamente uma narrativa divertida que você pode ouvir em formato MP3.  

## Funcionalidades

- Geração de histórias curtas e imaginativas a partir de um personagem e cenário fornecidos pelo usuário.
- Conversão da história em áudio usando Text-to-Speech (TTS) da OpenAI.
- Salvamento do áudio gerado em arquivo MP3 com o nome do personagem.

## Tecnologias

- Python 3.10+
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- `pathlib` para manipulação de arquivos

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/storyteller-ai.git
cd storyteller-ai

## Dependências
pip install openai

## Crie um arquivo .env:
OPENAI_API_KEY = "sua chave aqui"

## Rode o script
python main.py

