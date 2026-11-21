"""Replot published DocLayNet Table 2 mAP values; no training occurs here.

Source: Pfitzmann et al., KDD 2022, DOI 10.1145/3534678.3539043.
"""
from pathlib import Path
import matplotlib.pyplot as plt

MODELS = ["Mask R-CNN R50", "Mask R-CNN R101", "Faster R-CNN R101", "YOLOv5x6"]
MAP = [72.4, 73.5, 73.4, 76.8]


def main():
    output = Path(__file__).resolve().parents[1] / "results" / "doclaynet_baselines.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    bars = ax.bar(MODELS, MAP)
    ax.set_ylim(0, 100)
    ax.set_ylabel("mAP@0.5:0.95 (0–100)")
    ax.set_title("DocLayNet: Published Object Detection Baselines")
    ax.bar_label(bars, fmt="%.1f", padding=3)
    ax.tick_params(axis="x", labelrotation=12)
    fig.text(0.02, 0.01, "Source: Pfitzmann et al. (2022), Table 2. Revisualization only.", fontsize=8)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(output, dpi=200)
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
