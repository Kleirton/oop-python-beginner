# Estudos de POO em Python 🐍

Este repositório é focado nos meus estudos de Programação Orientada a Objetos (POO) na linguagem Python.

## 📚 Sobre o Projeto
Os códigos e exercícios práticos armazenados aqui são baseados no livro **"Object-Oriented Python: Master OOP by Building Games and GUIs"**, escrito por Irv Kalb. O objetivo principal é consolidar os conceitos de orientação a objetos através da construção prática de interfaces gráficas e jogos.

## 🚀 O que será abordado
- Fundamentos de POO (Classes, Objetos, Encapsulamento, Herança e Polimorfismo)
- Criação de Interfaces Gráficas (GUIs)
- Desenvolvimento estruturado de jogos simples

## 🛠️ Tecnologias
- Python 3

## ⚙️ Instalação e Configuração

O Pygame é um pacote gratuito do Python. Iremos utilizar o gerenciador de pacotes `pip` para realizar a instalação.

Para evitar conflitos com os pacotes do sistema operacional, é altamente recomendável criar e utilizar um ambiente virtual (`venv`). Siga os passos abaixo:

**1. Clone o repositório e entre na pasta do projeto:**
```bash
git clone https://github.com/Kleirton/oop-python-beginner
cd oop-python-beginner
```

**2. Crie o ambiente virtual:**
```bash
python -m venv .venv
```
*(Nota: Se você estiver usando um disco externo formatado em NTFS/exFAT no Linux, use `python -m venv --copies .venv` para evitar problemas com links simbólicos).*

**3. Ative o ambiente virtual:**
- **Bash / Zsh:**
  ```bash
  source .venv/bin/activate
  ```
- **Fish:**
  ```fish
  source .venv/bin/activate.fish
  ```
- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

**4. Instale o Pygame:**
```bash
pip install pygame
```
*(Nota para usuários Arch Linux / CachyOS: O Pygame precisa das bibliotecas do SDL2 para compilar corretamente. Antes de usar o `pip`, certifique-se de instalar as dependências com `sudo pacman -S base-devel sdl2 sdl2_image sdl2_ttf sdl2_mixer portmidi`).*

**5. Verifique a instalação:**
Teste se o pacote foi instalado corretamente e execute o jogo de exemplo "Aliens" que vem embutido:
```bash
python -c "import pygame; print('Pygame instalado com sucesso!')"
python -m pygame.examples.aliens
```

Após concluir esses passos, o ambiente estará pronto para que você possa acompanhar os estudos e executar os jogos construídos ao longo do repositório!

---
*Estudos realizados por Kleirton de Abreu Silva Filho*