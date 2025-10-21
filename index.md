---
title: "Hyperbolic and Non-Euclidean Geometry for LLMs"
layout: page
permlink: /
---

<link rel="stylesheet" href="/style.css">

## Introduction

Foundation models, including large language models (LLMs), vision-language models (VLMs), and large multimodal models, pre-trained on massive datasets, have demonstrated remarkable success in diverse downstream tasks. However recent studies reveal fundamental limitations of these models: (1) limited representational capacity, (2) lower adaptability, and (3) less scalability. These shortcomings raise a critical question: Is Euclidean geometry truly the optimal inductive bias for foundation models, or could alternative geometric spaces better align with the intrinsic structure of real-world data and reasoning processes?

<div class="sticky-outline">
  <ul>
    <li><a href="#events-and-news">Events and News</a></li>
    <li><a href="#1-hyperbolic-geometry">Hyperbolic Geometry</a></li>
    <li><a href="#2-hyperbolic-models">Hyperbolic Models</a></li>
    <li><a href="#3-hyperbolic-neural-networks">Hyperbolic Neural Networks</a></li>
    <li><a href="#4-hyperbolic-transformers">Hyperbolic Transformers</a></li>
    <li><a href="#5-hyperbolic-foundation-models">Hyperbolic Foundation Models</a></li>
    <li><a href="#challenges-and-opportunities">Challenges and Opportunities</a></li>
    <li><a href="#6-conclusion">Conclusion</a></li>
  </ul>
</div>

<style>
body {
  background-color: #ffffff;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}
.wrapper {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}
h1 {
  color: #000000;
  text-align: center;
  margin-top: 0.5em;
  margin-bottom: 1.5em;
}
h2, h3, h4, h5, h6 {
  color: #000000;
}
.sticky-outline {
  position: fixed;
  top: 80px;
  left: 20px;
  width: 180px;
  max-height: 60vh;
  overflow-y: auto;
  background: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  padding: 8px 6px;
  z-index: 1000;
  font-size: 0.7rem;
  text-align: left;
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
  color: #0366d6;
  text-decoration: none;
  transition: color 0.2s;
  display: block;
  padding: 1px 0;
  text-align: left;
  font-weight: bold;
}
.sticky-outline a:hover {
  color: #2222B2;
  text-decoration: underline;
  text-align: left;
}
</style>

## Events and News!

- [Hyperbolic Fine-tuning for Large Language Models (HypLoRA)]({{ "/work/hyplora" | relative_url }})
- [HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts - PDF](https://arxiv.org/abs/2505.24722)
- [NeurIPS 2025 NEGEL Workshop]({{ "/events/neurips2025negelworkshop" | relative_url }})
- [KDD 2025 Hyperbolic FM Tutorial]({{ "/events/kdd2025tutorial" | relative_url }})
- [WWW 2025 NEGEL Workshop]({{ "/events/www2025workshop" | relative_url }})
- [KDD 2023 Tutorial](https://hyperbolicgnn.github.io/)
- [Slack channel for more discussions and tracking updates!](https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA) 
- [Awesome Hyperbolic Representation and Deep Learning Repository]({{ "/collection" | relative_url }})

## 1. Hyperbolic Geometry

Hyperbolic geometry represents one of the most profound developments in mathematical history, emerging from the centuries-long quest to understand Euclid's fifth postulate. Unlike Euclidean geometry, where parallel lines maintain a constant distance, **hyperbolic geometry permits an infinite number of parallel lines through a point external to a given line**. This fundamental difference creates a geometric space with constant negative curvature, contrasting with the flat (zero curvature) Euclidean space and the positive curvature of spherical geometry.

The distinctive properties of hyperbolic spaces include:

- **Exponential growth of area/volume** with respect to radius
- **Angle sum in triangles less than 180 degrees**
- **Distance distortion** that increases with distance from the origin
- **Natural representation of hierarchical structures and tree-like data**

## 2. Hyperbolic Models

To visualize and work with hyperbolic geometry, mathematicians have developed several models, each offering unique advantages:

• **Poincaré Disk Model**: The Poincaré disk represents the entire hyperbolic plane as the interior of a circle, where straight lines in hyperbolic space appear as either circular arcs perpendicular to the boundary or as diameters. **This model is conformal (preserves angles) but not isometric (distorts distances)**, with distances increasingly compressed as one approaches the boundary. The Poincaré disk model is particularly valuable for visualization and has become the most commonly used representation in machine learning applications.

• **Lorentz (Hyperboloid) Model**: The Lorentz model embeds hyperbolic space as a hyperboloid in Minkowski space. **It preserves the intrinsic geometry most faithfully but requires working in higher dimensions**. The Lorentz model is particularly useful for mathematical analysis and serves as a foundation for many theoretical results.

• **Klein Model**: The Klein model represents hyperbolic space within a disk where geodesics appear as straight chords. While it distorts both angles and distances, it offers computational simplicity for certain operations.

• **Poincaré Half-Plane Model**: Similar to the disk model but representing hyperbolic space as the upper half of the complex plane. It maintains the conformal property while offering different computational advantages.

## 3. Hyperbolic Neural Networks

Hyperbolic neural networks extend deep learning architectures to operate in hyperbolic space, enabling more efficient representation of hierarchical data. **The core insight driving hyperbolic neural networks is that hierarchical relationships require exponentially increasing capacity to represent at greater depths—precisely matching the exponential volume growth of hyperbolic spaces**.

Key components include:

- **Hyperbolic Embeddings**: These represent discrete objects (like nodes in a graph) as points in hyperbolic space. Hyperbolic embeddings have demonstrated remarkable ability to represent complex hierarchies with significantly fewer dimensions than their Euclidean counterparts, achieving state-of-the-art performance on tasks involving taxonomies, organizational hierarchies, and knowledge graphs.

- **Hyperbolic Neural Layers**: These extend the concept of linear transformations to hyperbolic space. Since hyperbolic space lacks a vector space structure, operations like matrix multiplication must be carefully redefined. Approaches include:
    - **Tangent space projections**: Mapping inputs to the tangent space, applying Euclidean operations, and projecting back
    - **Möbius transformations**: Extending complex-valued operations to the Poincaré disk
    - **Gyrovector operations**: Using non-associative algebraic structures to define operations analogous to vector addition and scalar multiplication

- **Hyperbolic Activation Functions**: These adapt standard activation functions to respect hyperbolic geometry, typically by applying the Euclidean function in tangent space before projecting back to the hyperbolic manifold.

## 4. Hyperbolic Transformers

Transformer architectures revolutionized natural language processing through their attention mechanisms and efficient handling of sequential data. **Hyperbolic transformers extend this paradigm to hyperbolic space, particularly benefiting applications involving deeply nested linguistic structures, hierarchical relations, and multi-scale features**.

Key innovations include:

- Hyperbolic Attention
Redefines attention mechanisms using hyperbolic distance metrics, enabling the model to better capture hierarchical dependencies. Distance calculations in hyperbolic space naturally emphasize structural relationships, with points at similar hierarchical levels appearing closer together despite potential semantic differences.

- Multi-Resolution Processing
Hyperbolic transformers can simultaneously process information at different scales, making them particularly effective for tasks involving multi-level abstractions or hierarchies with varying granularity.

- Hyperbolic Position Encodings
Position encodings adapted to hyperbolic geometry can better preserve hierarchical relationships between tokens or elements in a sequence.

## 5. Hyperbolic Foundation Models

Foundation models—large-scale systems trained on broad data that can be fine-tuned for specific applications—represent the cutting edge of modern AI. **Hyperbolic foundation models incorporate hyperbolic geometry into their architecture to better capture the hierarchical structures inherent in language, knowledge, and multimodal data**.

Potential advantages include:

• **Improved Knowledge Representation**: Hyperbolic foundation models can more efficiently encode taxonomic knowledge, ontological relationships, and compositional semantics, potentially reducing parameter counts while improving performance on tasks requiring hierarchical understanding.

• **Enhanced Reasoning Capabilities**: The natural tree-like structure of hyperbolic space aligns with logical hierarchies and deductive reasoning patterns, potentially enabling more sophisticated reasoning abilities.

• **More Efficient Scaling**: The intrinsic capacity of hyperbolic space to represent exponentially more information within the same dimensionality suggests better scaling properties as model sizes increase.

• **Cross-Modal Hierarchical Alignment**: For multimodal foundation models, hyperbolic representations may better align hierarchical structures across different modalities (e.g., visual scene graphs with linguistic parse trees).

## 6. Challenges and Opportunities

<span style="color:#0366d6">While hyperbolic deep learning demonstrates significant promise, several important challenges remain:</span>

• **Computational Challenges**: Implementing hyperbolic operations requires careful numerical handling to maintain stability, especially near the boundaries of models like the Poincaré disk where distances approach infinity. Current implementations often suffer from numerical issues that limit their practical deployment at scale.

• **Optimization Difficulties**: Optimization in hyperbolic space requires Riemannian optimization techniques that are more complex than standard gradient descent. Developing efficient and stable optimization methods for hyperbolic neural networks remains an active research area.

• **Integration with Existing Architectures**: Seamlessly combining hyperbolic components with traditional deep learning modules presents both theoretical and implementation challenges. Hybrid approaches that selectively apply hyperbolic geometry to appropriate components show promise.

• **Theoretical Understanding**: The theoretical foundations of hyperbolic deep learning are still developing. Better understanding of generalization, representation capacity, and optimization dynamics in hyperbolic space would accelerate progress.

<span style="color:#0366d6">Despite these challenges, hyperbolic geometry in deep learning presents exciting opportunities:</span>

• **Extreme Efficiency in Hierarchical Tasks**: For applications dominated by tree-like structures, hyperbolic approaches could dramatically reduce model size while improving performance.

• **Novel Architectural Paradigms**: Fully embracing non-Euclidean geometry may inspire fundamentally new neural network architectures beyond current paradigms.

• **Cross-Disciplinary Insights**: The integration of differential geometry with deep learning opens possibilities for importing techniques from mathematics and theoretical physics.

• **Biologically Inspired Representations**: Some evidence suggests that biological neural systems may utilize hyperbolic-like representations, offering potential insights for neuromorphic computing.

## 7. Conclusion

Hyperbolic geometry provides a powerful framework for enhancing deep learning systems, particularly for applications involving hierarchical, tree-like structures. **The intersection of hyperbolic geometry and artificial intelligence represents a frontier where mathematical elegance meets practical utility**, potentially addressing fundamental limitations of traditional Euclidean approaches.

As research progresses, we can expect hyperbolic methods to become increasingly integrated into mainstream deep learning systems, particularly for knowledge-intensive applications requiring multi-scale reasoning. The development of stable, efficient hyperbolic operations and their thoughtful integration into neural architectures promises significant advances in AI's ability to represent and reason about complex hierarchical structures.

## Contributors

Menglin Yang, Neil He, Hiren Madhu, Ngoc Bui, Ali Maatouk, Rishabh Anand, Yifei Zhang, Jialin Chen, Jiahong Liu, Bo Xiong, Min Zhou, Irwin King, Melanie Weber, Rex Ying

Invited Speakers: Philip S. Yu, Shirui Pan, Min Zhou, Pascal Mettes, Smita Krishnaswamy