import numpy as np
import matplotlib.pyplot as plt

# 1. Definição dos valores físicos dos componentes
R = 100.0      # Resistência: 100 Ohms
L = 10e-3      # Indutância: 10 mH (10 * 10^-3 H)
C = 1e-6       # Capacitância: 1 uF (1 * 10^-6 F)

# Constantes auxiliares calculadas a partir das equações
LC = L * C     # Resultará em 10^-8
RC = R * C     # Resultará em 10^-4

# 2. Definição do vetor de frequência w (rad/s) em escala logarítmica
# A ressonância esperada é em 10^4 rad/s. 
# Varremos de 10^2 (100) até 10^6 (1.000.000) com 1000 pontos.
w = np.logspace(2, 6, 1000)

# 3. Modelagem explícita da Função de Transferência H(jw)
# Numerador = 1
# Denominador = (1 - LC*w^2) + j(w*RC)
H = 1 / ((1 - LC * w**2) + 1j * (w * RC))
    
# 4. Cálculo da Magnitude e Fase
# Magnitude em decibéis: 20 * log10(|H|)
mag_dB = 20 * np.log10(np.abs(H))

# Fase em graus: arctg(Parte Imaginária / Parte Real)
# np.unwrap mantém a continuidade da curva sem saltos matemáticos
phase_deg = np.rad2deg(np.unwrap(np.angle(H)))

# 5. Configuração da Plotagem (Diagrama de Bode)
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plotagem da Magnitude
ax_mag.semilogx(w, mag_dB, color='blue', linewidth=2)
ax_mag.set_title('Diagrama de Bode - Filtro RLC Série ($R=100\Omega, L=10mH, C=1\mu F$)', fontsize=14)
ax_mag.set_ylabel('Magnitude (dB)', fontsize=12)
ax_mag.grid(True, which="both", ls="--", alpha=0.6)

# Marcação do ponto de ressonância (w = 10^4)
ax_mag.axvline(x=10000, color='red', linestyle=':', label='Ressonância ($\omega = 10^4$ rad/s)')
ax_mag.legend(loc='lower left')

# Plotagem da Fase
ax_phase.semilogx(w, phase_deg, color='green', linewidth=2)
ax_phase.set_ylabel('Fase (graus)', fontsize=12)
ax_phase.set_xlabel('Frequência $\omega$ (rad/s)', fontsize=12)

# Eixo Y travado nos ângulos notáveis
ax_phase.set_yticks([0, -45, -90, -135, -180])
ax_phase.grid(True, which="both", ls="--", alpha=0.6)

# Marcação do ponto de ressonância na fase
ax_phase.axvline(x=10000, color='red', linestyle=':')

# Ajuste e exibição
plt.tight_layout()
plt.show()