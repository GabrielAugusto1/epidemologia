# Simulação da Propagação da Dengue com Autômatos Celulares (Modelo SIR)

Este projeto apresenta uma simulação simples da propagação da dengue em uma população, utilizando autômatos celulares e o modelo compartimental SIR (Susceptível-Infectado-Recuperado).

## Objetivo

Demonstrar, de forma visual e computacional, como doenças infecciosas como a dengue podem se espalhar em uma população, e como o modelo SIR pode ser aplicado para estudar essa dinâmica.

## Descrição

- Cada célula da grade representa um indivíduo, que pode estar em um dos três estados: Suscetível (S), Infectado (I) ou Recuperado (R).
- A propagação ocorre localmente: infectados podem transmitir a doença para vizinhos suscetíveis.
- Após um tempo de infecção, o indivíduo se recupera e não pode mais ser infectado.
- O código gera gráficos mostrando a evolução dos grupos ao longo do tempo.

## Como executar

1. Clone este repositório:
   ```
   git clone https://github.com/GabrielAugusto1/epidemologia.git
   ```
2. Instale as dependências:
   ```
   pip install numpy matplotlib
   ```
3. Execute o script principal:
   ```
   python modelagem.py
   ```

## Artigo

O artigo científico explicando o modelo, metodologia e resultados está disponível neste repositório:  
[Artigo.pdf](https://github.com/GabrielAugusto1/epidemologia/ArtigoGabriel.pdf)


## Referências

- Kermack, W.O., McKendrick, A.G. (1927). A Contribution to the Mathematical Theory of Epidemics.
- Keeling, M.J., Rohani, P. (2008). Modeling Infectious Diseases in Humans and Animals.