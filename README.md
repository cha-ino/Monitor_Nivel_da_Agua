# 🌊 Monitor de Nível de Água (Water Level Monitor)

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um script interativo em Python desenvolvido para monitorar, validar e classificar o nível de água de um reservatório. O programa utiliza a biblioteca `colorama` para fornecer um feedback visual colorido e intuitivo diretamente no terminal, facilitando a identificação de estados críticos ou de alerta.

## 🚀 Funcionalidades

- **Validação Robusta de Dados:** O programa aceita apenas números inteiros entre 0 e 100. Caso o utilizador digite letras ou valores fora da faixa, o sistema trata o erro (`ValueError`) e solicita a entrada novamente sem crashar.
- **Feedback Visual Inteligente:** Cada faixa de nível possui uma cor específica associada, permitindo uma leitura rápida do estado do reservatório.
- **Reset de Estilo Automático:** Utiliza o `autoreset=True` da biblioteca Colorama para garantir que as cores do terminal voltem ao normal após a exibição do status.

## 📊 Classificação de Níveis e Cores

O sistema categoriza a quantidade de água de acordo com a tabela abaixo:

| Intervalo (%) | Status | Cor no Terminal | Significado Visual |
| :---: | :--- | :---: | :---: |
| **0 – 20** | Muito Baixo (crítico) | 🔴 Vermelho | Perigo / Escassez severa |
| **21 – 40** | Baixo | 🟡 Amarelo | Atenção / Nível reduzido |
| **41 – 60** | Médio | 🟢 Verde | Estado Normal / Estável |
| **61 – 80** | Alto | 🔵 Ciano | Bom armazenamento |
| **81 – 100** | Muito Alto (alerta) | 🔵 Azul | Reservatório Cheio / Transbordo |
