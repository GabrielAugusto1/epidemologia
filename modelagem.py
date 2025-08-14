import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
N = 20  # Tamanho da grade
steps = 50  # Número de passos
p_infect = 0.3  # Probabilidade de infecção
t_recover = 5  # Tempo para recuperação

# Estados: 0 = S, 1 = I, 2 = R
grid = np.zeros((N, N), dtype=int)
infection_time = np.zeros((N, N), dtype=int)

# Inicializa um infectado no centro
grid[N//2, N//2] = 1

susceptible_hist = []
infected_hist = []
recovered_hist = []

def get_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                neighbors.append((nx, ny))
    return neighbors

for step in range(steps):
    new_grid = grid.copy()
    for x in range(N):
        for y in range(N):
            if grid[x, y] == 1:  # Infectado
                for nx, ny in get_neighbors(x, y):
                    if grid[nx, ny] == 0 and np.random.rand() < p_infect:
                        new_grid[nx, ny] = 1
                infection_time[x, y] += 1
                if infection_time[x, y] >= t_recover:
                    new_grid[x, y] = 2  # Recupera
    grid = new_grid
    susceptible_hist.append(np.sum(grid == 0))
    infected_hist.append(np.sum(grid == 1))
    recovered_hist.append(np.sum(grid == 2))

# Gráfico dos resultados
plt.plot(susceptible_hist, label='Susceptíveis')
plt.plot(infected_hist, label='Infectados')
plt.plot(recovered_hist, label='Recuperados')
plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.legend()
plt.title('Simulação SIR com Autômatos Celulares')
plt.show()