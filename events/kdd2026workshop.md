---
title: "KDD 2026 Workshop: Geometric Space, Architecture and Learning Objective for Large Pre-Trained Models"
layout: page
permalink: /events/kdd2026workshop
---

<link rel="stylesheet" href="/assets/neurips2025.css">

<div class="kdd26-lead">
<p><strong>The Geometric Space, Architecture and Learning Objective for Large Pre-Trained Models (GALOP) workshop at <a href="https://kdd2026.kdd.org/">KDD 2026</a></strong> brings together researchers working on geometric representation spaces, geometry-aware architectures, and learning objectives for large pre-trained models, spanning natural language processing, computer vision, graph learning, knowledge discovery, and scientific AI.</p>
</div>


<div class="banner-container kdd26-banner">
 <img class="kdd26-banner-image" src="/images/kdd2026_cover_mid.jpg" alt="KDD 2026 official cover image">
 <div class="banner-overlay"></div>
 <div class="banner-text">
  Geometric Space, Architecture and Learning Objective for Large Pre-Trained Models @KDD 2026
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
.kdd26-lead {
  color: var(--primary, #3a5a7c);
  margin-bottom: 2rem;
  font-size: 1.02rem;
  line-height: 1.78;
}
.kdd26-banner {
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
.kdd26-banner-image {
  display: block;
  width: 100%;
  height: auto;
  filter: brightness(0.58) saturate(0.9);
  box-shadow: 0 10px 26px rgba(26, 54, 43, 0.08);
}
.kdd26-banner .banner-overlay {
  display: block;
  background: linear-gradient(
    180deg,
    rgba(8, 16, 28, 0.42) 0%,
    rgba(8, 16, 28, 0.54) 45%,
    rgba(8, 16, 28, 0.7) 100%
  );
}
.kdd26-banner .banner-text {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: min(86%, 700px);
  transform: translate(-50%, -50%);
  margin: 0;
  padding: 0.9rem 1.15rem;
  color: #ffffff;
  font-size: 1.72rem;
  font-weight: 900;
  line-height: 1.16;
  letter-spacing: -0.02em;
  text-align: center;
  text-shadow: 0 4px 18px rgba(0, 0, 0, 0.78);
  background: rgba(7, 13, 22, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 18px;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
}
.kdd26-card,
.kdd26-people-table td {
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}
.kdd26-card {
  padding: 1rem 1.1rem;
}
.kdd26-card h3,
.kdd26-people-table h3 {
  margin: 0 0 0.5rem;
  color: var(--heading, #1e2a36);
}
.kdd26-card p,
.kdd26-card li {
  color: var(--text, #3d424a);
}
.kdd26-card ul {
  margin: 0.6rem 0 0;
}
.post-content h2 {
  color: #3a5a7c;
  font-weight: 800;
  letter-spacing: -0.02em;
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
  letter-spacing: -0.01em;
  margin-top: 0.95rem;
  margin-bottom: 0.3rem;
  scroll-margin-top: 84px;
}
.post-content h2:first-of-type {
  margin-top: 0.7rem;
}
.post-content h2 + p,
.post-content h2 + ul,
.post-content h3 + p,
.post-content h3 + ul {
  margin-top: 0.1rem;
}
.post-content p,
.post-content ul,
.post-content table {
  margin-bottom: 0.75rem;
}
.post-content li {
  line-height: 1.72;
}
.kdd26-people-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 16px;
  margin: 1rem 0 2rem;
}
.kdd26-people-table td {
  width: 25%;
  padding: 1rem;
  text-align: center;
  vertical-align: top;
}
.kdd26-people-table img {
  width: 170px;
  height: 170px;
  object-fit: cover;
  border-radius: 14px;
  display: block;
  margin: 0 auto 0.85rem;
  background: #eef2f7;
}
.kdd26-btn {
  display: inline-block;
  background: #447588;
  color: #ffffff !important;
  padding: 0.85rem 2.15rem;
  font-size: 1rem;
  font-weight: 800;
  text-decoration: none !important;
  border: 2px solid #1e2a36;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.08);
  transition: background 0.2s, box-shadow 0.2s;
  letter-spacing: 0.01em;
}
.kdd26-btn:hover {
  background: #3a6478;
  box-shadow: 0 6px 14px rgba(0,0,0,0.12);
  color: #ffffff !important;
}
@media (max-width: 640px) {
  .kdd26-banner .banner-text {
    width: min(92%, 520px);
    padding: 0.7rem 0.85rem;
    font-size: 1.26rem;
    font-weight: 800;
    line-height: 1.3;
    border-radius: 14px;
  }
  .kdd26-people-table,
  .kdd26-people-table tbody,
  .kdd26-people-table tr,
  .kdd26-people-table td {
    display: block;
    width: 100%;
  }
}
</style>

## News

- 2026-03-22: Call for paper, [Submission website](https://openreview.net/group?id=KDD.org/2026/Workshop/GALOP)
- 2026-03-11: The workshop proposal was accepted by KDD 2026 as a half day workshop.

## Introduction

Foundation models now drive progress across language, vision, graphs, recommendation, and scientific discovery, yet most of them are still built around Euclidean representations and objectives. In many real world settings, however, the underlying data contain hierarchy, relational structure, multi scale organization, or nonuniform geometry that is not naturally captured by standard design choices.

This workshop focuses on how geometric spaces, geometric neural networks, and geometric objectives can improve foundation models by introducing more appropriate inductive bias for representation, reasoning, and adaptation. It highlights work on hyperbolic, spherical, mixed curvature, and other geometry aware approaches that can better align model structure with the structure of data.

The goal is to bring together researchers from machine learning, data mining, natural language processing, computer vision, graph learning, knowledge discovery, and scientific AI. By connecting theory, methods, systems, and applications, the workshop aims to create a shared forum for understanding when geometric modeling matters, how it should be integrated into large models, and how its benefits should be evaluated in practice.

### Important Dates

Time: 11:59 PM Anywhere on Earth unless otherwise specified.

- <span style="color: red;"><strong>Workshop paper submission: April 30, 2026</strong></span>
- Workshop paper notification: June 4, 2026
- Camera ready: June 15, 2026
- Final workshop program, materials, and full website online: June 22, 2026
- Workshop date: TBA
- Conference dates: August 9 to 13, 2026
- Venue: Jeju, Korea

## Topics of Interest

We welcome submissions on topics including, but not limited to, the following directions from the proposal:

- Hyperbolic, spherical, and mixed curvature embeddings for large pre-trained models
- Non Euclidean word, sentence, document, and multimodal representations
- Geometric transformers and manifold aware attention mechanisms
- Equivariant and invariant architectures for foundation models
- Metric learning and contrastive objectives with geometric constraints
- Curvature aware optimization on Riemannian manifolds
- Alignment and fusion across different geometric spaces
- Theory for geometric large pre-trained models, including expressiveness and generalization
- Applications in natural language processing, computer vision, graph learning, knowledge discovery, and scientific discovery
- Benchmarks, evaluation protocols, open source tools, visualization, and reproducibility resources

## Submission

- We welcome short research papers of up to 4 pages and full research papers of up to 9 pages, excluding references and supplementary materials.
- All accepted papers are planned to be presented as posters.
- Approximately 4 papers will be selected for oral presentations and 2 papers for outstanding paper awards.
- The workshop follows the current KDD 2026 workshop policy and is planned as an in person event.

<p style="text-align: center;"><a class="kdd26-btn" href="https://openreview.net/group?id=KDD.org/2026/Workshop/GALOP">GALOP Workshop @ KDD 2026 Submission</a></p>

## Tentative Program

The accepted workshop is half day. Based on the proposal, the program will include the following components:

- Opening remarks and workshop overview
- Invited talks on geometric learning and large pre-trained models
- Contributed paper spotlight presentations
- Poster and discussion session
- Panel discussion on the future of geometric AI
- Best paper recognition and closing remarks

## Invited Speakers

TBA

## Organizers

<table class="kdd26-people-table">
 <tr>
  <td>
   <img src="/images/people/menglin.png?raw=true" alt="Menglin Yang">
   <br>
   <a href="https://yangmenglinsite.github.io/">Menglin Yang</a>
   <br>
   HKUST (GZ)
  </td>
  <td>
   <img src="/images/people/jiahong.png?raw=true" alt="Jiahong Liu">
   <br>
   <a href="https://misc-lab.cse.cuhk.edu.hk/sciencex_teams/jiahong-liu/">Jiahong Liu</a>
   <br>
   CUHK
  </td>
  <td>
   <img src="/images/people/lucas.png" alt="Lucas Vinh Tran">
   <br>
   <a href="https://www.lucasvinhtran.com/">Lucas Vinh Tran</a>
   <br>
   JPMorgan Chase
  </td>
  <td>
   <img src="/images/people/rex.png?raw=true" alt="Rex Ying">
   <br>
   <a href="https://www.cs.yale.edu/homes/ying-rex/">Rex Ying</a>
   <br>
   Yale University
  </td>
 </tr>
</table>
