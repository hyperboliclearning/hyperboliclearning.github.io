---
title: "Hyperbolic and Non-Euclidean Geometry for LLMs"
layout: page
permlink: /
---

<div class="sticky-outline">
  <ul>
    <li><a href="#events-and-news">Events and News</a></li>
    <li><a href="#1-hyperbolic-geometry">Hyperbolic Geometry</a></li>
    <li><a href="#2-hyperbolic-models">Hyperbolic Models</a></li>
    <li><a href="#3-hyperbolic-neural-networks">Hyperbolic Neural Networks</a></li>
    <li><a href="#4-hyperbolic-transformers">Hyperbolic Transformers</a></li>
    <li><a href="#5-hyperbolic-foundation-models">Hyperbolic Foundation Models</a></li>
    <li><a href="#6-challenges-and-opportunities">Challenges and Opportunities</a></li>
    <li><a href="#7-conclusion">Conclusion</a></li>
    <li><a href="#references">References</a></li>
  </ul>
</div>

<style>
/* ---- Page-scoped overrides for tighter, more cohesive layout ---- */
.page-content h1 {
  text-align: center;
  margin-top: 0.2em;
  margin-bottom: 0.9em;
}
.page-content h1::before { display: none; }
/* ---- Section titles (h2): chapter-divider style ---- */
.page-content h2 {
  margin: 2em 0 0.6em 0;
  padding: 0.7em 0 0 0;
  font-size: 1.55em;
  font-weight: 700;
  color: var(--primary, #3a5a7c);
  letter-spacing: -0.015em;
  display: block;
  border-top: 2px solid var(--primary, #3a5a7c);
  position: relative;
}
.page-content h2::before {
  display: none !important;
  content: none !important;
}
/* The first h2 (Events and News!) gets a subtler treatment */
.page-content > h2:first-of-type {
  border-top: 1px solid var(--border, #e5e2dd);
  padding-top: 0.6em;
  margin-top: 0.3em;
}

/* ---- Subsection titles (h3): clean numbered marker ---- */
.page-content h3 {
  margin: 1.4em 0 0.5em 0;
  padding: 0;
  font-size: 1.12em;
  font-weight: 600;
  color: var(--primary, #3a5a7c);
  letter-spacing: -0.005em;
  border: none;
  display: block;
  position: relative;
}
.page-content h3::before,
.page-content h3::after {
  display: none !important;
  content: none !important;
}
/* No leading bar — clean, blue subsection title */
.page-content h3 {
  padding-left: 0;
  border-left: none;
  border-radius: 0;
}
.page-content p { margin-bottom: 0.85em; }
.page-content ul, .page-content ol { margin-bottom: 0.9em; }
.page-content li { margin-bottom: 0.25em; }

/* Body links use the same slate blue as subsection titles */
.page-content p a,
.page-content li a {
  color: var(--primary, #3a5a7c);
  text-decoration: none;
}
.page-content p a:hover,
.page-content li a:hover {
  color: var(--accent, #c0603c);
  text-decoration: underline;
}

/* ---- Critical-question callout (uses site primary palette) ---- */
.callout-question {
  background: linear-gradient(135deg, #f1f5f9 0%, #f7f5f2 100%);
  border-left: 4px solid var(--primary, #3a5a7c);
  color: var(--heading, #1e2a36);
  font-weight: 600;
  font-size: 1.02em;
  line-height: 1.6;
  padding: 0.95rem 1.2rem;
  margin: 1.1em 0;
  border-radius: 8px;
  box-shadow: 0 1px 4px rgba(58, 90, 124, 0.08);
}
.callout-question::before {
  content: "❝ ";
  color: var(--primary, #3a5a7c);
  font-size: 1.3em;
  font-weight: 700;
  margin-right: 0.15em;
}

/* ---- Math equations: hairlines hug the equation, not the text column ---- */
.math-block {
  background: transparent;
  border: none;
  border-top: 1px solid var(--border, #e5e2dd);
  border-bottom: 1px solid var(--border, #e5e2dd);
  border-radius: 0;
  padding: 0.7rem 1.4rem;
  margin: 1.1em auto;
  text-align: center;
  font-size: 1.08em;
  overflow-x: auto;
  color: var(--heading, #1e2a36);
  position: relative;
  width: fit-content;
  max-width: 100%;
}
.math-block::before {
  content: '';
  position: absolute;
  left: 0;
  top: -1px;
  width: 28px;
  height: 1px;
  background: var(--primary, #3a5a7c);
}
.math-block::after {
  content: '';
  position: absolute;
  right: 0;
  bottom: -1px;
  width: 28px;
  height: 1px;
  background: var(--primary, #3a5a7c);
}

/* ---- Citation block: matches palette ---- */
.cite-block {
  background: var(--bg, #f7f5f2);
  border: 1px solid var(--border, #e5e2dd);
  border-left: 3px solid var(--primary, #3a5a7c);
  border-radius: 8px;
  padding: 1rem 1.2rem;
  position: relative;
  margin-top: 0.8em;
}
.cite-block pre {
  margin: 0; color: var(--text, #3d424a); font-size: 0.78rem; line-height: 1.6;
  white-space: pre-wrap; word-break: break-all;
  font-family: 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace;
  background: transparent; padding: 0; border-radius: 0;
}
.cite-block .copy-btn {
  position: absolute; top: 0.6rem; right: 0.7rem;
  font-size: 0.72rem; color: var(--primary, #3a5a7c);
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  padding: 0.3em 0.8em; border-radius: 6px;
  cursor: pointer; transition: all 0.2s;
  font-family: 'Inter', sans-serif; font-weight: 600;
}
.cite-block .copy-btn:hover {
  background: var(--primary, #3a5a7c);
  color: #fff;
}

/* ---- Sticky outline ---- */
.sticky-outline {
  position: fixed;
  top: 80px;
  left: 20px;
  width: 175px;
  max-height: 60vh;
  overflow-y: auto;
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  padding: 10px 8px;
  z-index: 1000;
  font-size: 0.7rem;
  text-align: left;
  display: none;
}
@media (min-width: 1300px) {
  .sticky-outline { display: block; }
}
.sticky-outline ul { list-style: none; padding: 0; margin: 0; text-align: left; }
.sticky-outline > ul > li { margin-bottom: 2px; text-align: left; }
.sticky-outline li { margin-bottom: 1px; text-align: left; }
.sticky-outline > ul > li > a {
  font-weight: 600; font-size: 0.9rem; padding: 1px 0; text-align: left;
}
.sticky-outline a {
  color: var(--primary, #3a5a7c);
  text-decoration: none;
  transition: color 0.2s;
  display: block;
  padding: 1px 0;
  text-align: left;
  font-weight: 600;
}
.sticky-outline a:hover {
  color: var(--accent, #c0603c);
  text-decoration: underline;
}

/* ---- Figures ---- */
.fig-container {
  text-align: center;
  margin: 1.2em 0;
}
.fig-container img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  border: 1px solid var(--border, #e5e2dd);
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}
.fig-container .fig-cap {
  font-size: 0.86em;
  color: var(--text-soft, #6b7280);
  margin-top: 0.5em;
  font-style: italic;
  line-height: 1.5;
}

/* ---- News list icons ---- */
.news-list { list-style: none; padding-left: 0; }
.news-list li {
  display: flex;
  align-items: flex-start;
  gap: 0.55em;
  padding: 0.25em 0;
  margin-bottom: 0.15em;
  line-height: 1.55;
}
.news-icon {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.25em;
  height: 1.25em;
  margin-top: 0.18em;
  font-size: 0.95em;
}
.news-icon svg { width: 100%; height: 100%; display: block; }
.news-updated {
  margin-top: 0.6em;
  font-size: 0.82em;
  color: var(--text-soft, #6b7280);
  font-style: italic;
  text-align: right;
}
/* Featured news item highlight */
.news-list li.featured {
  background: rgba(58, 90, 124, 0.10);
  border-left: 3px solid var(--primary, #3a5a7c);
  border-radius: 6px;
  padding: 0.45em 0.7em;
  margin-bottom: 0.3em;
}

/* ---- Section divider for Challenges/Opportunities ---- */
.section-lead {
  color: var(--primary, #3a5a7c);
  font-weight: 600;
  font-size: 1.02em;
  margin: 0.6em 0 0.4em 0;
  padding-left: 0.7rem;
  border-left: 3px solid var(--primary, #3a5a7c);
}

/* ---- References ---- */
.refs-list { padding-left: 1.4em; font-size: 0.9em; line-height: 1.55; color: var(--text, #3d424a); }
.refs-list li { margin-bottom: 0.45em; }
.refs-list a { color: var(--primary, #3a5a7c); }
.refs-list a:hover { color: var(--accent, #c0603c); }
</style>

<script>
MathJax = { tex: { inlineMath: [['$','$'], ['\\(','\\)']], displayMath: [['$$','$$'], ['\\[','\\]']] } };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>

## Events and News!

<ul class="news-list">
  <li><span class="news-icon" title="Paper">📄</span><a href="https://arxiv.org/pdf/2405.03188">ICML 2026 · HypRAG: Hyperbolic Dense Retrieval for Retrieval Augmented Generation (PDF)</a></li>
  <li><span class="news-icon" title="GitHub"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#24292f"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></span><a href="https://github.com/graph-and-geometric-learning/helm">NeurIPS 2025 HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts - GitHub</a></li>
  <li><span class="news-icon" title="Project page">📝</span><a href="{{ "/work/hyplora" | relative_url }}">NeurIPS 2025 Hyperbolic Fine-tuning for Large Language Models (HypLoRA)</a></li>
  <li class="featured"><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/kdd2026workshop" | relative_url }}">KDD 2026 Geometric Learning Workshop</a> <span style="font-size:0.95em">🔥</span></li>
  <li><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/neurips2025negelworkshop" | relative_url }}">NeurIPS 2025 NEGEL Workshop</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="{{ "/events/aaai2026tutorial" | relative_url }}">AAAI 2026 Hyperbolic FM Tutorial</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="{{ "/events/kdd2025tutorial" | relative_url }}">KDD 2025 Hyperbolic FM Tutorial</a></li>
  <li><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/www2025workshop" | relative_url }}">WWW 2025 NEGEL Workshop</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="https://hyperbolicgnn.github.io/">KDD 2023 Tutorial</a></li>
  <li><span class="news-icon" title="Slack"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path fill="#E01E5A" d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313z"/><path fill="#36C5F0" d="M8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312z"/><path fill="#2EB67D" d="M18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312z"/><path fill="#ECB22E" d="M15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg></span><a href="https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA">Slack channel for more discussions and tracking updates!</a></li>
  <li><span class="news-icon" title="Repository">⭐</span><a href="{{ "/collection" | relative_url }}">Awesome Hyperbolic Representation and Deep Learning Repository</a></li>
</ul>

<p class="news-updated">Last updated: May 5, 2026</p>

## Introduction

Foundation models, including large language models (LLMs), vision-language models (VLMs), and large multimodal models, are pre-trained on massive datasets and have demonstrated remarkable success across diverse downstream tasks. Models such as GPT-4, LLaMA, CLIP, and Gemini have pushed the boundaries of natural language understanding, visual reasoning, and cross-modal generation. Despite these achievements, recent studies have identified three fundamental limitations rooted in their reliance on Euclidean geometry:

- **Limited representational capacity** for hierarchical and structured data, where shallow Euclidean embeddings struggle to preserve tree-like relations.
- **Lower adaptability** when fine-tuning on tasks with inherent geometric structure, leading to suboptimal transfer on knowledge- and reasoning-intensive benchmarks.
- **Less efficient scaling**, since the polynomial volume growth of Euclidean space cannot match the exponential branching of real-world hierarchies, forcing the use of high-dimensional embeddings.

These shortcomings raise a critical question:

<div class="callout-question">Is Euclidean geometry truly the optimal inductive bias for foundation models, or could alternative geometric spaces better align with the intrinsic structure of real-world data and reasoning processes?</div>

Consider a simple example. Natural language inherently contains hierarchical structures, where words compose phrases, phrases compose sentences, and sentences compose paragraphs. Knowledge graphs likewise encode taxonomic relationships (e.g., "animal → mammal → dog → poodle") that grow exponentially with depth. In Euclidean space, representing a balanced binary tree of depth $d$ with low distortion requires $\mathcal{O}(2^d)$ dimensions, whereas in hyperbolic space the same tree can be faithfully embedded in just **2 dimensions** [Sarkar, 2011]. This exponential advantage motivates the exploration of hyperbolic geometry as a foundational building block for modern AI systems.

<div class="fig-container" style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
  <img src="/images/figs/root-leaf.png" alt="Root-leaf proximity in hyperbolic space" style="flex: 1 1 48%; min-width: 280px;">
  <img src="/images/figs/leaf-leaf.png" alt="Leaf-leaf distance in hyperbolic space" style="flex: 1 1 48%; min-width: 280px;">
</div>
<div class="fig-container" style="margin-top: 0;">
  <div class="fig-cap">Figure 1: Hyperbolic space naturally encodes hierarchical structure. <strong>Left</strong>: Root and leaf nodes are close in hyperbolic distance, reflecting parent-child relationships. <strong>Right</strong>: Leaf nodes from different branches are far apart, preserving the tree's branching structure. The exponential volume growth of hyperbolic space enables faithful low-distortion embeddings of trees.</div>
</div>

This webpage provides a comprehensive overview of hyperbolic geometry and non-Euclidean representations for large language models and foundation models. We cover the mathematical foundations, key computational models, neural network architectures, and state-of-the-art methods that bring hyperbolic geometry to modern AI.


## 1. Hyperbolic Geometry

Hyperbolic geometry represents one of the most profound developments in mathematical history, emerging from the centuries-long quest to understand Euclid's fifth postulate (the parallel postulate). For over two thousand years, mathematicians attempted to derive the parallel postulate from the other four axioms. It was not until the 19th century that Lobachevsky, Bolyai, and Gauss independently discovered that rejecting the parallel postulate leads to a consistent, non-Euclidean geometry, namely **hyperbolic geometry**.

Unlike Euclidean geometry, where exactly one parallel line passes through a given external point, **hyperbolic geometry permits infinitely many parallel lines through a point external to a given line**. This fundamental difference creates a geometric space with **constant negative curvature** $\kappa < 0$, contrasting with the flat (zero curvature) Euclidean space and the positive curvature of spherical geometry.

### 1.1 Key Properties of Hyperbolic Space

The distinctive properties of hyperbolic spaces set them apart from Euclidean geometry in ways that are profoundly useful for machine learning:

- **Exponential volume growth**: The area of a disk of radius $r$ in hyperbolic space grows as $\mathcal{O}(e^{r})$, compared to $\mathcal{O}(r^2)$ in Euclidean space. This means hyperbolic space can "fit" exponentially more content at increasing distances from the origin, precisely matching the branching factor of trees and hierarchies.

- **Triangle angle deficit**: The sum of angles in a hyperbolic triangle is always **strictly less than $\pi$** (180°), with the deficit proportional to the triangle's area. Specifically, for a triangle with angles $\alpha, \beta, \gamma$ and curvature $\kappa$, the area equals $(\pi - \alpha - \beta - \gamma) / \lvert\kappa\rvert$.

- **Distance distortion**: Distances grow exponentially as one moves away from the origin. In the Poincaré disk model, the metric tensor is $g_{ij} = \frac{4}{(1 - \lVert \mathbf{x}\rVert^2)^2}\delta_{ij}$, meaning distances near the boundary of the disk are dramatically stretched. A point that appears close to the boundary in visual coordinates is therefore actually infinitely far from the center.

- **Natural hierarchy representation**: A regular tree with branching factor $b$ and depth $d$ has $\mathcal{O}(b^d)$ nodes. The exponential volume growth of hyperbolic space naturally accommodates such structures, enabling low-distortion embeddings with remarkably few dimensions.

### 1.2 Why Hyperbolic Geometry for AI?

Real-world data frequently exhibits hierarchical or scale-free structure. Natural language has syntactic parse trees, knowledge graphs form taxonomies, protein structures involve nested sub-domains, social networks display community hierarchies, and image features organize from low-level textures to high-level semantics. The **Gromov $\delta$-hyperbolicity** of many real-world graphs (small $\delta$ values indicate tree-like structure) confirms that these datasets are intrinsically more hyperbolic than Euclidean [Gromov, 1987; Adcock et al., 2013], providing a principled motivation for leveraging hyperbolic representations in deep learning.


## 2. Hyperbolic Models

To visualize and work with hyperbolic geometry computationally, mathematicians have developed several isometric models. Each model represents the same underlying hyperbolic space but offers different computational trade-offs. Understanding these models is essential for designing hyperbolic neural networks.

### 2.1 Poincaré Ball Model

The Poincaré ball model $(\mathbb{B}^n_\kappa, g^{\mathbb{B}})$ represents $n$-dimensional hyperbolic space as the interior of the unit ball $\mathbb{B}^n = \{\mathbf{x} \in \mathbb{R}^n : \lVert \mathbf{x}\rVert < 1\}$. The Riemannian metric is given by:

<div class="math-block">
$g^{\mathbb{B}}_{\mathbf{x}} = \left(\frac{2}{1 - \lVert \mathbf{x}\rVert^2}\right)^2 g^E$
</div>

where $g^E$ is the Euclidean metric. This model is **conformal** (preserves angles but distorts distances) and is the most widely used in machine learning thanks to its intuitive visualization properties: the origin represents the "root" of a hierarchy, while branches spread toward the boundary. Key operations include the **Möbius addition** $\mathbf{x} \oplus_\kappa \mathbf{y}$ and the **exponential/logarithmic maps** that transport vectors between the tangent space and the manifold [Ungar, 2008; Ganea et al., 2018].

### 2.2 Lorentz (Hyperboloid) Model

The Lorentz model $(\mathbb{H}^n_\kappa, g^{\mathbb{L}})$ embeds hyperbolic space as the upper sheet of a hyperboloid in $(n+1)$-dimensional Minkowski space:

<div class="math-block">
$\mathbb{H}^n = \{\mathbf{x} \in \mathbb{R}^{n+1} : \langle \mathbf{x}, \mathbf{x} \rangle_{\mathcal{L}} = -1/\kappa, \; x_0 > 0\}$
</div>

where \\(\langle \mathbf{x}, \mathbf{y} \rangle\_{\mathcal{L}} = -x\_0 y\_0 + \sum\_{i=1}^{n} x\_i y\_i\\) is the Minkowski inner product. The Lorentz model has **superior numerical stability** compared to the Poincaré model (avoiding the boundary singularity) and is often preferred for optimization. The geodesic distance is:

<div class="math-block">
$d_{\mathbb{H}}(\mathbf{x}, \mathbf{y}) = \frac{1}{\sqrt{\lvert\kappa\rvert}} \operatorname{arccosh}\!\big(-\kappa \langle \mathbf{x}, \mathbf{y} \rangle_{\mathcal{L}}\big)$
</div>

### 2.3 Klein Model

The Klein model represents hyperbolic space within a disk where **geodesics appear as straight chords** rather than arcs. While it distorts both angles and distances, it offers computational simplicity for certain geometric operations such as computing convex hulls and determining whether points lie on the same geodesic. The metric is non-conformal, making it less popular in neural network applications but valuable for geometric algorithms.

### 2.4 Poincaré Half-Plane Model

The upper half-plane model $\mathbb{U}^n = \{\mathbf{x} \in \mathbb{R}^n : x_n > 0\}$ with metric $g^{\mathbb{U}}_{\mathbf{x}} = \frac{1}{x_n^2} g^E$ offers an unbounded representation of hyperbolic space. It is particularly useful for theoretical analysis and has deep connections to complex analysis and modular forms. Like the Poincaré ball, it is conformal.

### 2.5 Inter-Model Mappings

All four models are isometric to one another, and explicit diffeomorphisms exist between them. In practice, researchers often perform **forward computation in the Lorentz model** (for numerical stability) and **visualization in the Poincaré ball** (for interpretability), converting between models as needed.


## 3. Hyperbolic Neural Networks

Hyperbolic neural networks extend deep learning architectures to operate directly in hyperbolic space, enabling more efficient representation of hierarchical data. **The core insight is that hierarchical relationships demand exponentially increasing capacity at greater depths, which is exactly the regime in which hyperbolic spaces excel due to their exponential volume growth.**

### 3.1 Hyperbolic Embeddings

Hyperbolic embeddings represent discrete objects (such as nodes in a graph or words in a vocabulary) as points in hyperbolic space. The seminal work of [Nickel and Kiela (2017)](https://arxiv.org/abs/1705.08039) demonstrated that **Poincaré embeddings** of the WordNet noun hierarchy could achieve superior performance with just 5 dimensions compared to 200-dimensional Euclidean embeddings. Subsequent work introduced embeddings in the Lorentz model for improved optimization stability [[Nickel and Kiela, 2018](https://arxiv.org/abs/1806.03417)].

Key advantages of hyperbolic embeddings include:
- **Dimensionality reduction**: Orders-of-magnitude fewer parameters for hierarchical data
- **Implicit hierarchy preservation**: Distance from the origin encodes hierarchical depth
- **Continuous relaxation of trees**: Hyperbolic space serves as a continuous analogue of discrete tree structures

### 3.2 Hyperbolic Neural Layers

Since hyperbolic space is a Riemannian manifold (not a vector space), standard operations like matrix multiplication and addition must be carefully redefined. Three main paradigms have emerged:

- **Tangent space approach**: Map points to the tangent space at a reference point (typically the origin), apply standard Euclidean operations, and project back using the exponential map. This is computationally efficient but introduces approximation errors, especially for points far from the reference.

- **Möbius gyrovector approach**: The Möbius addition $\oplus_\kappa$ and Möbius scalar multiplication $\otimes_\kappa$ provide intrinsic operations in the Poincaré ball that generalize their Euclidean counterparts. A hyperbolic linear layer can be defined as $f(\mathbf{x}) = \mathbf{M} \otimes_\kappa \mathbf{x} \oplus_\kappa \mathbf{b}$, where $\mathbf{M}$ is a learnable weight matrix and $\mathbf{b}$ is a bias in hyperbolic space.

- **Lorentz operations**: Directly define neural network operations on the hyperboloid using the Lorentz inner product and parallel transport. This approach often yields better numerical stability and has become increasingly popular in recent architectures.

### 3.3 Key Architectures

Several foundational hyperbolic architectures have been developed:

- **[HGCN](https://arxiv.org/abs/1910.12933)** (Hyperbolic Graph Convolutional Networks) [Chami et al., 2019]: Extends GCNs to hyperbolic space, achieving state-of-the-art on hierarchical graph benchmarks
- **[HNN](https://arxiv.org/abs/1805.09112) / [HNN++](https://arxiv.org/abs/2006.08210)** (Hyperbolic Neural Networks) [Ganea et al., 2018; Shimizu et al., 2021]: General-purpose hyperbolic feedforward and recurrent networks
- **[HGNN](https://arxiv.org/abs/1910.12892)** (Hyperbolic Graph Neural Networks) [Liu et al., 2019]: Message-passing framework adapted for hyperbolic geometry
- **[Fully Hyperbolic Neural Networks](https://arxiv.org/abs/2105.14686)** [Chen et al., 2022]: Builds every layer (linear, attention, normalization) directly on the Lorentz model via Lorentz transformations, removing the need for repeated tangent-space mappings and improving stability for deeper networks
- **[\\(\kappa\\)-GCN](https://arxiv.org/abs/1911.05076)** [Bachmann et al., 2020]: Operates in the stereographic model with learnable curvature, unifying hyperbolic (\\(\kappa < 0\\)), Euclidean (\\(\kappa = 0\\)), and spherical (\\(\kappa > 0\\)) geometries

### 3.4 Hyperbolic Activation Functions

Standard activation functions (ReLU, tanh, sigmoid) operate in Euclidean space and cannot be directly applied to hyperbolic points. Hyperbolic activation functions are typically defined by: (1) projecting to tangent space via the logarithmic map, (2) applying the Euclidean activation, and (3) mapping back via the exponential map. More recent approaches define intrinsic activations that avoid this intermediate mapping.

### 3.5 Optimization in Hyperbolic Space

Training hyperbolic networks requires **Riemannian optimization**, where gradients are computed in the tangent space and updates follow geodesics rather than straight lines. Riemannian SGD and Riemannian Adam have been developed for this purpose [Bonnabel, 2013; [Bécigneul and Ganea, 2019](https://arxiv.org/abs/1810.00760)], with the update rule:

<div class="math-block">
$\mathbf{x}_{t+1} = \mathrm{exp}_{\mathbf{x}_t}\!\big(-\eta \cdot \mathrm{grad}_R\, f(\mathbf{x}_t)\big)$
</div>

where $\mathrm{exp}_{\mathbf{x}_t}$ is the exponential map and $\mathrm{grad}_R$ is the Riemannian gradient.


## 4. Hyperbolic Transformers

Transformer architectures revolutionized natural language processing through their self-attention mechanisms and efficient parallel processing of sequential data. **Hyperbolic transformers extend this paradigm to hyperbolic space, particularly benefiting applications involving deeply nested linguistic structures, hierarchical relations, and multi-scale features.**

The key challenge in building hyperbolic transformers is that the self-attention mechanism relies heavily on linear algebra operations (queries, keys, values via matrix multiplication, softmax normalization) that assume Euclidean structure. Adapting each component to respect hyperbolic geometry requires careful mathematical reformulation.

### 4.1 Hyperbolic Attention Mechanisms

The standard attention score $\mathrm{Attn}(\mathbf{Q}, \mathbf{K}) = \mathrm{softmax}(\mathbf{Q}\mathbf{K}^\top / \sqrt{d_k})$ can be reformulated using hyperbolic distance:

<div class="math-block">
$\alpha_{ij} = \mathrm{softmax}\!\left(-\beta \cdot d_{\mathbb{H}}(\mathbf{q}_i, \mathbf{k}_j)^2\right)$
</div>

where $d_{\mathbb{H}}$ is the hyperbolic distance and $\beta$ is a learnable temperature. This formulation naturally emphasizes hierarchical relationships: tokens at similar hierarchical levels (similar distance from the origin) produce stronger attention scores, while cross-level attention captures parent-child dependencies.

Alternative formulations include:
- **Lorentz attention**: Using the Minkowski inner product \\(\langle \mathbf{q}\_i, \mathbf{k}\_j \rangle\_{\mathcal{L}}\\) directly as an attention score
- **Tangent-space attention**: Computing standard dot-product attention in the tangent space, then projecting results back
- **Hybrid attention**: Combining Euclidean and hyperbolic attention heads within the same layer

### 4.2 Multi-Resolution Processing

One of the most compelling advantages of hyperbolic transformers is their ability to simultaneously process information at different scales. In the Poincaré disk, points near the center capture high-level, coarse-grained information (analogous to root-level concepts), while points near the boundary encode fine-grained details (analogous to leaf-level specifics). This natural multi-resolution property enables hyperbolic transformers to process hierarchical abstractions more efficiently than their Euclidean counterparts.

### 4.3 Hyperbolic Position Encodings

Position encodings adapted to hyperbolic geometry can better preserve hierarchical relationships between tokens. Instead of sinusoidal or learned Euclidean position vectors, **hyperbolic position encodings** place position information on the manifold, where the distance structure naturally encodes both sequential order and hierarchical depth. For example, in a document with sections, subsections, and paragraphs, hyperbolic position encodings can jointly capture both the linear reading order and the nesting structure.

### 4.4 Notable Hyperbolic Transformer Models

- **[HyboNet](https://arxiv.org/abs/2105.14686)** [Chen et al., 2022]: Builds attention, feed-forward, and normalization layers directly on the Lorentz model via Lorentz transformations, enabling fully hyperbolic computation without repeated tangent-space mappings
- **[Hypformer](https://arxiv.org/abs/2407.01290)** [Yang et al., 2024]: A fully hyperbolic Transformer in the Lorentz model that introduces foundational hyperbolic modules and a linear self-attention mechanism, enabling efficient processing of large-scale graphs and long sequences
- **[Mixed-Curvature Transformers](https://openreview.net/forum?id=HJxeWnCcF7)** [Gu et al., 2019]: Use product manifolds that combine hyperbolic, Euclidean, and spherical components, with curvatures learned per factor


## 5. Hyperbolic Foundation Models

Foundation models, namely large-scale systems trained on broad data and then fine-tuned for specific applications, represent the cutting edge of modern AI. **Hyperbolic foundation models incorporate hyperbolic geometry into their architecture to better capture the hierarchical structures inherent in language, knowledge, and multimodal data.** This forms one of the most active and promising frontiers in geometric deep learning.

### 5.1 Hyperbolic Large Language Models

Recent work has demonstrated that incorporating hyperbolic geometry into LLMs yields measurable improvements:

- **[HypLoRA]({{ "/work/hyplora" | relative_url }})** [Yang et al., 2025]: Introduces hyperbolic low-rank adaptation for fine-tuning LLMs. By performing LoRA updates in hyperbolic space, HypLoRA better captures the hierarchical nature of downstream tasks while maintaining the parameter efficiency of standard LoRA. Experiments show consistent gains on commonsense reasoning, natural language understanding, and mathematical reasoning benchmarks.

- **[HELM](https://arxiv.org/abs/2505.24722)** [He et al., 2025]: Hyperbolic LLMs via Mixture-of-Curvature Experts. Proposes a mixture-of-experts architecture where different experts operate in spaces of different curvatures (hyperbolic, Euclidean, spherical), allowing the model to adaptively select the optimal geometry for each input.

- **Hyperbolic Token Embeddings**: Replacing standard Euclidean token embeddings with hyperbolic embeddings can improve the representation of taxonomic and compositional relationships, especially benefiting tasks involving structured knowledge.

### 5.2 Hyperbolic Vision Foundation Models

Visual data exhibits hierarchical structure at multiple levels, ranging from pixels to textures, parts, objects, and scenes. Hyperbolic vision models exploit this:

- **[Hyperbolic Image Embeddings](https://arxiv.org/abs/1904.02239)** [Khrulkov et al., 2020]: Mapping image features to hyperbolic space for improved zero-shot and few-shot classification, especially when label hierarchies are available (e.g., ImageNet's WordNet-based class taxonomy)
- **[MERU](https://arxiv.org/abs/2304.09172)** (Hyperbolic CLIP) [Desai et al., 2023]: Adapting CLIP-style contrastive learning to hyperbolic space, enabling better cross-modal alignment of hierarchical visual and linguistic concepts
- **[Hyperbolic ViT](https://arxiv.org/abs/2203.10833)** [Ermolov et al., 2022]: Vision Transformers with hyperbolic attention and position encodings

### 5.3 Hyperbolic Multi-Modal Models

Multi-modal foundation models (e.g., combining vision, language, and audio) benefit from hyperbolic geometry through:

- **Cross-Modal Hierarchical Alignment**: Different modalities often share hierarchical structure (e.g., a visual scene graph and a textual description both encode part-whole relationships). Hyperbolic space provides a natural shared geometry for aligning these hierarchies.
- **Compositional Grounding**: Hyperbolic representations can better capture the compositional nature of language and visual scenes, where meanings compose hierarchically.
- **Efficient Multi-Modal Fusion**: The parameter efficiency of hyperbolic representations reduces the overhead of multi-modal fusion layers.

### 5.4 Key Advantages

• **Improved Knowledge Representation**: Hyperbolic foundation models can more efficiently encode taxonomic knowledge, ontological relationships, and compositional semantics, potentially reducing parameter counts while improving performance on tasks requiring hierarchical understanding.

• **Enhanced Reasoning Capabilities**: The natural tree-like structure of hyperbolic space aligns with logical hierarchies and deductive reasoning patterns, potentially enabling more sophisticated chain-of-thought and structured reasoning abilities.

• **More Efficient Scaling**: The intrinsic capacity of hyperbolic space to represent exponentially more information within the same dimensionality suggests better scaling properties as model sizes increase. This is a critical factor given the computational cost of modern foundation models.

• **Cross-Modal Hierarchical Alignment**: For multimodal foundation models, hyperbolic representations may better align hierarchical structures across different modalities (e.g., visual scene graphs with linguistic parse trees), improving performance on complex cross-modal tasks.


## 6. Challenges and Opportunities

<div class="section-lead">While hyperbolic deep learning demonstrates significant promise, several important challenges remain:</div>

• **Numerical Stability**: Hyperbolic operations involve exponential and hyperbolic trigonometric functions that can lead to overflow/underflow, especially near the boundary of the Poincaré disk where the conformal factor $\lambda_{\mathbf{x}} = \frac{2}{1-\lVert \mathbf{x}\rVert^2}$ diverges. Techniques such as **clipping norms**, **working in the Lorentz model**, and **mixed-precision training** have been developed to mitigate these issues, but a general solution remains elusive.

• **Optimization Difficulties**: Riemannian optimization (RSGD, RAdam) in hyperbolic space is more complex than standard gradient descent. The curvature of the space introduces additional terms in the update rules, and **learning rate sensitivity** is amplified, since points near the boundary of the Poincaré disk experience much larger effective step sizes. Developing efficient, stable, and scalable Riemannian optimizers is an active research area.

• **Scalability to Large Models**: While hyperbolic methods have shown success at moderate scales, scaling to billions of parameters introduces engineering challenges. GPU-efficient implementations of hyperbolic operations, memory-efficient training strategies, and distributed Riemannian optimization are needed to bring hyperbolic methods to production-scale foundation models.

• **Integration with Existing Architectures**: Seamlessly combining hyperbolic components with traditional Euclidean deep learning modules presents both theoretical and implementation challenges. **Hybrid approaches** that selectively apply hyperbolic geometry to specific components (e.g., embedding layers or attention modules) while keeping other components Euclidean have shown promise as a practical middle ground.

• **Theoretical Understanding**: The theoretical foundations of hyperbolic deep learning are still developing. Key open questions include: generalization bounds for hyperbolic networks, the expressiveness gap between hyperbolic and Euclidean representations, optimal curvature selection strategies, and the approximation theory of functions on hyperbolic manifolds.

• **Learnable Curvature**: The curvature parameter $\kappa$ significantly affects representation quality, but it is often treated as a hyperparameter. Learning curvature jointly with model parameters, or using **product manifolds with mixed curvatures**, remains a promising but challenging direction.

<div class="section-lead">Despite these challenges, hyperbolic geometry in deep learning presents exciting opportunities:</div>

• **Extreme Efficiency in Hierarchical Tasks**: For applications dominated by tree-like structures (taxonomies, ontologies, organizational charts), hyperbolic approaches could dramatically reduce model size while improving performance, achieving "more with less."

• **Novel Architectural Paradigms**: Fully embracing non-Euclidean geometry may inspire fundamentally new neural network architectures beyond current paradigms, analogous to how the Transformer architecture revolutionized sequence modeling.

• **Cross-Disciplinary Insights**: The integration of differential geometry, algebraic topology, and Riemannian optimization with deep learning opens possibilities for importing powerful techniques from mathematics and theoretical physics into machine learning.

• **Biologically Inspired Representations**: Growing evidence suggests that biological neural systems may utilize hyperbolic-like representations for spatial navigation and conceptual organization. This connection offers insights for neuromorphic computing and cognitive architectures.

• **AI for Science**: Hyperbolic representations are particularly well-suited for scientific data with inherent hierarchical structure, including molecular graphs, protein folding hierarchies, phylogenetic trees, and multi-scale physical simulations.


## 7. Conclusion

Hyperbolic geometry provides a powerful mathematical framework for enhancing deep learning systems, particularly for applications involving hierarchical, tree-like structures that are ubiquitous in natural language, knowledge representation, computer vision, and scientific data. **The intersection of hyperbolic geometry and artificial intelligence represents a frontier where mathematical elegance meets practical utility**, potentially addressing fundamental limitations of traditional Euclidean approaches.

As research progresses, we can expect hyperbolic methods to become increasingly integrated into mainstream deep learning systems, particularly for knowledge-intensive applications requiring multi-scale reasoning. The development of stable, efficient hyperbolic operations and their thoughtful integration into neural architectures promises significant advances in AI's ability to represent and reason about complex hierarchical structures.

Key directions to watch include: **(1)** scaling hyperbolic foundation models to billions of parameters, **(2)** mixed-curvature and product manifold approaches that adaptively combine different geometries, **(3)** hyperbolic methods for reasoning and planning in LLM agents, and **(4)** applications in AI for science where hierarchical structure is a first-class concern.

We invite the community to join us in advancing this exciting research direction. Please refer to our [events page]({{ "/events" | relative_url }}) for upcoming workshops and tutorials, and our [collection page]({{ "/collection" | relative_url }}) for a comprehensive literature reference.


## Contributors

Menglin Yang, Neil He, Hiren Madhu, Ngoc Bui, Ali Maatouk, Rishabh Anand, Yifei Zhang, Jialin Chen, Jiahong Liu, Bo Xiong, Min Zhou, Irwin King, Melanie Weber, Rex Ying

Invited Speakers: Philip S. Yu, Shirui Pan, Min Zhou, Pascal Mettes, Smita Krishnaswamy

## References

<ol class="refs-list">
  <li>Adcock, A. B., Sullivan, B. D., & Mahoney, M. W. (2013). <em>Tree-like structure in large social and information networks.</em> ICDM.</li>
  <li>Bachmann, G., Bécigneul, G., & Ganea, O. (2020). <em>Constant Curvature Graph Convolutional Networks.</em> ICML. <a href="https://arxiv.org/abs/1911.05076">arXiv:1911.05076</a></li>
  <li>Bécigneul, G., & Ganea, O. (2019). <em>Riemannian Adaptive Optimization Methods.</em> ICLR. <a href="https://arxiv.org/abs/1810.00760">arXiv:1810.00760</a></li>
  <li>Bonnabel, S. (2013). <em>Stochastic Gradient Descent on Riemannian Manifolds.</em> IEEE Transactions on Automatic Control, 58(9).</li>
  <li>Chami, I., Ying, R., Ré, C., & Leskovec, J. (2019). <em>Hyperbolic Graph Convolutional Neural Networks.</em> NeurIPS. <a href="https://arxiv.org/abs/1910.12933">arXiv:1910.12933</a></li>
  <li>Chen, W., Han, X., Lin, Y., Zhao, H., Liu, Z., Li, P., Sun, M., & Zhou, J. (2022). <em>Fully Hyperbolic Neural Networks.</em> ACL. <a href="https://arxiv.org/abs/2105.14686">arXiv:2105.14686</a></li>
  <li>Desai, K., Nickel, M., Rajpurohit, T., Johnson, J., & Vedantam, R. (2023). <em>Hyperbolic Image-Text Representations (MERU).</em> ICML. <a href="https://arxiv.org/abs/2304.09172">arXiv:2304.09172</a></li>
  <li>Ermolov, A., Mirvakhabova, L., Khrulkov, V., Sebe, N., & Oseledets, I. (2022). <em>Hyperbolic Vision Transformers: Combining Improvements in Metric Learning.</em> CVPR. <a href="https://arxiv.org/abs/2203.10833">arXiv:2203.10833</a></li>
  <li>Ganea, O., Bécigneul, G., & Hofmann, T. (2018). <em>Hyperbolic Neural Networks.</em> NeurIPS. <a href="https://arxiv.org/abs/1805.09112">arXiv:1805.09112</a></li>
  <li>Gromov, M. (1987). <em>Hyperbolic Groups.</em> In Essays in Group Theory, MSRI Publ., Springer.</li>
  <li>Gu, A., Sala, F., Gunel, B., & Ré, C. (2019). <em>Learning Mixed-Curvature Representations in Product Spaces.</em> ICLR. <a href="https://openreview.net/forum?id=HJxeWnCcF7">OpenReview</a></li>
  <li>He, N., Yang, M., et al. (2025). <em>HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts.</em> NeurIPS. <a href="https://arxiv.org/abs/2505.24722">arXiv:2505.24722</a></li>
  <li>Khrulkov, V., Mirvakhabova, L., Ustinova, E., Oseledets, I., & Lempitsky, V. (2020). <em>Hyperbolic Image Embeddings.</em> CVPR. <a href="https://arxiv.org/abs/1904.02239">arXiv:1904.02239</a></li>
  <li>Liu, Q., Nickel, M., & Kiela, D. (2019). <em>Hyperbolic Graph Neural Networks.</em> NeurIPS. <a href="https://arxiv.org/abs/1910.12892">arXiv:1910.12892</a></li>
  <li>Nickel, M., & Kiela, D. (2017). <em>Poincaré Embeddings for Learning Hierarchical Representations.</em> NeurIPS. <a href="https://arxiv.org/abs/1705.08039">arXiv:1705.08039</a></li>
  <li>Nickel, M., & Kiela, D. (2018). <em>Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry.</em> ICML. <a href="https://arxiv.org/abs/1806.03417">arXiv:1806.03417</a></li>
  <li>Sarkar, R. (2011). <em>Low Distortion Delaunay Embedding of Trees in Hyperbolic Plane.</em> Graph Drawing.</li>
  <li>Shimizu, R., Mukuta, Y., & Harada, T. (2021). <em>Hyperbolic Neural Networks++.</em> ICLR. <a href="https://arxiv.org/abs/2006.08210">arXiv:2006.08210</a></li>
  <li>Ungar, A. A. (2008). <em>Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity.</em> World Scientific.</li>
  <li>Yang, M., Verma, H., Zhang, D. C., Liu, J., King, I., & Ying, R. (2024). <em>Hypformer: Exploring Efficient Transformer Fully in Hyperbolic Space.</em> KDD. <a href="https://arxiv.org/abs/2407.01290">arXiv:2407.01290</a></li>
  <li>Yang, M. et al. (2025). <em>Hyperbolic Fine-tuning for Large Language Models (HypLoRA).</em> NeurIPS.</li>
</ol>


## Citation

If you find this webpage useful, please consider citing our work:

<div class="cite-block">
  <button class="copy-btn" onclick="copyBib(this)">Copy</button>
  <pre id="bib-text">@article{yang2026hyperbolic,
  title     = {Hyperbolic Geometry and Non-Euclidean Representations
               for Large Language Models},
  author    = {Yang, Menglin and He, Neil and Madhu, Hiren and
               Bui, Ngoc and Maatouk, Ali and Anand, Rishabh and
               Zhang, Yifei and Chen, Jialin and Liu, Jiahong and
               Xiong, Bo and Zhou, Min and King, Irwin and
               Weber, Melanie and Ying, Rex},
  year      = {2026},
  url       = {https://hyperboliclearning.github.io}
}</pre>
</div>

<script>
function copyBib(btn) {
  var text = document.getElementById('bib-text').innerText;
  navigator.clipboard.writeText(text).then(function() {
    btn.textContent = 'Copied!';
    setTimeout(function() { btn.textContent = 'Copy'; }, 2000);
  });
}
</script>
