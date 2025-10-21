---
title: "Hyperbolic Fine-tuning for Large Language Models (HypLoRA)"
layout: page
permalink: /work/hyplora
---

<link rel="stylesheet" href="/style.css">

<div style="text-align: right; margin-top: -3.5em; margin-bottom: 2em;">
<h2 style="color: #0366d6; font-size: 1.5em; font-weight: 600; margin: 0;">— Introducing HypLoRA: Hyperbolic Low-Rank Adaptation</h2>
</div>

Authors: Menglin Yang, Ram Samarth, Aosong Feng, Bo Xiong, Jihong Liu, Irwin King, Rex Ying


## Overview

Large language models typically learn in Euclidean space, which can be mismatched to the hierarchical, tree-like structure often present in language data. This work analyzes token embeddings and finds strong hyperbolic characteristics, with frequent (abstract) tokens clustered near the origin and rare (specific) tokens farther away. Building on this, HypLoRA performs efficient fine-tuning directly on the hyperbolic manifold to preserve non‑Euclidean inductive bias and improve reasoning, particularly on challenging problems. See the paper for full details and results. [arXiv PDF](https://arxiv.org/pdf/2410.04010)

## Abstract (from the paper)

Large language models (LLMs) have demonstrated remarkable performance on various tasks. However, it remains an open question whether the default Euclidean space is the most suitable choice for embedding tokens in LLMs. In this study, we investigate the non‑Euclidean characteristics of LLMs and show that token embeddings exhibit a high degree of hyperbolicity, suggesting a latent tree‑like structure. We introduce HypLoRA, a hyperbolic low‑rank efficient fine‑tuning method that adapts models directly on the hyperbolic manifold, avoiding cancellation effects from exponential/logarithmic maps. Experiments show significant gains on complex reasoning tasks, including up to 13.0% improvement on AQuA.

## Highlights

- Strong evidence of hyperbolic structure in LLM token embeddings (hierarchical, tree‑like).
- HypLoRA applies low‑rank adaptation directly on the hyperbolic manifold.
- Avoids cancellation from back‑to‑back exp/log maps used in tangent‑space approaches.
- Improves complex reasoning performance; benefits scale with token specificity norms.

## Paper and Code

- Paper (PDF): [Hyperbolic Fine-tuning for Large Language Models](https://arxiv.org/pdf/2410.04010)
- Code: [HypLLM GitHub Repository](https://github.com/marlin-codes/HypLLM)

## Citation

```bibtex
@article{yang2024hyperbolic,
  title={Hyperbolic Fine-tuning for Large Language Models},
  author={Yang, Menglin, Ram, Samarth and Feng, Aosong and Xiong, Bo and Liu, Jihong and King, Irwin and Ying, Rex},
  journal={arXiv preprint arXiv:2410.04010},
  year={2024}
}
```


