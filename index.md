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
  </ul>
</div>

<style>
h1 {
  text-align: center;
  margin-top: 0.3em;
  margin-bottom: 1.2em;
}
h1::before { display: none; }
.cite-block {
  background: #f8f6f3;
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 12px;
  padding: 1.3rem 1.5rem;
  position: relative;
  margin-top: 0.8em;
}
.cite-block pre {
  margin: 0; color: #111; font-size: 0.8rem; line-height: 1.65;
  white-space: pre-wrap; word-break: break-all;
  font-family: 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace;
  background: transparent; padding: 0; border-radius: 0;
}
.cite-block .copy-btn {
  position: absolute; top: 0.7rem; right: 0.9rem;
  font-size: 0.75rem; color: var(--primary, #3a5a7c);
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  padding: 0.35em 0.9em; border-radius: 6px;
  cursor: pointer; transition: all 0.2s;
  font-family: 'Inter', sans-serif; font-weight: 600;
}
.cite-block .copy-btn:hover {
  background: var(--primary, #3a5a7c);
  color: #fff;
}
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
.sticky-outline ul {
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
}
.sticky-outline > ul > li {
  margin-bottom: 2px;
  text-align: left;
}
.sticky-outline li {
  margin-bottom: 1px;
  text-align: left;
}
.sticky-outline > ul > li > a {
  font-weight: 600;
  font-size: 0.9rem;
  padding: 1px 0;
  text-align: left;
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
  text-align: left;
}
.fig-container {
  text-align: center;
  margin: 1.8em 0;
}
.fig-container img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  border: 1px solid var(--border, #e5e2dd);
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}
.fig-container .fig-cap {
  font-size: 0.88em;
  color: var(--text-soft, #6b7280);
  margin-top: 0.6em;
  font-style: italic;
  line-height: 1.5;
}
.math-block {
  background: #f8f6f3;
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 10px;
  padding: 1rem 1.4rem;
  margin: 1.2em 0;
  text-align: center;
  font-size: 1.02em;
  overflow-x: auto;
}
</style>

<script>
MathJax = { tex: { inlineMath: [['$','$'], ['\\(','\\)']], displayMath: [['$$','$$'], ['\\[','\\]']] } };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>

## Events and News!

- [Hyperbolic Fine-tuning for Large Language Models (HypLoRA)]({{ "/work/hyplora" | relative_url }})
- [HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts - PDF](https://arxiv.org/abs/2505.24722)
- [KDD 2026 Geometric Learning Workshop]({{ "/events/kdd2026workshop" | relative_url }})
- [NeurIPS 2025 NEGEL Workshop]({{ "/events/neurips2025negelworkshop" | relative_url }})
- [AAAI 2026 Hyperbolic FM Tutorial]({{ "/events/aaai2026tutorial" | relative_url }})
- [KDD 2025 Hyperbolic FM Tutorial]({{ "/events/kdd2025tutorial" | relative_url }})
- [WWW 2025 NEGEL Workshop]({{ "/events/www2025workshop" | relative_url }})
- [KDD 2023 Tutorial](https://hyperbolicgnn.github.io/)
- [Slack channel for more discussions and tracking updates!](https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA)
- [Awesome Hyperbolic Representation and Deep Learning Repository]({{ "/collection" | relative_url }})

## Introduction

Foundation models, including large language models (LLMs), vision-language models (VLMs), and large multimodal models, pre-trained on massive datasets, have demonstrated remarkable success in diverse downstream tasks. Models such as GPT-4, LLaMA, CLIP, and Gemini have pushed the boundaries of what is possible in natural language understanding, visual reasoning, and cross-modal generation. However, recent studies reveal fundamental limitations of these models: **(1) limited representational capacity** for hierarchical and structured data, **(2) lower adaptability** when fine-tuning on tasks with inherent geometric structure, and **(3) less scalability** due to the polynomial growth of Euclidean embeddings struggling to capture exponentially branching relationships.

These shortcomings raise a critical question: **Is Euclidean geometry truly the optimal inductive bias for foundation models, or could alternative geometric spaces better align with the intrinsic structure of real-world data and reasoning processes?**

Consider a simple example: natural language inherently contains hierarchical structures—words compose phrases, phrases compose sentences, sentences compose paragraphs, and so on. Similarly, knowledge graphs encode taxonomic relationships (e.g., "animal → mammal → dog → poodle") that grow exponentially with depth. In Euclidean space, representing a balanced binary tree of depth $d$ with low distortion requires $\mathcal{O}(2^d)$ dimensions, whereas in hyperbolic space, the same tree can be faithfully embedded in just **2 dimensions**. This exponential advantage motivates the exploration of hyperbolic geometry as a foundational building block for modern AI systems.

<div class="fig-container" style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;">
  <img src="/images/figs/root-leaf.png" alt="Root-leaf proximity in hyperbolic space" style="flex: 1 1 48%; min-width: 280px;">
  <img src="/images/figs/leaf-leaf.png" alt="Leaf-leaf distance in hyperbolic space" style="flex: 1 1 48%; min-width: 280px;">
</div>
<div class="fig-container" style="margin-top: 0;">
  <div class="fig-cap">Figure 1: Hyperbolic space naturally encodes hierarchical structure. <strong>Left</strong>: Root and leaf nodes are close in hyperbolic distance, reflecting parent-child relationships. <strong>Right</strong>: Leaf nodes from different branches are far apart, preserving the tree's branching structure. The exponential volume growth of hyperbolic space enables faithful low-distortion embeddings of trees.</div>
</div>

This webpage provides a comprehensive overview of hyperbolic geometry and non-Euclidean representations for large language models and foundation models. We cover the mathematical foundations, key computational models, neural network architectures, and state-of-the-art methods that bring hyperbolic geometry to modern AI.


## 1. Hyperbolic Geometry

Hyperbolic geometry represents one of the most profound developments in mathematical history, emerging from the centuries-long quest to understand Euclid's fifth postulate (the parallel postulate). For over two thousand years, mathematicians attempted to derive the parallel postulate from the other four axioms. It was not until the 19th century that Lobachevsky, Bolyai, and Gauss independently discovered that rejecting the parallel postulate leads to a consistent, non-Euclidean geometry—**hyperbolic geometry**.

Unlike Euclidean geometry, where exactly one parallel line passes through a given external point, **hyperbolic geometry permits infinitely many parallel lines through a point external to a given line**. This fundamental difference creates a geometric space with **constant negative curvature** $\kappa < 0$, contrasting with the flat (zero curvature) Euclidean space and the positive curvature of spherical geometry.

### Key Properties of Hyperbolic Space

The distinctive properties of hyperbolic spaces set them apart from Euclidean geometry in ways that are profoundly useful for machine learning:

- **Exponential volume growth**: The area of a disk of radius $r$ in hyperbolic space grows as $\mathcal{O}(e^{r})$, compared to $\mathcal{O}(r^2)$ in Euclidean space. This means hyperbolic space can "fit" exponentially more content at increasing distances from the origin—precisely matching the branching factor of trees and hierarchies.

- **Triangle angle deficit**: The sum of angles in a hyperbolic triangle is always **strictly less than $\pi$** (180°), with the deficit proportional to the triangle's area. Specifically, for a triangle with angles $\alpha, \beta, \gamma$ and curvature $\kappa$, the area equals $(\pi - \alpha - \beta - \gamma) / \lvert\kappa\rvert$.

- **Distance distortion**: Distances grow exponentially as one moves away from the origin. In the Poincaré disk model, the metric tensor is $g_{ij} = \frac{4}{(1 - \lVert x\rVert^2)^2}\delta_{ij}$, meaning distances near the boundary of the disk are dramatically stretched—a point that appears close to the boundary in visual coordinates is actually infinitely far from the center.

- **Natural hierarchy representation**: A regular tree with branching factor $b$ and depth $d$ has $\mathcal{O}(b^d)$ nodes. The exponential volume growth of hyperbolic space naturally accommodates such structures, enabling low-distortion embeddings with remarkably few dimensions.

### Why Hyperbolic Geometry for AI?

Real-world data frequently exhibits hierarchical or scale-free structure. Natural language has syntactic parse trees, knowledge graphs form taxonomies, protein structures involve nested sub-domains, social networks display community hierarchies, and image features organize from low-level textures to high-level semantics. The **Gromov $\delta$-hyperbolicity** of many real-world graphs (small $\delta$ values indicate tree-like structure) confirms that these datasets are intrinsically more hyperbolic than Euclidean, providing a principled motivation for leveraging hyperbolic representations in deep learning.


## 2. Hyperbolic Models

To visualize and work with hyperbolic geometry computationally, mathematicians have developed several isometric models. Each model represents the same underlying hyperbolic space but offers different computational trade-offs. Understanding these models is essential for designing hyperbolic neural networks.

### Poincaré Ball Model

The Poincaré ball model $(\mathbb{B}^n_\kappa, g^{\mathbb{B}})$ represents $n$-dimensional hyperbolic space as the interior of the unit ball $\mathbb{B}^n = \{x \in \mathbb{R}^n : \lVert x\rVert < 1\}$. The Riemannian metric is given by:

<div class="math-block">
$g^{\mathbb{B}}_x = \left(\frac{2}{1 - \lVert x\rVert^2}\right)^2 g^E$
</div>

where $g^E$ is the Euclidean metric. This model is **conformal** (preserves angles but distorts distances) and is the most widely used in machine learning due to its intuitive visualization properties—the origin represents the "root" of a hierarchy, and branches spread toward the boundary. Key operations include the **Möbius addition** $x \oplus_\kappa y$ and the **exponential/logarithmic maps** that transport vectors between the tangent space and the manifold.

### Lorentz (Hyperboloid) Model

The Lorentz model $(\mathbb{H}^n_\kappa, g^{\mathbb{L}})$ embeds hyperbolic space as the upper sheet of a hyperboloid in $(n+1)$-dimensional Minkowski space:

<div class="math-block">
$\mathbb{H}^n = \{x \in \mathbb{R}^{n+1} : \langle x, x \rangle_{\mathcal{L}} = -1/\kappa, \; x_0 > 0\}$
</div>

where $\langle x, y \rangle_{\mathcal{L}} = -x_0 y_0 + \sum_{i=1}^{n} x_i y_i$ is the Minkowski inner product. The Lorentz model has **superior numerical stability** compared to the Poincaré model (avoiding the boundary singularity) and is often preferred for optimization. The geodesic distance is:

<div class="math-block">
$d_{\mathbb{H}}(x, y) = \frac{1}{\sqrt{\lvert\kappa\rvert}} \operatorname{arccosh}\!\big(-\kappa \langle x, y \rangle_{\mathcal{L}}\big)$
</div>

### Klein Model

The Klein model represents hyperbolic space within a disk where **geodesics appear as straight chords** rather than arcs. While it distorts both angles and distances, it offers computational simplicity for certain geometric operations such as computing convex hulls and determining whether points lie on the same geodesic. The metric is non-conformal, making it less popular in neural network applications but valuable for geometric algorithms.

### Poincaré Half-Plane Model

The upper half-plane model $\mathbb{U}^n = \{x \in \mathbb{R}^n : x_n > 0\}$ with metric $g^{\mathbb{U}}_x = \frac{1}{x_n^2} g^E$ offers an unbounded representation of hyperbolic space. It is particularly useful for theoretical analysis and has deep connections to complex analysis and modular forms. Like the Poincaré ball, it is conformal.

### Inter-Model Mappings

All four models are isometric to one another, and explicit diffeomorphisms exist between them. In practice, researchers often perform **forward computation in the Lorentz model** (for numerical stability) and **visualization in the Poincaré ball** (for interpretability), converting between models as needed.


## 3. Hyperbolic Neural Networks

Hyperbolic neural networks extend deep learning architectures to operate directly in hyperbolic space, enabling more efficient representation of hierarchical data. **The core insight is that hierarchical relationships require exponentially increasing capacity at greater depths—precisely matching the exponential volume growth of hyperbolic spaces.**

### Hyperbolic Embeddings

Hyperbolic embeddings represent discrete objects (such as nodes in a graph or words in a vocabulary) as points in hyperbolic space. The seminal work by Nickel and Kiela (2017) demonstrated that **Poincaré embeddings** of the WordNet noun hierarchy could achieve superior performance with just 5 dimensions compared to 200-dimensional Euclidean embeddings. Subsequent work introduced embeddings in the Lorentz model for improved optimization stability.

Key advantages of hyperbolic embeddings include:
- **Dimensionality reduction**: Orders-of-magnitude fewer parameters for hierarchical data
- **Implicit hierarchy preservation**: Distance from the origin encodes hierarchical depth
- **Continuous relaxation of trees**: Hyperbolic space serves as a continuous analogue of discrete tree structures

### Hyperbolic Neural Layers

Since hyperbolic space is a Riemannian manifold (not a vector space), standard operations like matrix multiplication and addition must be carefully redefined. Three main paradigms have emerged:

- **Tangent space approach**: Map points to the tangent space at a reference point (typically the origin), apply standard Euclidean operations, and project back using the exponential map. This is computationally efficient but introduces approximation errors, especially for points far from the reference.

- **Möbius gyrovector approach**: The Möbius addition $\oplus_\kappa$ and Möbius scalar multiplication $\otimes_\kappa$ provide intrinsic operations in the Poincaré ball that generalize their Euclidean counterparts. A hyperbolic linear layer can be defined as $f(x) = M \otimes_\kappa x \oplus_\kappa b$, where $M$ is a learnable weight matrix and $b$ is a bias in hyperbolic space.

- **Lorentz operations**: Directly define neural network operations on the hyperboloid using the Lorentz inner product and parallel transport. This approach often yields better numerical stability and has become increasingly popular in recent architectures.

### Key Architectures

Several foundational hyperbolic architectures have been developed:

- **HGCN** (Hyperbolic Graph Convolutional Networks): Extends GCNs to hyperbolic space, achieving state-of-the-art on hierarchical graph benchmarks
- **HNN/HNN++** (Hyperbolic Neural Networks): General-purpose hyperbolic feedforward and recurrent networks
- **HGNN** (Hyperbolic Graph Neural Networks): Message-passing framework adapted for hyperbolic geometry
- **$\kappa$-GCN**: Operates in stereographic model with learnable curvature, unifying hyperbolic ($\kappa < 0$), Euclidean ($\kappa = 0$), and spherical ($\kappa > 0$) geometries

### Hyperbolic Activation Functions

Standard activation functions (ReLU, tanh, sigmoid) operate in Euclidean space and cannot be directly applied to hyperbolic points. Hyperbolic activation functions are typically defined by: (1) projecting to tangent space via the logarithmic map, (2) applying the Euclidean activation, and (3) mapping back via the exponential map. More recent approaches define intrinsic activations that avoid this intermediate mapping.

### Optimization in Hyperbolic Space

Training hyperbolic networks requires **Riemannian optimization**, where gradients are computed in the tangent space and updates follow geodesics rather than straight lines. Riemannian SGD and Riemannian Adam have been developed for this purpose, with the update rule:

<div class="math-block">
$x_{t+1} = \text{exp}_{x_t}(-\eta \cdot \text{grad}_R f(x_t))$
</div>

where $\text{exp}_{x_t}$ is the exponential map and $\text{grad}_R$ is the Riemannian gradient.


## 4. Hyperbolic Transformers

Transformer architectures revolutionized natural language processing through their self-attention mechanisms and efficient parallel processing of sequential data. **Hyperbolic transformers extend this paradigm to hyperbolic space, particularly benefiting applications involving deeply nested linguistic structures, hierarchical relations, and multi-scale features.**

The key challenge in building hyperbolic transformers is that the self-attention mechanism relies heavily on linear algebra operations (queries, keys, values via matrix multiplication, softmax normalization) that assume Euclidean structure. Adapting each component to respect hyperbolic geometry requires careful mathematical reformulation.

### Hyperbolic Attention Mechanisms

The standard attention score $\text{Attn}(Q, K) = \text{softmax}(QK^T / \sqrt{d_k})$ can be reformulated using hyperbolic distance:

<div class="math-block">
$\alpha_{ij} = \text{softmax}\left(-\beta \cdot d_{\mathbb{H}}(q_i, k_j)^2\right)$
</div>

where $d_{\mathbb{H}}$ is the hyperbolic distance and $\beta$ is a learnable temperature. This formulation naturally emphasizes hierarchical relationships: tokens at similar hierarchical levels (similar distance from the origin) produce stronger attention scores, while cross-level attention captures parent-child dependencies.

Alternative formulations include:
- **Lorentz attention**: Using the Minkowski inner product $\langle q_i, k_j \rangle_{\mathcal{L}}$ directly as an attention score
- **Tangent-space attention**: Computing standard dot-product attention in the tangent space, then projecting results back
- **Hybrid attention**: Combining Euclidean and hyperbolic attention heads within the same layer

### Multi-Resolution Processing

One of the most compelling advantages of hyperbolic transformers is their ability to simultaneously process information at different scales. In the Poincaré disk, points near the center capture high-level, coarse-grained information (analogous to root-level concepts), while points near the boundary encode fine-grained details (analogous to leaf-level specifics). This natural multi-resolution property enables hyperbolic transformers to process hierarchical abstractions more efficiently than their Euclidean counterparts.

### Hyperbolic Position Encodings

Position encodings adapted to hyperbolic geometry can better preserve hierarchical relationships between tokens. Instead of sinusoidal or learned Euclidean position vectors, **hyperbolic position encodings** place position information on the manifold, where the distance structure naturally encodes both sequential order and hierarchical depth. For example, in a document with sections, subsections, and paragraphs, hyperbolic position encodings can jointly capture both the linear reading order and the nesting structure.

### Notable Hyperbolic Transformer Models

- **Fully Hyperbolic Transformers**: Implement all components (attention, FFN, normalization) in hyperbolic space
- **HyboNet**: Uses Lorentz transformations for fully hyperbolic computation
- **Hyperbolic BERT**: Adapts pre-trained BERT representations to hyperbolic space for improved hierarchical NLP tasks
- **Mixed-Curvature Transformers**: Use product manifolds combining hyperbolic, Euclidean, and spherical components


## 5. Hyperbolic Foundation Models

Foundation models—large-scale systems trained on broad data that can be fine-tuned for specific applications—represent the cutting edge of modern AI. **Hyperbolic foundation models incorporate hyperbolic geometry into their architecture to better capture the hierarchical structures inherent in language, knowledge, and multimodal data.** This represents one of the most active and promising frontiers in geometric deep learning.

### Hyperbolic Large Language Models

Recent work has demonstrated that incorporating hyperbolic geometry into LLMs yields measurable improvements:

- **[HypLoRA]({{ "/work/hyplora" | relative_url }})** (Yang et al., 2025): Introduces hyperbolic low-rank adaptation for fine-tuning LLMs. By performing LoRA updates in hyperbolic space, HypLoRA better captures the hierarchical nature of downstream tasks while maintaining the parameter efficiency of standard LoRA. Experiments show consistent gains on commonsense reasoning, natural language understanding, and mathematical reasoning benchmarks.

- **[HELM](https://arxiv.org/abs/2505.24722)** (Hyperbolic LLMs via Mixture-of-Curvature Experts): Proposes a mixture-of-experts architecture where different experts operate in spaces of different curvatures (hyperbolic, Euclidean, spherical), allowing the model to adaptively select the optimal geometry for each input.

- **Hyperbolic Token Embeddings**: Replacing standard Euclidean token embeddings with hyperbolic embeddings can improve the representation of taxonomic and compositional relationships, especially beneficial for tasks involving structured knowledge.

### Hyperbolic Vision Foundation Models

Visual data exhibits hierarchical structure at multiple levels—from pixels to textures, parts, objects, and scenes. Hyperbolic vision models exploit this:

- **Hyperbolic Image Embeddings**: Mapping image features to hyperbolic space for improved zero-shot and few-shot classification, especially when label hierarchies are available (e.g., ImageNet's WordNet-based class taxonomy)
- **Hyperbolic CLIP**: Adapting CLIP's contrastive learning to hyperbolic space, enabling better cross-modal alignment of hierarchical visual and linguistic concepts
- **Hyperbolic ViT**: Vision Transformers with hyperbolic attention and position encodings

### Hyperbolic Multi-Modal Models

Multi-modal foundation models (e.g., combining vision, language, and audio) benefit from hyperbolic geometry through:

- **Cross-Modal Hierarchical Alignment**: Different modalities often share hierarchical structure (e.g., a visual scene graph and a textual description both encode part-whole relationships). Hyperbolic space provides a natural shared geometry for aligning these hierarchies.
- **Compositional Grounding**: Hyperbolic representations can better capture the compositional nature of language and visual scenes, where meanings compose hierarchically.
- **Efficient Multi-Modal Fusion**: The parameter efficiency of hyperbolic representations reduces the overhead of multi-modal fusion layers.

### Key Advantages

• **Improved Knowledge Representation**: Hyperbolic foundation models can more efficiently encode taxonomic knowledge, ontological relationships, and compositional semantics, potentially reducing parameter counts while improving performance on tasks requiring hierarchical understanding.

• **Enhanced Reasoning Capabilities**: The natural tree-like structure of hyperbolic space aligns with logical hierarchies and deductive reasoning patterns, potentially enabling more sophisticated chain-of-thought and structured reasoning abilities.

• **More Efficient Scaling**: The intrinsic capacity of hyperbolic space to represent exponentially more information within the same dimensionality suggests better scaling properties as model sizes increase—a critical factor given the computational cost of modern foundation models.

• **Cross-Modal Hierarchical Alignment**: For multimodal foundation models, hyperbolic representations may better align hierarchical structures across different modalities (e.g., visual scene graphs with linguistic parse trees), improving performance on complex cross-modal tasks.


## 6. Challenges and Opportunities

<span style="color:#547a80">While hyperbolic deep learning demonstrates significant promise, several important challenges remain:</span>

• **Numerical Stability**: Hyperbolic operations involve exponential and hyperbolic trigonometric functions that can lead to overflow/underflow, especially near the boundary of the Poincaré disk where the conformal factor $\lambda_x = \frac{2}{1-\lVert x\rVert^2}$ diverges. Techniques such as **clipping norms**, **working in the Lorentz model**, and **mixed-precision training** have been developed to mitigate these issues, but a general solution remains elusive.

• **Optimization Difficulties**: Riemannian optimization (RSGD, RAdam) in hyperbolic space is more complex than standard gradient descent. The curvature of the space introduces additional terms in the update rules, and **learning rate sensitivity** is amplified—points near the boundary of the Poincaré disk experience much larger effective step sizes. Developing efficient, stable, and scalable Riemannian optimizers is an active research area.

• **Scalability to Large Models**: While hyperbolic methods have shown success at moderate scales, scaling to billions of parameters introduces engineering challenges. GPU-efficient implementations of hyperbolic operations, memory-efficient training strategies, and distributed Riemannian optimization are needed to bring hyperbolic methods to production-scale foundation models.

• **Integration with Existing Architectures**: Seamlessly combining hyperbolic components with traditional Euclidean deep learning modules presents both theoretical and implementation challenges. **Hybrid approaches** that selectively apply hyperbolic geometry to specific components (e.g., embedding layers or attention modules) while keeping other components Euclidean have shown promise as a practical middle ground.

• **Theoretical Understanding**: The theoretical foundations of hyperbolic deep learning are still developing. Key open questions include: generalization bounds for hyperbolic networks, the expressiveness gap between hyperbolic and Euclidean representations, optimal curvature selection strategies, and the approximation theory of functions on hyperbolic manifolds.

• **Learnable Curvature**: The curvature parameter $\kappa$ significantly affects representation quality, but it is often treated as a hyperparameter. Learning curvature jointly with model parameters, or using **product manifolds with mixed curvatures**, remains a promising but challenging direction.

<span style="color:#547a80">Despite these challenges, hyperbolic geometry in deep learning presents exciting opportunities:</span>

• **Extreme Efficiency in Hierarchical Tasks**: For applications dominated by tree-like structures (taxonomies, ontologies, organizational charts), hyperbolic approaches could dramatically reduce model size while improving performance—achieving "more with less."

• **Novel Architectural Paradigms**: Fully embracing non-Euclidean geometry may inspire fundamentally new neural network architectures beyond current paradigms, analogous to how the Transformer architecture revolutionized sequence modeling.

• **Cross-Disciplinary Insights**: The integration of differential geometry, algebraic topology, and Riemannian optimization with deep learning opens possibilities for importing powerful techniques from mathematics and theoretical physics into machine learning.

• **Biologically Inspired Representations**: Growing evidence suggests that biological neural systems may utilize hyperbolic-like representations for spatial navigation and conceptual organization. This connection offers insights for neuromorphic computing and cognitive architectures.

• **AI for Science**: Hyperbolic representations are particularly well-suited for scientific data with inherent hierarchical structure—molecular graphs, protein folding hierarchies, phylogenetic trees, and multi-scale physical simulations.


## 7. Conclusion

Hyperbolic geometry provides a powerful mathematical framework for enhancing deep learning systems, particularly for applications involving hierarchical, tree-like structures that are ubiquitous in natural language, knowledge representation, computer vision, and scientific data. **The intersection of hyperbolic geometry and artificial intelligence represents a frontier where mathematical elegance meets practical utility**, potentially addressing fundamental limitations of traditional Euclidean approaches.

As research progresses, we can expect hyperbolic methods to become increasingly integrated into mainstream deep learning systems, particularly for knowledge-intensive applications requiring multi-scale reasoning. The development of stable, efficient hyperbolic operations and their thoughtful integration into neural architectures promises significant advances in AI's ability to represent and reason about complex hierarchical structures.

Key directions to watch include: **(1)** scaling hyperbolic foundation models to billions of parameters, **(2)** mixed-curvature and product manifold approaches that adaptively combine different geometries, **(3)** hyperbolic methods for reasoning and planning in LLM agents, and **(4)** applications in AI for science where hierarchical structure is a first-class concern.

We invite the community to join us in advancing this exciting research direction. Please refer to our [events page]({{ "/events" | relative_url }}) for upcoming workshops and tutorials, and our [collection page]({{ "/collection" | relative_url }}) for a comprehensive literature reference.


## Contributors

Menglin Yang, Neil He, Hiren Madhu, Ngoc Bui, Ali Maatouk, Rishabh Anand, Yifei Zhang, Jialin Chen, Jiahong Liu, Bo Xiong, Min Zhou, Irwin King, Melanie Weber, Rex Ying

Invited Speakers: Philip S. Yu, Shirui Pan, Min Zhou, Pascal Mettes, Smita Krishnaswamy

## Citation

If you find this webpage useful, please consider citing our work:

<div class="cite-block">
  <button class="copy-btn" onclick="copyBib(this)">Copy</button>
  <pre id="bib-text">@article{yang2024hyperbolic,
  title     = {Hyperbolic Geometry and Non-Euclidean Representations
               for Large Language Models},
  author    = {Yang, Menglin and He, Neil and Madhu, Hiren and
               Bui, Ngoc and Maatouk, Ali and Anand, Rishabh and
               Zhang, Yifei and Chen, Jialin and Liu, Jiahong and
               Xiong, Bo and Zhou, Min and King, Irwin and
               Weber, Melanie and Ying, Rex},
  year      = {2024},
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
