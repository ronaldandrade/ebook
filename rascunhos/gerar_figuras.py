"""Gera as figuras criadas na revisão dos Capítulos 3 e 4.

Uso (a partir da pasta livro/):
    python rascunhos/gerar_figuras.py

Saídas em images/:
    arvore_regressao.png  -> Capítulo 3, árvore de decisão para regressão
    sigmoide.png          -> Capítulo 4, função sigmoide com o e-mail do exemplo
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

IMAGES = Path(__file__).resolve().parent.parent / "images"
virgula = FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))


def arvore_regressao():
    d = pd.DataFrame({
        "tamanho": [50, 70, 80, 100, 120, 60, 90, 110, 85, 95],
        "quartos": [1, 2, 2, 3, 3, 1, 2, 3, 2, 2],
        "preco": [180000, 240000, 280000, 350000, 420000,
                  200000, 300000, 380000, 290000, 320000],
    })
    X_tr, _, y_tr, _ = train_test_split(d[["tamanho", "quartos"]], d["preco"],
                                        test_size=0.2, random_state=42)
    arvore = DecisionTreeRegressor(max_depth=3, random_state=42).fit(X_tr, y_tr)
    fig, ax = plt.subplots(figsize=(17, 7.5))
    anotacoes = plot_tree(arvore, feature_names=["tamanho", "quartos"], impurity=False,
                          filled=True, rounded=True, fontsize=10, precision=1, ax=ax)
    for a in anotacoes:
        a.set_text(a.get_text().replace("samples", "amostras").replace("value", "preço médio"))
    ax.set_title("Árvore de decisão para regressão (max_depth=3)", fontsize=14)
    fig.savefig(IMAGES / "arvore_regressao.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def sigmoide():
    X = np.array([[2, 0], [1, 3], [0, 1], [3, 2]])
    y = [0, 1, 0, 1]
    modelo = LogisticRegression().fit(X, y)
    w, b = modelo.coef_[0], modelo.intercept_[0]
    z_novo = w @ np.array([2, 1]) + b
    p_novo = 1 / (1 + np.exp(-z_novo))

    z = np.linspace(-6, 6, 300)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(z, 1 / (1 + np.exp(-z)), color="black", linewidth=2, label=r"$\sigma(z)$")
    ax.axhline(0.5, color="gray", linestyle="--", linewidth=1)
    ax.axvline(0, color="gray", linestyle="--", linewidth=1)
    ax.axvspan(-6, 0, color="royalblue", alpha=0.08)
    ax.axvspan(0, 6, color="crimson", alpha=0.08)
    ax.text(-5.7, 0.9, "z < 0: classe 0\n(não spam)", fontsize=10, color="royalblue")
    ax.text(3.3, 0.08, "z > 0: classe 1\n(spam)", fontsize=10, color="crimson")
    ax.scatter([z_novo], [p_novo], color="darkorange", zorder=3, s=60,
               label="novo e-mail (2 grátis, 1 urgente)")
    ax.annotate(f"z = {z_novo:.2f}\np = {p_novo:.2f}".replace(".", ","),
                xy=(z_novo, p_novo), xytext=(z_novo + 1.2, p_novo - 0.25),
                arrowprops=dict(arrowstyle="->", color="darkorange"), fontsize=10)
    ax.set_xlabel(r"$z = \mathbf{w}^\top \mathbf{x} + b$")
    ax.set_ylabel("probabilidade da classe 1")
    ax.set_title("Função sigmoide")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-0.02, 1.02)
    ax.xaxis.set_major_formatter(virgula)
    ax.yaxis.set_major_formatter(virgula)
    ax.legend(loc="center right")
    fig.savefig(IMAGES / "sigmoide.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    arvore_regressao()
    sigmoide()
    print("Figuras salvas em", IMAGES)
