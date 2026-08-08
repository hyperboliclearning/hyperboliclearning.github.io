---
title: "KDD 2026 Tutorial: Hyperbolic Learning for Structured Data, Knowledge, and Memory"
layout: page
permalink: /events/kdd2026tutorial
---

<link rel="stylesheet" href="/assets/kdd2025.css">

<div class="kdd26-tutorial-lead">
<p><strong>Hyperbolic Learning for Structured Data, Knowledge, and Memory: A Tutorial</strong> will take place at <a href="https://kdd2026.kdd.org/">KDD 2026</a> on Sunday, August 9, 2026, <span class="kdd26-info-highlight">from 9:00 AM to 12:00 PM</span> in <span class="kdd26-info-highlight">Samda A at ICC Jeju</span>. The tutorial focuses on how hyperbolic geometry can support structured data organization, retrieval, knowledge interfaces, and memory layers in modern foundation-model systems.</p>
</div>

<div class="banner-container kdd26-tutorial-banner">
 <img class="kdd26-tutorial-banner-image" src="/images/kdd2026_cover_mid.jpg" alt="KDD 2026 official cover image">
 <div class="banner-overlay"></div>
 <div class="banner-text">
  Hyperbolic Learning for Structured Data, Knowledge, and Memory @KDD 2026
 </div>
</div>

<style>
body {
  background: #f1efed;
  background-image: none;
}
body::before {
  display: none;
}
.page-content > .wrapper {
  background: #ffffff;
  border: 1px solid #d8d9dc;
  border-radius: 24px;
  box-shadow: 0 16px 42px rgba(24, 33, 46, 0.08);
  overflow: hidden;
}
.post-header {
  position: relative;
  overflow: hidden;
  background: linear-gradient(175deg, #e7ebef 0%, #f2f1ef 58%, #ffffff 100%);
  border-bottom: 1px solid #d8d9dc;
  margin-bottom: 0;
}
.post-header::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 30%, rgba(84, 122, 128, 0.045) 0%, transparent 68%);
  pointer-events: none;
}
.kdd26-tutorial-lead {
  color: var(--primary, #3a5a7c);
  margin-bottom: 2rem;
  font-size: 1.02rem;
  line-height: 1.78;
}
.kdd26-tutorial-banner {
  height: auto;
  min-height: 0;
  background: #f8f6f3;
  background-image: none;
  display: block;
  width: min(100%, 840px);
  max-width: 100%;
  margin: 0 auto 1.8rem;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(24, 33, 46, 0.08);
}
.kdd26-tutorial-banner-image {
  display: block;
  width: 100%;
  height: auto;
  filter: brightness(1.05) saturate(1.05);
  box-shadow: 0 10px 26px rgba(26, 54, 43, 0.08);
}
.kdd26-tutorial-banner .banner-overlay {
  display: block;
  background: linear-gradient(
    180deg,
    rgba(8, 16, 28, 0.12) 0%,
    rgba(8, 16, 28, 0.18) 45%,
    rgba(8, 16, 28, 0.28) 100%
  );
}
.kdd26-tutorial-banner .banner-text {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: min(86%, 720px);
  transform: translate(-50%, -50%);
  margin: 0;
  padding: 0.9rem 1.15rem;
  color: #ffffff;
  font-size: 1.7rem;
  font-weight: 900;
  line-height: 1.18;
  letter-spacing: 0;
  text-align: center;
  text-shadow: 0 4px 18px rgba(0, 0, 0, 0.78);
  background: rgba(7, 13, 22, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 18px;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
}
.kdd26-info-card {
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  padding: 1rem 1.1rem;
  margin: 1rem 0 1.4rem;
}
.kdd26-info-card ul {
  margin: 0.55rem 0 0;
}
.kdd26-info-highlight {
  color: #8b1e1e;
  font-weight: 800;
}
.post-content h2 {
  color: #3a5a7c;
  font-weight: 800;
  letter-spacing: 0;
  line-height: 1.2;
  padding-top: 0.45rem;
  margin-top: 1.35rem;
  margin-bottom: 0.5rem;
  padding-bottom: 0.15rem;
  scroll-margin-top: 84px;
}
.post-content h3 {
  color: #1e2a36;
  font-weight: 760;
  letter-spacing: 0;
  margin-top: 0.95rem;
  margin-bottom: 0.3rem;
  scroll-margin-top: 84px;
}
.post-content h2:first-of-type {
  margin-top: 0.7rem;
}
.post-content p,
.post-content ul,
.post-content table {
  margin-bottom: 0.75rem;
}
.post-content li {
  line-height: 1.72;
}
@media (max-width: 640px) {
  .kdd26-tutorial-banner .banner-text {
    width: min(92%, 520px);
    padding: 0.7rem 0.85rem;
    font-size: 1.16rem;
    font-weight: 800;
    line-height: 1.3;
    border-radius: 14px;
  }
}
</style>

## Important Information

<div class="kdd26-info-card" markdown="1">

* **Tutorial title**: Hyperbolic Learning for Structured Data, Knowledge, and Memory: A Tutorial
* **Date**: Sunday, August 9, 2026
* **Time**: <span class="kdd26-info-highlight">9:00 AM - 12:00 PM (KST)</span>
* **Conference**: KDD 2026
* **Venue**: <span class="kdd26-info-highlight">Samda A, International Convention Center Jeju (ICC Jeju), Jeju, Korea</span>
* **Format**: Half-day lecture-style tutorial with interactive questions and discussion

</div>

## Tutorial Introduction

Foundation models are increasingly deployed as data-and-memory systems that combine pretrained parameters with retrieval interfaces, external knowledge stores, persistent memory, and continually updated corpora. Many KDD problems, including recommendation, search, temporal modeling, knowledge discovery, enterprise knowledge systems, and AI for science, involve long-tail, hierarchical, and relational data that are not naturally matched to purely Euclidean latent spaces.

This tutorial introduces hyperbolic learning as a practical geometric framework for structured data, knowledge, and memory layers. The focus is on when curved geometry improves data organization, retrieval interfaces, memory updates, adaptation, and deployment behavior, and how these gains should be evaluated in KDD systems.

## Tutorial Topics

The tutorial will cover:

* Hyperbolic geometry essentials, including Poincare ball and hyperboloid models, geodesic distance, exponential and logarithmic maps, and optimization in curved spaces
* Hyperbolic data layers for representation, indexing, retrieval, attention, normalization, and numerical stability
* Hyperbolic memory and agent systems, including retrieval-aware LLMs, non-parametric memory, agent memory management, model editing, and unlearning
* Multimodal, generative, and scientific data systems, including vision-language modeling, hierarchical multimodal understanding, and AI-for-science scenarios
* KDD-native applications and evaluation in recommendation, temporal and relational learning, enterprise knowledge systems, scaling strategies, and responsible deployment

## Target Audience and Prerequisites

The tutorial targets researchers, practitioners, and graduate students interested in foundation models, hyperbolic learning, geometric deep learning, and KDD applications involving structured data, knowledge, retrieval, or memory. No differential geometry background is required. Familiarity with basic machine learning, deep learning, and standard foundation-model architectures is sufficient.

## Tutors

All tutors are planned to participate in person for this tutorial.

* **Jiahong Liu (The Chinese University of Hong Kong)**: Ph.D. candidate whose research focuses on hyperbolic geometry for foundation models, recommender systems, and federated learning.
* **Menglin Yang (HKUST(GZ))**: Assistant Professor in AI Thrust at HKUST (Guangzhou). His research interests include hyperbolic geometric learning, graph representation learning, and foundation models.
* **Irwin King (The Chinese University of Hong Kong)**: Pro-Vice-Chancellor (Education) and Professor whose research spans geometric machine learning, hyperbolic representation learning, data mining, multimodal learning, personalization, recommendation, and large language models.

## Contact

For questions or updates, please contact `jiahong.liu21@gmail.com`, `menglinyang@hkust-gz.edu.cn`, or `king@cse.cuhk.edu.hk`.
