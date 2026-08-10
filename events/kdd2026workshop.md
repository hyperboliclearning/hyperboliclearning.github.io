---
title: "KDD 2026 Workshop: Geometric Space, Architecture and Learning Objectives for Large Pre-Trained Models"
layout: page
permalink: /events/kdd2026workshop
---

<link rel="stylesheet" href="/assets/neurips2025.css">

<div class="kdd26-lead">
<p><strong>The Geometric Space, Architecture and Learning Objectives for Large Pre-Trained Models (GALOP) workshop at <a href="https://kdd2026.kdd.org/">KDD 2026</a></strong> brings together researchers working on geometric representation spaces, geometry-aware architectures, and learning objectives for large pre-trained models, spanning natural language processing, computer vision, graph learning, knowledge discovery, and scientific AI.</p>
</div>


<div class="banner-container kdd26-banner">
 <img class="kdd26-banner-image" src="/images/kdd2026_cover_mid.jpg" alt="KDD 2026 official cover image">
 <div class="banner-overlay"></div>
 <div class="banner-text">
  Geometric Space, Architecture and Learning Objectives for Large Pre-Trained Models @KDD 2026
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
.kdd26-program-meta {
  margin: 0.35rem 0 1rem;
  color: #3d424a;
}
.kdd26-program-table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.75rem 0 1.5rem;
  background: #ffffff;
  border: 1px solid #d8d9dc;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(24, 33, 46, 0.07);
  font-size: 0.95rem;
}
.kdd26-program-table th,
.kdd26-program-table td {
  padding: 0.62rem 0.72rem;
  border-bottom: 1px solid #e5e2dd;
  text-align: left;
  vertical-align: middle;
  line-height: 1.45;
}
.kdd26-program-table th {
  background: linear-gradient(180deg, #edf3f5 0%, #e7eef1 100%);
  color: #1e2a36;
  font-weight: 800;
  letter-spacing: 0.01em;
}
.kdd26-program-table tr:last-child td {
  border-bottom: 0;
}
.kdd26-program-table tbody tr:nth-child(even) td {
  background: #fafbfb;
}
.kdd26-program-table tbody tr:nth-child(4) td {
  background: #f4eee5;
}
.kdd26-program-table td:first-child {
  width: 7.3rem;
  white-space: nowrap;
  color: #3a5a7c;
  font-weight: 750;
}
.kdd26-program-table td:nth-child(2) {
  width: 15rem;
  font-weight: 700;
}
.kdd26-speaker-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
.kdd26-speaker-card h3 {
  margin: 0 0 0.25rem;
  font-size: 1.55rem;
}
.kdd26-speaker-card p {
  text-align: left;
}
.kdd26-speaker-photo {
  width: 100%;
  max-width: 190px;
  aspect-ratio: 1 / 1;
  height: auto;
  object-fit: cover;
  object-position: center top;
  border-radius: 14px;
  display: block;
  margin: 0.65rem 0 0.85rem;
  background: #eef2f7;
  border: 1px solid #d8d9dc;
}
.kdd26-speaker-role {
  margin: 0 0 0.55rem;
  color: #5a6572;
  font-weight: 700;
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
  font-size: 1.35rem;
  font-weight: 760;
  letter-spacing: -0.01em;
  margin-top: 0.95rem;
  margin-bottom: 0.3rem;
  scroll-margin-top: 84px;
}
.post-content .kdd26-speaker-card h3 {
  font-size: 1.55rem;
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
.kdd26-slack-group {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin: 0.85rem 0 1.5rem;
  padding: 1.35rem 1.4rem;
  background: #ffffff;
  border: 1px solid #d8d9dc;
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(24, 33, 46, 0.07);
}
.kdd26-slack-group img {
  width: 190px;
  height: 190px;
  flex: 0 0 190px;
  display: block;
}
.kdd26-slack-group p {
  margin: 0;
  color: #3d424a;
  font-size: 1.08rem;
  line-height: 1.65;
  text-align: left;
}
.kdd26-slack-group a {
  color: #3a5a7c;
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
  .kdd26-speaker-grid {
    grid-template-columns: 1fr;
  }
  .kdd26-slack-group {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem;
  }
  .kdd26-slack-group img {
    width: 170px;
    height: 170px;
    flex-basis: 170px;
  }
  .kdd26-program-table,
  .kdd26-program-table tbody,
  .kdd26-program-table tr,
  .kdd26-program-table td {
    display: block;
    width: 100%;
  }
  .kdd26-program-table thead {
    display: none;
  }
  .kdd26-program-table tr {
    padding: 0.62rem 0.72rem;
    border-bottom: 1px solid #d8d9dc;
  }
  .kdd26-program-table tr:last-child {
    border-bottom: 0;
  }
  .kdd26-program-table td {
    padding: 0.15rem 0;
    border: 0;
  }
  .kdd26-program-table td:first-child,
  .kdd26-program-table td:nth-child(2) {
    width: 100%;
    white-space: normal;
  }
}
@media (min-width: 481px) and (max-width: 640px) {
  .kdd26-speaker-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .kdd26-program-table {
    display: table;
    width: 100%;
  }
  .kdd26-program-table thead {
    display: table-header-group;
  }
  .kdd26-program-table tbody {
    display: table-row-group;
  }
  .kdd26-program-table tr {
    display: table-row;
    padding: 0;
    border-bottom: 0;
  }
  .kdd26-program-table td {
    display: table-cell;
    width: auto;
    padding: 0.62rem 0.72rem;
    border-bottom: 1px solid #e5e2dd;
  }
  .kdd26-program-table td:first-child {
    width: 7.3rem;
    white-space: nowrap;
  }
  .kdd26-program-table td:nth-child(2) {
    width: 15rem;
  }
}
</style>

## News

- <span style="color: #8b1e1e;"><strong>2026-08-09:</strong> 🔥 The final workshop program and Workshop Slack group are now available.</span>
- 2026-07-25: Workshop date and time information has been updated.
- 2026-06-10: Paper notifications have been sent through OpenReview. Camera-ready revision is open for accepted papers.
- 2026-03-22: Call for papers, [OpenReview portal](https://openreview.net/group?id=KDD.org/2026/Workshop/GALOP)
- 2026-03-11: The workshop proposal was accepted by KDD 2026 as a half day workshop.

## Introduction

Foundation models now drive progress across language, vision, graphs, recommendation, and scientific discovery, yet most of them are still built around Euclidean representations and objectives. In many real world settings, however, the underlying data contain hierarchy, relational structure, multi scale organization, or nonuniform geometry that is not naturally captured by standard design choices.

**Target.** This workshop focuses on how geometric spaces, geometric neural networks, and geometric objectives can improve foundation models by introducing more appropriate inductive bias for representation, reasoning, and adaptation. It highlights work on hyperbolic, spherical, mixed curvature, and other geometry aware approaches that can better align model structure with the structure of data.

**Goal.** The goal is to bring together researchers from machine learning, data mining, natural language processing, computer vision, graph learning, knowledge discovery, and scientific AI. By connecting theory, methods, systems, and applications, the workshop aims to create a shared forum for understanding when geometric modeling matters, how it should be integrated into large models, and how its benefits should be evaluated in practice.

### Important Dates

Time: 11:59 PM Anywhere on Earth unless otherwise specified.

- <strong>Workshop paper submission:</strong> <span style="color: #6c757d;"><del>April 30, 2026</del></span> <strong>extended to May 31, 2026</strong>
- Workshop paper notification: June 10, 2026
- Camera-ready revision: June 15, 2026
- Final workshop program, materials, and full website online: June 22, 2026
- <span style="color: #8b1e1e;">Workshop date: August 9, 2026 afternoon (1:00 pm-5:00 pm)</span>
- Conference dates: August 9 to 13, 2026
- Venue: Room 201B, International Convention Center Jeju (ICC Jeju)

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

## Submission (Completed)

- The submission period has closed.
- Authors of accepted papers should submit the camera-ready revision through OpenReview by June 15, 2026.
- Accepted papers will be presented as oral or poster presentations, as indicated in the decision notification.
- The workshop follows the current KDD 2026 workshop policy and is planned as an in person event.

<p style="text-align: center;"><a class="kdd26-btn" href="https://openreview.net/group?id=KDD.org/2026/Workshop/GALOP">GALOP Workshop @ KDD 2026 OpenReview Portal</a></p>

## Accepted Papers

- [Geometric Perturbation Graph Neural Network for Heterophily Modeling](https://openreview.net/forum?id=xzPpTAWG25) (Oral + Poster)
- [Hyperattentive Residuals](https://openreview.net/forum?id=6I2ZE5IdXS) (Oral + Poster)
- [Revisiting CF-Integrated LLM Recommenders through Dimensional Collapse](https://openreview.net/forum?id=KaBEPwhpgK) (Oral + Poster)
- [MeSH-HyRerank: Hyperbolic Ontology Adaptation for Biomedical Foundation Model Retrieval](https://openreview.net/forum?id=1ssMLWnBwf) (Oral + Poster)
- [Curvature-Adaptive Self-Attention: Riemannian Transformers with Distortion and Generalization Bounds](https://openreview.net/forum?id=lSExhYH4Cz) (Poster)
- [Extracting Local Manifold Geometry from Pretrained Diffusion Models in One Inverse Step](https://openreview.net/forum?id=E7op24P6Uh) (Poster)

## Program

<p class="kdd26-program-meta"><strong>August 9, 2026 · 1:00–5:00 PM KST · Room 201B, International Convention Center Jeju (ICC Jeju)</strong></p>

<table class="kdd26-program-table">
 <thead>
  <tr>
   <th>Time (KST)</th>
   <th>Session</th>
   <th>Speaker / Presentation</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>1:00–1:05 PM</td>
   <td>Opening Remarks</td>
   <td>—</td>
  </tr>
  <tr>
   <td>1:05–2:00 PM</td>
   <td>Invited Talk 1<br><span style="font-weight: 500;">(Geometric Objective Function)</span></td>
   <td><strong>Prof. Yifei Zhang</strong><br>Understanding Self-supervised Learning from the Dimensional Collapse Perspective</td>
  </tr>
  <tr>
   <td>2:00–3:00 PM</td>
   <td>Invited Talk 2<br><span style="font-weight: 500;">(Geometric Architecture)</span></td>
   <td><strong>Prof. Kijung Shin</strong><br>AI for Complex Networks: With a Focus on Hypergraphs</td>
  </tr>
  <tr>
   <td>3:00–3:30 PM</td>
   <td>Coffee Break and Poster Session</td>
   <td>—</td>
  </tr>
  <tr>
   <td>3:30–3:45 PM</td>
   <td>Contributed Talk 1</td>
   <td>Geometric Perturbation Graph Neural Network for Heterophily Modeling</td>
  </tr>
  <tr>
   <td>3:45–4:00 PM</td>
   <td>Contributed Talk 2</td>
   <td>MeSH-HyRerank: Hyperbolic Ontology Adaptation for Biomedical Foundation Model Retrieval</td>
  </tr>
  <tr>
   <td>4:00–4:15 PM</td>
   <td>Contributed Talk 3</td>
   <td>Revisiting CF-Integrated LLM Recommenders through Dimensional Collapse</td>
  </tr>
  <tr>
   <td>4:15–4:30 PM</td>
   <td>Contributed Talk 4</td>
   <td>Hyperattentive Residuals</td>
  </tr>
  <tr>
   <td>4:30–5:00 PM</td>
   <td>Organizational Talk<br><span style="font-weight: 500;">(Geometric Embedding Space)</span></td>
   <td><strong>Ms. Jiahong Liu</strong><br>Hyperbolic Learning in the Era of Large Language Models</td>
  </tr>
 </tbody>
</table>

## Invited Speakers

<div class="kdd26-speaker-grid">
 <div class="kdd26-card kdd26-speaker-card">
  <h3><a href="https://yifeiacc.github.io/Lab/">Yifei Zhang</a></h3>
  <img class="kdd26-speaker-photo" src="https://yifeiacc.github.io/Lab/assets/img/group/yifei-zhang.jpg" alt="Yifei Zhang">
  <p class="kdd26-speaker-role">Professor, School of Computer Science, Northwestern Polytechnical University</p>
  <p>Yifei Zhang works on trustworthy machine learning, federated learning, graph representation learning, large language models, and robust vision-language models.</p>
 </div>
 <div class="kdd26-card kdd26-speaker-card">
  <h3><a href="https://kijungs.github.io/">Kijung Shin</a></h3>
  <img class="kdd26-speaker-photo" src="/images/people/kijung-shin.jpg" alt="Kijung Shin">
  <p class="kdd26-speaker-role">Associate Professor, KAIST AI &amp; EE; Director, Data Mining Lab</p>
  <p>Kijung Shin works on data mining, graph algorithms, and network science, with broad interests in scalable methods for structured and relational data.</p>
 </div>
</div>

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

## Slack Group

<div class="kdd26-slack-group">
 <img src="/images/kdd2026-workshop-slack-qr.png" alt="QR code for the Workshop Slack group">
 <p>Join the <a href="https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA"><strong>Workshop Slack group</strong></a> for community discussions and updates.</p>
</div>

## Contact

For questions about the workshop, please contact us at [galop-kdd2026@googlegroups.com](mailto:galop-kdd2026@googlegroups.com).
