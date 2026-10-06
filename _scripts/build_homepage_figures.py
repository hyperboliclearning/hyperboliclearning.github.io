"""Reproduce the homepage figures from the bundled survey and exact formulas.

Requires pdftoppm, Pillow, NumPy, and Matplotlib. Run from any directory.
Survey crops retain the original artwork; the projection diagram is redrawn
from exact unit-curvature cross-sections, with desktop and mobile layouts.
"""

from pathlib import Path
import os
import subprocess
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "hyperbolic-mpl"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "images" / "figs"
SURVEY = ROOT / "survey" / "From-Hyperbolic-to-Mixed-Curvature-Geometric-Learning-A-Comprehensive-Survey.pdf"


def extract_survey_figures():
    with tempfile.TemporaryDirectory(prefix="hyperbolic-figures-") as tmp:
        for page, crop, filename in [
            (8, (245, 125, 1300, 450), "survey-manifold-operations.png"),
            (11, (220, 140, 1300, 590), "survey-model-projections.png"),
        ]:
            target = Path(tmp) / f"page-{page}"
            subprocess.run([
                "pdftoppm", "-f", str(page), "-l", str(page), "-scale-to", "2000",
                "-singlefile", "-png", str(SURVEY), str(target),
            ], check=True)
            with Image.open(target.with_suffix(".png")) as image:
                image.crop(crop).save(FIGURES / filename, optimize=True)


def plot_geometry():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.labelcolor": "#3d424a", "text.color": "#1e2a36",
        "axes.edgecolor": "#cbd5df", "xtick.color": "#586575", "ytick.color": "#586575",
        "svg.fonttype": "none",
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.25), layout="constrained")
    hyperbolic_color, euclidean_color = "#c0392b", "#222222"
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.25, color="#b9c5d2")
        ax.set_axisbelow(True)

    r = np.linspace(0, 5, 400)
    axes[0].plot(r, 2 * np.pi * (np.cosh(r) - 1), color=hyperbolic_color, linewidth=2.5, label="Hyperbolic, curvature = −1")
    axes[0].plot(r, np.pi * r ** 2, color=euclidean_color, linewidth=2.5, label="Euclidean, curvature = 0")
    axes[0].set(xlabel="Geodesic radius r", ylabel="Disk area", xlim=(0, 5), ylim=(0, 490))
    axes[0].set_title("More room for branching structure", loc="left", fontsize=12, weight="bold", pad=12)
    axes[0].legend(frameon=False, loc="upper left", fontsize=9)

    rho = np.linspace(0, 0.999, 700)
    axes[1].plot(rho, 2 * np.arctanh(rho), color=hyperbolic_color, linewidth=2.5, label="Hyperbolic")
    axes[1].plot(rho, rho, color=euclidean_color, linewidth=2.5, label="Euclidean")
    axes[1].axvline(1, color="#94a3b8", linestyle="--", linewidth=1.4)
    axes[1].set(xlabel="Poincaré coordinate norm ρ", ylabel="Distance from the origin", xlim=(0, 1.02), ylim=(0, 8))
    axes[1].set_title("A finite disk represents infinite distance", loc="left", fontsize=12, weight="bold", pad=12)
    axes[1].legend(frameon=False, loc="upper left", fontsize=9)
    axes[1].text(0.06, 5.8, r"$d_H(0,x)=2\,\mathrm{artanh}(\rho)$", fontsize=12)
    axes[1].text(0.06, 4.9, r"$d_E(0,x)=\rho$", fontsize=12)
    axes[1].annotate("Boundary is excluded", xy=(1, 4.5), xytext=(0.28, 5.4),
                     arrowprops={"arrowstyle": "->", "color": "#586575"}, color="#586575", fontsize=10)
    fig.savefig(FIGURES / "hyperbolic-area-and-distance.svg", facecolor="white", metadata={"Date": None})
    fig.savefig(Path(tempfile.gettempdir()) / "hyperbolic-area-and-distance.png", facecolor="white", dpi=160)
    plt.close(fig)


def plot_model_projections():
    """Show exact cross-sections without the occlusion of a 3D perspective."""
    # Match the homepage's Arial prose and its Computer Modern / TeX math style.
    for filename in ("Arial.ttf", "Arial Italic.ttf", "Arial Bold.ttf"):
        font_path = Path("/System/Library/Fonts/Supplemental") / filename
        if font_path.exists():
            font_manager.fontManager.addfont(font_path)
    available = {font.name for font in font_manager.fontManager.ttflist}
    face = "Arial" if "Arial" in available else "DejaVu Sans"
    plt.rcParams.update({
        "font.family": face, "font.size": 13,
        "text.color": "#1e2a36", "svg.fonttype": "path",
        "mathtext.fontset": "cm",
    })
    blue, orange, green = "#3a5a7c", "#c0603c", "#28776b"

    def draw_panel(ax, spherical):
        ax.set(xlim=(-1.9, 1.9), ylim=(-1.35, 2.45), aspect="equal")
        ax.axis("off")
        ax.annotate("", xy=(1.83, 0), xytext=(-1.83, 0),
                    arrowprops={"arrowstyle": "->", "color": "#bbc4ce", "lw": 1.2})
        ax.annotate("", xy=(0, 2.0), xytext=(0, -1.15),
                    arrowprops={"arrowstyle": "->", "color": "#bbc4ce", "lw": 1.2})
        ax.text(1.83, -0.21, r"$X_s$", ha="right", color="#64748b", fontsize=16)
        ax.text(0.08, 1.95, r"$X_0$", color="#64748b", fontsize=16)
        ax.text(-1.8, 2.32, "Sphere → stereographic plane" if spherical else "Lorentz → Poincaré",
                fontsize=14, weight="bold")
        ax.text(-1.8, 2.08, r"$X_0^2+X_s^2=1$" if spherical else r"$-X_0^2+X_s^2=-1,\quad X_0>0$",
                fontsize=16, color=blue)

        if spherical:
            theta = np.linspace(0, 2 * np.pi, 500)
            ax.plot(np.cos(theta), np.sin(theta), color=blue, lw=2.8)
            xs, x0 = 0.8, 0.6
            # A lower-hemisphere point demonstrates the unbounded image.
            xs2, x02 = -12 / 13, -5 / 13
            u2 = xs2 / (1 + x02)
            ax.plot([0, u2], [-1, 0], color=orange, lw=1.6, ls="--", alpha=0.7)
            ax.scatter([xs2], [x02], s=44, color=blue, zorder=5)
            ax.scatter([u2], [0], s=44, color=green, zorder=5)
            ax.text(xs2 - 0.08, x02 - 0.23, r"$X'$", ha="right", color=blue, fontsize=16)
            ax.text(u2 - 0.05, 0.13, r"$u'$", ha="right", color=green, fontsize=16)
            ax.text(0, -1.58, "Projection covers the entire plane", ha="center", fontsize=12,
                    transform=ax.transData, clip_on=False, color=green)
        else:
            xs_curve = np.linspace(-1.7, 1.7, 400)
            ax.plot(xs_curve, np.sqrt(1 + xs_curve ** 2), color=blue, lw=2.8)
            ax.plot([-1, 1], [0, 0], color=green, lw=4, solid_capstyle="butt")
            ax.scatter([-1, 1], [0, 0], s=55, facecolors="white", edgecolors=green, lw=1.8, zorder=5)
            ax.text(-1, -0.25, r"$-1$", ha="center", color=green, fontsize=16)
            ax.text(1, -0.25, r"$1$", ha="center", color=green, fontsize=16)
            xs, x0 = 1.2, np.sqrt(1 + 1.2 ** 2)
            ax.text(0, -1.58, "Inside the ball · boundary excluded", ha="center", fontsize=12,
                    transform=ax.transData, clip_on=False, color=green)

        u = xs / (1 + x0)
        ax.plot([0, xs], [-1, x0], color=orange, lw=1.5, alpha=0.6)
        ax.annotate("", xy=(u, 0), xytext=(xs, x0),
                    arrowprops={"arrowstyle": "->", "color": orange, "lw": 1.8,
                                "shrinkA": 8, "shrinkB": 8})
        ax.scatter([xs], [x0], s=65, color=blue, zorder=6)
        ax.scatter([u], [0], s=65, color=green, zorder=6)
        ax.scatter([0], [-1], s=65, color=orange, zorder=6)
        if spherical:
            ax.text(xs + 0.08, x0 + 0.09, r"$X$", color=blue, fontsize=18)
        else:
            ax.annotate(r"$X$", xy=(xs, x0), xytext=(-9, 10),
                        textcoords="offset points", ha="right", va="bottom",
                        color=blue, fontsize=18)
        ax.text(u + 0.09, 0.12, r"$u$", color=green, fontsize=18)
        ax.text(0.13, -1.13, r"$S=(-1,0)$", color=orange, fontsize=15)
        ax.text(0, -1.9, r"$u=\frac{X_s}{1+X_0}$", ha="center", fontsize=21,
                transform=ax.transData, clip_on=False)

    for stacked in (False, True):
        fig, axes = plt.subplots(2 if stacked else 1, 1 if stacked else 2,
                                 figsize=(6, 12.5) if stacked else (12, 6))
        fig.subplots_adjust(left=0.035, right=0.965, top=0.98, bottom=0.14,
                            hspace=0.36 if stacked else 0, wspace=0.12)
        for ax, spherical in zip(np.ravel(axes), (False, True)):
            draw_panel(ax, spherical)
        name = "model-projections-stacked" if stacked else "model-projections"
        fig.savefig(FIGURES / f"{name}.svg", facecolor="white", metadata={"Date": None},
                    bbox_inches="tight", pad_inches=0.15)
        fig.savefig(Path(tempfile.gettempdir()) / f"{name}.png", facecolor="white", dpi=160,
                    bbox_inches="tight", pad_inches=0.15)
        plt.close(fig)


if __name__ == "__main__":
    FIGURES.mkdir(parents=True, exist_ok=True)
    extract_survey_figures()
    plot_geometry()
    plot_model_projections()
