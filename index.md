---
title: "Hyperbolic and Non-Euclidean Geometric Learning in the Era of LLM"
display_date: "2026-10-06"
layout: page
permlink: /
---

<nav class="sticky-outline" aria-label="On this page">
  <p class="outline-title">On this page</p>
  <ul>
    <li><a href="#events-and-news">Events and News</a></li>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#1-hyperbolic-geometry">Hyperbolic Geometry</a></li>
    <li><a href="#2-hyperbolic-models">Hyperbolic Models</a></li>
    <li><a href="#3-hyperbolic-neural-networks">Hyperbolic Neural Networks</a></li>
    <li><a href="#4-hyperbolic-transformers">Hyperbolic Transformers</a></li>
    <li><a href="#5-hyperbolic-foundation-models">Hyperbolic Foundation Models</a></li>
    <li><a href="#6-challenges-and-opportunities">Challenges and Opportunities</a></li>
    <li><a href="#7-conclusion">Conclusion</a></li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#references">References</a></li>
  </ul>
</nav>

<style>
/* ---- Page-scoped overrides for tighter, more cohesive layout ---- */
.page-content h1 {
  text-align: center;
  margin-top: 0.2em;
  margin-bottom: 0.9em;
}
.page-content h1::before { display: none; }
.page-content h2, .page-content h3 { scroll-margin-top: 90px; }
.page-content .post-date {
  margin: 0;
  text-align: right;
  font-size: 0.82rem;
  font-weight: 400;
  color: var(--text-soft, #6b7280);
}
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
.page-content .post-content p { text-align: left; hyphens: none; }
.notation-note {
  background: var(--bg, #f7f5f2);
  border-left: 3px solid var(--primary, #3a5a7c);
  border-radius: 0 8px 8px 0;
  padding: 0.85rem 1rem;
  margin: 1.1rem 0;
  font-size: 0.92rem;
}
.notation-note p:last-child { margin-bottom: 0; }
.math-block mjx-container[display="true"] { margin: 0 !important; }
.math-block mjx-container[display="true"] + mjx-container[display="true"] { margin-top: 0.65em !important; }
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
  font-size: 1em;
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
  box-sizing: border-box;
  position: fixed;
  top: 88px;
  left: max(16px, calc((100vw - 920px) / 2 - 216px));
  width: 196px;
  max-height: calc(100vh - 112px);
  overflow-y: auto;
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  padding: 12px 8px;
  z-index: 10;
  text-align: left;
  display: none;
}
@media (min-width: 1380px) {
  .sticky-outline { display: block; }
}
.sticky-outline ul { display: block; list-style: none; padding: 0; margin: 0; border: 0; background: transparent; text-align: left; }
.sticky-outline .outline-title { margin: 0 10px 8px; color: var(--text-soft, #6b7280); font-size: 0.72rem; font-weight: 600; }
.sticky-outline > ul > li { padding: 0; margin: 0 0 2px; text-align: left; }
.sticky-outline a {
  color: var(--text-soft, #6b7280);
  text-decoration: none;
  transition: color 0.2s;
  display: block;
  padding: 6px 9px;
  border-left: 2px solid transparent;
  border-radius: 0 5px 5px 0;
  text-align: left;
  font-size: 0.8rem;
  line-height: 1.4;
  font-weight: 400;
}
.sticky-outline a:hover {
  color: var(--primary, #3a5a7c);
  background: var(--bg, #f7f5f2);
}
.sticky-outline a[aria-current="location"] {
  color: var(--primary, #3a5a7c);
  background: rgba(58, 90, 124, 0.08);
  border-left-color: var(--primary, #3a5a7c);
  font-weight: 600;
}
.sticky-outline a:focus-visible {
  outline: 2px solid var(--primary, #3a5a7c);
  outline-offset: 1px;
}

/* ---- Figures ---- */
.fig-container {
  text-align: center;
  margin: 1.2em 0;
}
.fig-container > a { cursor: zoom-in; }
.fig-container.fig-compact { max-width: 640px; margin-left: auto; margin-right: auto; }
.fig-container img {
  display: block;
  width: 100%;
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
  font-style: normal;
  line-height: 1.5;
}

/* ---- Interactive geometry plots ---- */
#geometry-interactive { scroll-margin-top: 90px; }
.geometry-charts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; padding: 16px; border: 1px solid var(--border, #e5e2dd); border-radius: 10px; text-align: left; }
.geometry-chart { min-width: 0; }
.geometry-chart .chart-title { margin: 0 0 4px; color: var(--heading, #1e2a36); font-size: 0.88rem; font-weight: 600; }
.geometry-chart svg { display: block; width: 100%; height: auto; overflow: visible; font-family: inherit; touch-action: pan-y; }
.chart-grid { stroke: #e5e8ec; stroke-width: 1; }
.chart-axis { stroke: #aeb9c5; stroke-width: 1; }
.chart-label { fill: #586575; font-size: 12px; }
.chart-curve { fill: none; stroke-width: 2.5; stroke-linecap: round; }
.chart-guide { stroke: #94a3b8; stroke-width: 1; stroke-dasharray: 4 4; }
.chart-marker { stroke: white; stroke-width: 1.5; }
.chart-hitbox { fill: transparent; cursor: crosshair; }
.chart-controls { display: flex; align-items: center; gap: 9px; margin-top: 8px; }
.chart-controls label { flex: 1; color: var(--text-soft, #6b7280); font-size: 0.78rem; white-space: nowrap; }
.chart-controls input { width: 100%; display: block; margin: 7px 0 0; accent-color: var(--primary, #3a5a7c); cursor: pointer; }
.chart-play { flex-shrink: 0; min-width: 58px; padding: 5px 9px; border: 1px solid var(--border, #e5e2dd); border-radius: 5px; background: white; color: var(--primary, #3a5a7c); font: inherit; font-size: 0.75rem; cursor: pointer; }
.chart-play:hover { background: var(--bg, #f7f5f2); border-color: var(--primary, #3a5a7c); }
.chart-play:focus-visible, .chart-controls input:focus-visible { outline: 2px solid var(--primary, #3a5a7c); outline-offset: 3px; }
.chart-values { min-height: 3.4em; margin: 8px 0 0; color: var(--text, #3d424a); font-size: 0.78rem; line-height: 1.65; font-variant-numeric: tabular-nums; }
.chart-values .hyp-value { color: #c0392b; }
.chart-values .eu-value { color: #222222; }
.chart-help { margin: 6px 0 0; color: var(--text-soft, #6b7280); font-size: 0.73rem; }
@media (max-width: 600px) {
  .geometry-charts { grid-template-columns: 1fr; gap: 20px; padding: 12px; }
}

/* ---- Model comparison: keep long descriptions readable on small screens ---- */
.model-table-wrap { overflow-x: auto; margin: 1em 0; border: 1px solid var(--border, #e5e2dd); border-radius: 8px; }
.model-table { width: 100%; min-width: 620px; margin: 0; border-collapse: collapse; font-size: 0.88rem; line-height: 1.55; }
.model-table th, .model-table td { padding: 0.75rem 0.85rem; text-align: left; vertical-align: top; border: 0; border-bottom: 1px solid var(--border, #e5e2dd); }
.model-table thead th { color: var(--heading, #1e2a36); background: var(--bg, #f7f5f2); font-weight: 600; }
.model-table tbody th { width: 18%; font-weight: 600; }
.model-table td:nth-child(3), .model-table td:nth-child(4) { white-space: nowrap; }
.model-table tbody tr:last-child th, .model-table tbody tr:last-child td { border-bottom: 0; }
.model-table a { color: var(--primary, #3a5a7c); }
.model-table a:hover { color: var(--accent, #c0603c); text-decoration: underline; }

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
MathJax = {
  tex: { inlineMath: [['$','$'], ['\\(','\\)']], displayMath: [['$$','$$'], ['\\[','\\]']] },
  chtml: { scale: 0.95, mtextInheritFont: true },
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" defer></script>
<script src="{{ '/assets/homepage-outline.js' | relative_url }}" defer></script>
<script src="{{ '/assets/geometry-charts.js' | relative_url }}" defer></script>

## Events and News!

<ul class="news-list">
  <li class="featured"><span class="news-icon" title="Survey">📄</span><a href="/survey/">October 1, 2026 · From Hyperbolic to Mixed-Curvature Geometric Learning: A Comprehensive Survey</a> <span style="font-size:0.95em">🔥</span></li>
  <li><span class="news-icon" title="Paper">📄</span><a href="https://arxiv.org/pdf/2602.07739">ICML 2026 · HypRAG: Hyperbolic Dense Retrieval for Retrieval Augmented Generation (PDF)</a></li>
  <li><span class="news-icon" title="GitHub"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#24292f"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></span><a href="https://github.com/graph-and-geometric-learning/helm">NeurIPS 2025 HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts - GitHub</a></li>
  <li><span class="news-icon" title="Project page">📝</span><a href="{{ "/work/hyplora" | relative_url }}">NeurIPS 2025 Hyperbolic Fine-tuning for Large Language Models (HypLoRA)</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="{{ "/events/kdd2026tutorial" | relative_url }}">KDD 2026 Hyperbolic Learning Tutorial</a></li>
  <li><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/kdd2026workshop" | relative_url }}">KDD 2026 Geometric Learning Workshop</a></li>
  <li><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/neurips2025negelworkshop" | relative_url }}">NeurIPS 2025 NEGEL Workshop</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="{{ "/events/aaai2026tutorial" | relative_url }}">AAAI 2026 Hyperbolic FM Tutorial</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="{{ "/events/kdd2025tutorial" | relative_url }}">KDD 2025 Hyperbolic FM Tutorial</a></li>
  <li><span class="news-icon" title="Workshop">🎤</span><a href="{{ "/events/www2025workshop" | relative_url }}">WWW 2025 NEGEL Workshop</a></li>
  <li><span class="news-icon" title="Tutorial">🎓</span><a href="https://hyperbolicgnn.github.io/">KDD 2023 Tutorial</a></li>
  <li><span class="news-icon" title="Slack"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path fill="#E01E5A" d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313z"/><path fill="#36C5F0" d="M8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312z"/><path fill="#2EB67D" d="M18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312z"/><path fill="#ECB22E" d="M15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg></span><a href="https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA">Slack channel for more discussions and tracking updates!</a></li>
  <li><span class="news-icon" title="Repository">⭐</span><a href="{{ "/collection" | relative_url }}">Awesome Hyperbolic Representation and Deep Learning Repository</a></li>
</ul>

## Introduction

The geometry of a representation space determines how a model expresses similarity, hierarchy, and relationships. Euclidean vectors are a useful default, but their geometry may not match the structure we want to preserve. Hyperbolic space provides room for branching hierarchies; spherical space offers a compact setting for directional representations; mixed-curvature spaces combine several geometries when the data contain different kinds of structure.

In the era of large language models, these choices matter at several stages: learning token representations, building attention layers, adapting pretrained models, and organizing external knowledge for retrieval. Hyperbolic learning is one way to introduce a structural inductive bias. Its value depends on the data, the learning objective, and the computational budget, so comparisons with strong Euclidean baselines remain essential.

This page connects the geometry to the operations used in neural networks, Transformers, and foundation models. For a broader treatment of spherical and mixed-curvature learning, see our [survey]({{ "/survey/" | relative_url }}); the [paper collection]({{ "/collection" | relative_url }}) organizes research by methods, applications, and task settings.

<figure class="fig-container">
  <a href="{{ '/survey/geometry.png' | relative_url }}"><img src="{{ '/survey/geometry.png' | relative_url }}" width="4724" height="1275" alt="Geodesic triangles in hyperbolic, Euclidean, and spherical geometry, followed by a product of the three spaces." loading="lazy" decoding="async"></a>
  <figcaption class="fig-cap"><strong>Figure 1 · Choosing a geometry.</strong> Triangle angles sum to less than, equal to, or greater than $\pi$ in negative, zero, or positive constant curvature, respectively. A product space represents different geometric components together. The signed-curvature symbol $c$ in the figure corresponds to $\kappa$ below. For more details, please check the <a href="{{ '/survey/' | relative_url }}">survey</a>.</figcaption>
</figure>

## 1. Hyperbolic Geometry

Hyperbolic space is a complete, simply connected space of constant negative sectional curvature. Its shortest paths, called geodesics, generalize straight lines. Unlike Euclidean space, its available volume grows exponentially with geodesic radius, making it a useful setting for representing branching structure.

<div class="notation-note" markdown="1">
**Notation used below.** $\kappa$ denotes signed sectional curvature, with $\kappa<0$ for hyperbolic space. $\lVert\cdot\rVert$ is the Euclidean norm, and $g^E=I_n$ is the Euclidean metric. Formulas for a unit Poincaré ball use $\kappa=-1$; other negative curvatures change the coordinate radius and distance scale.
</div>

### 1.1 Key Properties of Hyperbolic Space

**Exponential area growth.** In the hyperbolic plane, the area of a geodesic disk of radius $r$ is

<div class="math-block">
$$A_\kappa(r)=\frac{2\pi}{-\kappa}\left[\cosh\!\left(\sqrt{-\kappa}\,r\right)-1\right].$$
</div>

For $\kappa=-1$, this grows exponentially for large $r$, while a Euclidean disk has area $\pi r^2$. The comparison concerns geodesic radius, rather than the apparent radius in a drawing. Higher-dimensional hyperbolic spaces also exhibit exponential volume growth.

**Triangle angle deficit.** For a geodesic triangle in constant curvature $\kappa<0$, with angles $\alpha,\beta,\gamma$, the area is $(\pi-\alpha-\beta-\gamma)/(-\kappa)$. The angle sum is smaller than $\pi$, as illustrated in Figure 1.

**An infinite space inside bounded coordinates.** In the unit Poincaré ball, a point with coordinate norm $\rho=\lVert\mathbf{x}\rVert<1$ has radial distance

<div class="math-block">
$$d_{\mathbb{B}}(\mathbf{0},\mathbf{x})=2\operatorname{artanh}(\rho)=\log\!\frac{1+\rho}{1-\rho}.$$
</div>

Every interior point is at a finite distance from the origin. The distance tends to infinity only as $\rho\to1$. Small coordinate differences near the boundary can therefore correspond to large geometric distances. These formulas follow the standard [Poincaré model](https://arxiv.org/abs/1805.09112).

<figure class="fig-container" id="geometry-interactive">
  <div class="geometry-charts">
    <div class="geometry-chart" data-geometry-chart="area">
      <p class="chart-title">More room for branching structure</p>
      <svg viewBox="0 0 480 300" role="img" aria-label="Hyperbolic and Euclidean disk area as a function of geodesic radius"></svg>
      <div class="chart-controls"><label>Geodesic radius r: <output class="chart-coordinate">3.00</output><input type="range" min="0" max="5" step="0.01" value="3" aria-label="Geodesic radius for disk area"></label><button class="chart-play" type="button" aria-label="Animate disk area" aria-pressed="false">Play</button></div>
      <div class="chart-values"><span class="hyp-value">Hyperbolic disk area: <output data-value="hyperbolic"></output></span><br><span class="eu-value">Euclidean disk area: <output data-value="euclidean"></output></span></div>
    </div>
    <div class="geometry-chart" data-geometry-chart="distance">
      <p class="chart-title">A finite disk represents infinite distance</p>
      <svg viewBox="0 0 480 300" role="img" aria-label="Hyperbolic and Euclidean distances from the origin at the same coordinate norm; hyperbolic distance grows without bound near the unit boundary"></svg>
      <div class="chart-controls"><label>Poincaré norm ρ: <output class="chart-coordinate">0.800</output><input type="range" min="0" max="0.999" step="0.001" value="0.8" aria-label="Poincaré coordinate norm for distance"></label><button class="chart-play" type="button" aria-label="Animate distance from the origin" aria-pressed="false">Play</button></div>
      <div class="chart-values"><span class="hyp-value">Hyperbolic distance: <output data-value="distance"></output></span><br><span class="eu-value">Euclidean distance: <output data-value="euclidean-distance"></output></span></div>
      <p class="chart-help">The boundary ρ = 1 is excluded; hyperbolic distance tends to infinity.</p>
    </div>
  </div>
  <p class="chart-help">Hover over a plot, drag the slider, or press Play to explore. Sliders also support arrow keys.</p>
  <noscript><img src="{{ '/images/figs/hyperbolic-area-and-distance.svg' | relative_url }}" width="1160" height="425" alt="Static plots of disk area and distance from the origin."></noscript>
  <figcaption class="fig-cap"><strong>Figure 2 · Geometry behind the intuition.</strong> Left: disk areas at the same geodesic radius. Right: hyperbolic and Euclidean distances from the origin at the same coordinate norm $\rho$, with Euclidean distance $d_E(0,\mathbf{x})=\rho$. Red denotes hyperbolic geometry; black denotes Euclidean geometry. Hyperbolic values follow the equations above at $\kappa=-1$; these are mathematical curves, rather than experimental results.</figcaption>
</figure>

### 1.2 Why Hyperbolic Geometry for AI?

A regular tree with branching factor $b>1$ has $b^d$ nodes at depth $d$. Hyperbolic volume growth offers a geometric way to accommodate that expansion. Learned embeddings can place general concepts closer to a chosen origin and more specific concepts farther out, while using directions to separate branches. This arrangement must be encouraged by the data and objective; curvature alone does not assign semantic meaning to radius.

Taxonomies, knowledge graphs, and some language or visual representations provide useful test cases. [Poincaré embeddings](https://arxiv.org/abs/1705.08039) showed that low-dimensional hyperbolic representations can perform well on hierarchical data. A power-law degree distribution or a small measured graph hyperbolicity can motivate an experiment, but neither establishes that hyperbolic geometry will outperform Euclidean geometry on every downstream task.

## 2. Hyperbolic Models

The Poincaré ball, Lorentz hyperboloid, Klein ball, and upper half-space describe the same hyperbolic geometry at a fixed curvature. Their coordinates and computational operations differ. Choosing a model changes how the space is represented, rather than its intrinsic distances.

### 2.1 Poincaré Ball Model

For signed curvature $\kappa<0$, the coordinate domain and metric are

<div class="math-block">
$$\mathbb{B}_\kappa^n=\left\{\mathbf{x}\in\mathbb{R}^n:\lVert\mathbf{x}\rVert<\frac{1}{\sqrt{-\kappa}}\right\},\qquad g_{\mathbf{x}}^{\mathbb{B}}=\left(\frac{2}{1+\kappa\lVert\mathbf{x}\rVert^2}\right)^2g^E.$$
</div>

The metric is conformal: angles between tangent vectors agree with their Euclidean-coordinate angles. In two dimensions, geodesics are diameters or circular arcs orthogonal to the boundary. The distance between two points is

<div class="math-block">
$$d_{\mathbb{B},\kappa}(\mathbf{x},\mathbf{y})=\frac{1}{\sqrt{-\kappa}}\operatorname{arcosh}\!\left(1-\frac{2\kappa\lVert\mathbf{x}-\mathbf{y}\rVert^2}{(1+\kappa\lVert\mathbf{x}\rVert^2)(1+\kappa\lVert\mathbf{y}\rVert^2)}\right).$$
</div>

At $\kappa=-1$, the radius is one and the metric reduces to $\left(2/(1-\lVert\mathbf{x}\rVert^2)\right)^2g^E$. The bounded picture is convenient for visualization, but computations near its boundary require care.

### 2.2 Lorentz (Hyperboloid) Model

For $\mathbf{x},\mathbf{y}\in\mathbb{R}^{n+1}$, define the Lorentz inner product by $\langle\mathbf{x},\mathbf{y}\rangle_{\mathcal{L}}=-x_0y_0+\sum_{i=1}^n x_iy_i$. The hyperbolic space is the upper sheet

<div class="math-block">
$$\mathbb{H}_\kappa^n=\left\{\mathbf{x}\in\mathbb{R}^{n+1}:\langle\mathbf{x},\mathbf{x}\rangle_{\mathcal{L}}=\frac{1}{\kappa},\quad x_0>0\right\}.$$
</div>

The ambient inner product is indefinite, but its restriction to a tangent space gives a positive-definite Riemannian metric. The geodesic distance is

<div class="math-block">
$$d_{\mathbb{H},\kappa}(\mathbf{x},\mathbf{y})=\frac{1}{\sqrt{-\kappa}}\operatorname{arcosh}\!\left(\kappa\langle\mathbf{x},\mathbf{y}\rangle_{\mathcal{L}}\right).$$
</div>

For the same point, the argument of $\operatorname{arcosh}$ is one and the distance is zero. At $\kappa=-1$, the formulas become $\langle\mathbf{x},\mathbf{x}\rangle_{\mathcal{L}}=-1$ and $d=\operatorname{arcosh}(-\langle\mathbf{x},\mathbf{y}\rangle_{\mathcal{L}})$, matching the [Lorentz embedding formulation](https://arxiv.org/abs/1806.03417). Lorentz coordinates support efficient geometric operations, but large coordinates can still cause cancellation and precision problems.

### 2.3 Klein Model

The Klein model uses a ball of radius $1/\sqrt{-\kappa}$ in which geodesics appear as straight chords. It is useful for geometric constructions and some aggregation rules. Unlike the Poincaré ball, it does not preserve angles in its coordinate drawing.

### 2.4 Poincaré Half-Plane Model

The two-dimensional half-plane generalizes to the upper half-space $\mathbb{U}^n=\{\mathbf{x}\in\mathbb{R}^n:x_n>0\}$. For curvature $\kappa<0$, its metric is $g_{\mathbf{x}}^{\mathbb{U}}=g^E/(-\kappa x_n^2)$. Geodesics are vertical lines or circle arcs meeting the boundary orthogonally. At $\kappa=-1$, this is the familiar metric $g^E/x_n^2$.

### 2.5 Inter-Model Mappings

At unit curvature $\kappa=-1$, a Lorentz point $\mathbf{X}=(X_0,\mathbf{X}_s)$ maps to the Poincaré point $\mathbf{u}=\mathbf{X}_s/(X_0+1)$. The inverse map is

<div class="math-block">
$$\mathbf{X}=\left(\frac{1+\lVert\mathbf{u}\rVert^2}{1-\lVert\mathbf{u}\rVert^2},\frac{2\mathbf{u}}{1-\lVert\mathbf{u}\rVert^2}\right).$$
</div>

These maps preserve intrinsic distances. One can compute in Lorentz coordinates and visualize the same points in the Poincaré ball. Neither coordinate model is universally more numerically stable; the operation, precision, and distance range matter. See the [numerical stability analysis](https://arxiv.org/abs/2211.00181).

<figure class="fig-container fig-compact">
  <a href="{{ '/images/figs/model-projections.svg' | relative_url }}"><img src="{{ '/images/figs/model-projections.svg' | relative_url }}" width="1080" height="594" alt="Two-dimensional cross-sections: rays from S map a Lorentz hyperboloid point X into the open Poincaré ball, while stereographic projection maps the sphere minus its south pole onto the entire plane." loading="lazy" decoding="async"></a>
  <figcaption class="fig-cap"><strong>Figure 3 · From manifold points to coordinates.</strong> Cross-sections of the projections at unit curvature. Left: the upper hyperboloid maps inside the Poincaré ball. Right: the sphere, excluding its south pole, maps to an unbounded plane. Blue points $X$ project to green coordinates $u$ along rays from $S$; higher-dimensional models use the same construction. Click to enlarge. For more details, please check the <a href="{{ '/survey/' | relative_url }}">survey</a>.</figcaption>
</figure>

## 3. Hyperbolic Neural Networks

Once representations live on a manifold, layers must respect its geometry. A practical design specifies where features live, how transformations and aggregation act, and how outputs remain valid points. Euclidean parameters can still be used to construct manifold-valued representations.

### 3.1 Hyperbolic Embeddings

An embedding assigns each entity a point and trains distances or similarity scores to reflect the desired relationships. [Poincaré embeddings](https://arxiv.org/abs/1705.08039) established this approach for hierarchies; [Lorentz embeddings](https://arxiv.org/abs/1806.03417) offered an alternative coordinate system for optimization. Low dimensionality and a meaningful radial organization are possible outcomes of training, rather than properties guaranteed for every dataset.

### 3.2 Hyperbolic Neural Layers

**Tangent-space layers** use $\log_{\mathbf{p}}$ to map a manifold point to a vector at a reference point $\mathbf{p}$, apply a Euclidean operation, then return with $\exp_{\mathbf{p}}$. These maps are exact on hyperbolic space; the resulting Euclidean operation is a design choice and does not automatically preserve hyperbolic distances.

**Möbius layers** define ball operations that keep outputs in the domain. A bias-free transformation can be written as $\mathbf{M}\otimes_\kappa\mathbf{x}=\exp_{\mathbf{0}}^\kappa(\mathbf{M}\log_{\mathbf{0}}^\kappa(\mathbf{x}))$, followed by a Möbius bias addition. This connects gyrovector operations to neural layers in [Hyperbolic Neural Networks](https://arxiv.org/abs/1805.09112).

**Direct Lorentz layers** construct a valid hyperboloid point from learned spatial coordinates. For example, spatial output $\mathbf{z}$ can be completed with time coordinate $x_0=\sqrt{\lVert\mathbf{z}\rVert^2-1/\kappa}$. This enforces the manifold constraint, although it does not by itself make the layer distance-preserving.

<figure class="fig-container fig-compact">
  <a href="{{ '/images/figs/survey-manifold-operations.png' | relative_url }}"><img src="{{ '/images/figs/survey-manifold-operations.png' | relative_url }}" width="1055" height="325" alt="Exponential and logarithmic maps between a manifold and its tangent space, and parallel transport of tangent vectors along a geodesic." loading="lazy" decoding="async"></a>
  <figcaption class="fig-cap"><strong>Figure 4 · The operations behind geometric layers.</strong> The exponential map follows a geodesic from a tangent vector to a manifold point; the logarithmic map reverses that construction. Parallel transport moves a tangent vector between tangent spaces while preserving its norm. For more details, please check the <a href="{{ '/survey/' | relative_url }}">survey</a>.</figcaption>
</figure>

### 3.3 Key Architectures

- **[HNN](https://arxiv.org/abs/1805.09112) and [HNN++](https://arxiv.org/abs/2006.08210):** building blocks for hyperbolic feed-forward, recurrent, and attention-based networks.
- **[HGCN](https://arxiv.org/abs/1910.12933) and [HGNN](https://arxiv.org/abs/1910.12892):** geometric feature transformations and neighborhood aggregation for graphs.
- **[Fully Hyperbolic Neural Networks](https://arxiv.org/abs/2105.14686):** Lorentz-valued layers and attention without repeatedly using a common tangent space.
- **[$\kappa$-GCN](https://arxiv.org/abs/1911.05076):** graph learning in a shared stereographic formulation spanning negative, zero, and positive curvature.

### 3.4 Hyperbolic Activation Functions

A common activation applies $\sigma$ to tangent coordinates and maps the result back: $\sigma_{\mathcal{M}}(\mathbf{x})=\exp_{\mathbf{p}}(\sigma(\log_{\mathbf{p}}(\mathbf{x})))$. Other constructions act on Lorentz spatial coordinates and rebuild the time coordinate. Applying an ordinary coordinate-wise activation directly to a manifold point generally fails to preserve its constraint.

### 3.5 Optimization in Hyperbolic Space

For a parameter $\mathbf{x}$ constrained to the manifold, the Riemannian gradient belongs to its tangent space. A Riemannian SGD step is

<div class="math-block">
$$\mathbf{x}_{t+1}=\exp_{\mathbf{x}_t}\!\left(-\eta_t\operatorname{grad}f(\mathbf{x}_t)\right).$$
</div>

Here $\eta_t>0$ is the learning rate. Implementations may use a suitable retraction instead of the exponential map. In the Poincaré model, the Riemannian gradient is $(\lambda_{\mathbf{x}}^\kappa)^{-2}\nabla f(\mathbf{x})$, where $\lambda_{\mathbf{x}}^\kappa=2/(1+\kappa\lVert\mathbf{x}\rVert^2)$. Adaptive methods must also account for tangent-space geometry; see [Riemannian Adaptive Optimization Methods](https://arxiv.org/abs/1810.00760).

## 4. Hyperbolic Transformers

A Transformer combines projections, attention, value aggregation, residual connections, normalization, and position information. A hyperbolic version must define each component consistently. Mapping an ordinary Transformer's output embeddings to a manifold is useful, but it is a different architectural choice from performing its internal layers in hyperbolic space.

### 4.1 Hyperbolic Attention Mechanisms

Standard attention produces an output $\operatorname{softmax}(\mathbf{Q}\mathbf{K}^{\mathsf{T}}/\sqrt{d_k})\mathbf{V}$. In a distance-based geometric variant, queries and keys are manifold points and the attention weights can be

<div class="math-block">
$$\alpha_{ij}=\frac{\exp\!\left[-\beta d_{\mathbb{H},\kappa}(\mathbf{q}_i,\mathbf{k}_j)^2\right]}{\sum_{\ell=1}^{N}\exp\!\left[-\beta d_{\mathbb{H},\kappa}(\mathbf{q}_i,\mathbf{k}_\ell)^2\right]},\qquad\beta>0.$$
</div>

The denominator normalizes over keys for a fixed query; $\beta$ is an inverse temperature. A complete layer must also specify how the values are combined. An ordinary weighted coordinate sum generally leaves the manifold, so geometric means, normalized Lorentz centroids, or tangent-space aggregation are used. This distinction appears explicitly in [fully hyperbolic attention](https://arxiv.org/abs/2105.14686).

Geodesic proximity depends on both radius and direction. Two tokens at the same radius can belong to different branches and be far apart; radial depth alone does not determine attention. Other designs use Lorentz inner products or tangent-space dot products, and efficient variants need not compute every pairwise distance.

### 4.2 Multi-Resolution Processing

When the objective learns a hierarchy, radius can encode depth and direction can distinguish branches. Attention can then connect general and specific representations. Such a structure must be measured in the trained embeddings; operating in hyperbolic space does not automatically provide a multi-resolution decomposition.

### 4.3 Hyperbolic Position Encodings

Sequence position and semantic hierarchy serve different roles. Positional mechanisms must respect the chosen geometric operations while retaining useful relative-position information. [HELM](https://arxiv.org/abs/2505.24722) develops hyperbolic rotary positional encoding, along with geometry-aware normalization, for this purpose.

### 4.4 Notable Hyperbolic Transformer Models

The names below follow the papers. Model names link to the papers, and venues link to their publication records. Years refer to conference publication rather than the first preprint.

<div class="model-table-wrap" role="region" aria-label="Hyperbolic Transformer model comparison" tabindex="0">
<table class="model-table">
  <thead><tr><th scope="col">Name used in the paper</th><th scope="col">Key characteristics</th><th scope="col">Venue</th><th scope="col">Year</th></tr></thead>
  <tbody>
    <tr><th scope="row"><a href="https://arxiv.org/abs/2505.24722">HELM-MiCE</a></th><td>Mixture-of-Curvature Experts with distinct learned negative curvatures; hyperbolic Multi-Head Latent Attention reduces the KV cache. Shares HELM's positional and normalization modules.</td><td><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/d1e2f808a51842eedaf6ef0099d716c6-Abstract-Conference.html">NeurIPS</a></td><td>2025</td></tr>
    <tr><th scope="row"><a href="https://arxiv.org/abs/2505.24722">HELM-D</a></th><td>Dense, fully hyperbolic decoder-only language model with hyperbolic rotary positions and RMS normalization; pretrained at billion-parameter scale.</td><td><a href="https://proceedings.neurips.cc/paper_files/paper/2025/hash/d1e2f808a51842eedaf6ef0099d716c6-Abstract-Conference.html">NeurIPS</a></td><td>2025</td></tr>
    <tr><th scope="row"><a href="https://arxiv.org/abs/2407.01290">Hypformer</a></th><td>Lorentz-space Transformer blocks for projections, normalization, activation, and dropout; linear self-attention supports large graphs and long sequences.</td><td><a href="https://doi.org/10.1145/3637528.3672039">KDD</a></td><td>2024</td></tr>
    <tr><th scope="row"><a href="https://arxiv.org/abs/2105.14686">HyboNet</a></th><td>Direct Lorentz linear layers and attention using geometric centroids. The framework includes a fully hyperbolic Transformer evaluated on machine translation and syntax probing.</td><td><a href="https://aclanthology.org/2022.acl-long.389/">ACL</a></td><td>2022</td></tr>
    <tr><th scope="row"><a href="https://arxiv.org/abs/1805.09786">Hyperbolic Attention Networks</a></th><td>Hyperbolic attention weights and geometric value aggregation; other Transformer blocks remain Euclidean. An early approach evaluated on translation, graphs, and visual question answering.</td><td><a href="https://iclr.cc/virtual/2019/poster/805">ICLR</a></td><td>2019</td></tr>
  </tbody>
</table>
</div>

[Mixed-curvature product embeddings](https://openreview.net/forum?id=HJxeWnCcF7) provide a related geometric foundation. They combine model spaces, but are not themselves a Transformer architecture.

## 5. Hyperbolic Foundation Models

Geometry can enter a foundation-model pipeline through pretraining, parameter-efficient adaptation, embedding heads, or external retrieval. These routes change different components and should be evaluated accordingly. A geometric retrieval head, for example, does not make the underlying language model fully hyperbolic.

### 5.1 Hyperbolic Large Language Models

**[HypLoRA]({{ "/work/hyplora/" | relative_url }})** applies low-rank adaptation in hyperbolic space. Its [paper](https://arxiv.org/abs/2410.04010) studies token geometry and reports improvements on arithmetic and commonsense reasoning benchmarks. This provides evidence for a particular adaptation method and experimental setting, rather than a guarantee for every language task.

**[HELM](https://arxiv.org/abs/2505.24722)** studies fully hyperbolic pretraining at billion-parameter scale. Its dense model and Mixture-of-Curvature Experts variant use hyperbolic operations throughout the architecture. The experts in HELM-MiCE learn different negative curvatures; this should not be described as a mixture of hyperbolic, Euclidean, and spherical experts.

**Geometric retrieval and memory** apply structured representations outside the parameterized model. Their evaluation should separate retrieval quality, generated-answer quality, update behavior, and computational cost.

### 5.2 Hyperbolic Vision Foundation Models

**[Hyperbolic Image Embeddings](https://arxiv.org/abs/1904.02239)** explores visual representations in curved space. **[Hyperbolic Vision Transformers](https://arxiv.org/abs/2203.10833)** uses a vision Transformer encoder whose output embeddings are mapped to hyperbolic space for metric learning; it does not establish that every internal attention or positional operation is hyperbolic.

**[MERU](https://arxiv.org/abs/2304.09172)** learns image-text representations in a shared hyperbolic space. It is a concrete example of geometric multimodal representation learning, rather than a claim that standard CLIP already uses hyperbolic geometry.

### 5.3 Hyperbolic Multi-Modal Models

Image and text representations can be aligned through a shared geometric space and an appropriate learning objective. Hierarchical entailment constraints can distinguish a general description from a more specific image or phrase. This goes beyond making paired representations close: it asks the geometry to encode relationships between levels of specificity, as explored in [MERU](https://arxiv.org/abs/2304.09172).

Where modalities contain heterogeneous structure, a product of hyperbolic, Euclidean, and spherical factors is another option. The choice of factors, dimensions, and curvature remains part of the model design and must be validated.

### 5.4 Key Advantages

The main opportunity is to represent a task's structure with an appropriate geometric bias. Potential benefits include lower-dimensional hierarchical embeddings, explicit relations between general and specific concepts, and better retrieval or adaptation on suitable data. These benefits are conditional: fewer embedding dimensions do not automatically imply lower end-to-end latency, stronger reasoning, or better scaling. Performance and cost should be measured together.

## 6. Challenges and Opportunities

**Numerical precision.** Boundary effects in ball coordinates and cancellation in large Lorentz coordinates can both cause errors. Stable formulas, controlled radii, and suitable precision are necessary. Geometry-sensitive operations may need higher precision even when the rest of a network uses mixed precision. The [numerical stability study](https://arxiv.org/abs/2211.00181) explains why neither model is a universal solution.

**Optimization and curvature.** Gradient scaling, initialization, transport, and manifold constraints affect training. Learnable curvature adds flexibility, but can interact with representation scale and numerical conditioning. Parameters living in Euclidean space and points constrained to a manifold also need different optimization treatment.

**Scaling and integration.** Billion-parameter hyperbolic language models have already been explored in [HELM](https://arxiv.org/abs/2505.24722). Open questions include reliable training at larger scales, efficient kernels, KV-cache behavior, and comparisons at matched compute. Selective geometric adapters or retrieval modules offer another practical route.

**Evaluation.** Match parameter counts, training data, optimization effort, and compute budgets when possible. Report task performance alongside numerical failures, distortion, retrieval behavior, memory usage, and latency. Ablations should distinguish the effect of curvature from the effect of a changed architecture or objective.

**Broader geometric structure.** Product spaces allow heterogeneous relationships to be represented together. With a standard Riemannian product metric, the product space and its squared distance are

<div class="math-block">
$$\mathcal{M}=\mathcal{M}_1\times\cdots\times\mathcal{M}_m,$$
$$d_{\mathcal{M}}(\mathbf{x},\mathbf{y})^2=\sum_{j=1}^{m}d_{\mathcal{M}_j}(\mathbf{x}_j,\mathbf{y}_j)^2.$$
</div>

Choosing suitable factors and testing whether their structure is useful remain central questions for [mixed-curvature learning](https://openreview.net/forum?id=HJxeWnCcF7).

## 7. Conclusion

Hyperbolic and non-Euclidean learning make representation geometry an explicit design choice. The key is to connect a geometric property to a modeling need, define the corresponding operations correctly, and test the resulting system against appropriate alternatives. Hierarchical embeddings, geometric Transformers, adaptation, and retrieval provide concrete settings in which to make that connection.

Continue with the [survey]({{ "/survey/" | relative_url }}) for mathematical foundations and a broader research overview, the [collection]({{ "/collection" | relative_url }}) for papers organized by topic, or the [events page]({{ "/events/" | relative_url }}) for tutorials and workshops.



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
  <li>Mishne, G., Wan, Z., Wang, Y., & Yang, S. (2023). <em>The Numerical Stability of Hyperbolic Representation Learning.</em> ICML. <a href="https://arxiv.org/abs/2211.00181">arXiv:2211.00181</a></li>
</ol>
