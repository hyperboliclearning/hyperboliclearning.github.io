---
title: "Events"
layout: clean
permalink: /events/
---

<style>
.ev-card {
  max-width: 860px;
  margin: 2rem auto;
  background: var(--surface, #fff);
  border: 1px solid var(--border, #e5e2dd);
  border-radius: 12px;
  padding: 2.5rem 2.8rem;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06), 0 1px 4px rgba(0,0,0,0.04);
  position: relative;
  overflow: hidden;
}
.ev-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--primary, #3a5a7c), var(--accent, #c0603c), var(--primary, #3a5a7c));
  opacity: 0.7;
}
.ev-card h2 {
  font-family: 'Source Sans Pro', 'Inter', sans-serif;
  font-size: 1.55em;
  font-weight: 700;
  color: var(--heading, #1e2a36);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0;
  border: none;
}
.ev-card h2::before {
  content: '';
  display: inline-block;
  width: 4px; height: 0.85em;
  background: linear-gradient(180deg, var(--primary, #3a5a7c), var(--primary-light, #4d7a9e));
  border-radius: 2px;
  flex-shrink: 0;
}
.ev-card p { color: var(--text, #3d424a); font-size: 1em; line-height: 1.8; }
.ev-card ul { padding-left: 1.2em; }
.ev-card li { margin-bottom: 0.6em; color: var(--text, #3d424a); }
.ev-card a { color: var(--primary, #3a5a7c); font-weight: 600; text-decoration: none; transition: color 0.2s; }
.ev-card a:hover { color: var(--accent, #c0603c); text-decoration: underline; }
</style>

<div class="ev-card" markdown="1">

## Events

Welcome to our events page! Here you can find information about our tutorials, workshops, and more.

- [KDD 2026 Geometric Learning Workshop (🔥)]({{ "/events/kdd2026workshop" | relative_url }})
- [NeurIPS 2025 NEGEL Workshop]({{ "/events/neurips2025negelworkshop" | relative_url }})
- [AAAI 2026 Hyperbolic FM Tutorial]({{ "/events/aaai2026tutorial" | relative_url }})
- [KDD 2025 Hyperbolic FM Tutorial]({{ "/events/kdd2025tutorial" | relative_url }})
- [WWW 2025 NEGEL Workshop]({{ "/events/www2025workshop" | relative_url }})
- [KDD 2023 Tutorial - Website](https://hyperbolicgnn.github.io/)
- [Slack channel for more discussions and tracking updates!](https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA) 
- [Awesome Hyperbolic Representation and Deep Learning Repository]({{ "/collection" | relative_url }})

</div> 