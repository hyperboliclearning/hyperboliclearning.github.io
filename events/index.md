---
title: "Events"
layout: clean
permalink: /events/
---

<style>
body {
  background-color: #edf3e8;
  background-image:
    radial-gradient(ellipse 70% 50% at 50% -5%, rgba(84,122,128,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 50% 35% at 80% 60%, rgba(142,81,39,0.03) 0%, transparent 50%);
}
.ev-card {
  max-width: 860px;
  margin: 2rem auto;
  background: #fff;
  border: 1px solid #d5ddd0;
  border-radius: 16px;
  padding: 2.5rem 2.8rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04), 0 6px 24px rgba(0,0,0,0.03);
  position: relative;
  overflow: hidden;
}
.ev-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #547a80, #8e5127, #547a80);
  opacity: 0.5;
}
.ev-card h2 {
  font-family: 'Source Sans Pro', 'Inter', sans-serif;
  font-size: 1.65em;
  font-weight: 700;
  color: #2d3a3e;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0;
  border: none;
}
.ev-card h2::before {
  content: '';
  display: inline-block;
  width: 4px; height: 0.9em;
  background: linear-gradient(180deg, #547a80, #6a9199);
  border-radius: 2px;
  flex-shrink: 0;
}
.ev-card p { color: #596673; font-size: 1.02em; line-height: 1.8; }
.ev-card ul { padding-left: 1.2em; }
.ev-card li { margin-bottom: 0.6em; color: #596673; }
.ev-card a { color: #547a80; font-weight: 600; text-decoration: none; transition: color 0.2s; }
.ev-card a:hover { color: #8e5127; text-decoration: underline; }
</style>

<div class="ev-card" markdown="1">

## Events

Welcome to our events page! Here you can find information about our tutorials, workshops, and more.

- [NeurIPS 2025 NEGEL Workshop]({{ "/events/neurips2025negelworkshop" | relative_url }})
- [AAAI 2026 Hyperbolic FM Tutorial]({{ "/events/aaai2026tutorial" | relative_url }})
- [KDD 2025 Hyperbolic FM Tutorial]({{ "/events/kdd2025tutorial" | relative_url }})
- [WWW 2025 NEGEL Workshop]({{ "/events/www2025workshop" | relative_url }})
- [KDD 2023 Tutorial - Website](https://hyperbolicgnn.github.io/)
- [Slack channel for more discussions and tracking updates!](https://join.slack.com/t/hyperboliclearning/shared_invite/zt-1qcqgtwfr-HpsRSzDhvkAEal6dOnKDvA) 
- [Awesome Hyperbolic Representation and Deep Learning Repository]({{ "/collection" | relative_url }})

</div> 