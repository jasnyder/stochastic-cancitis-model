# Abstract

The point of this folder is to demonstrate how to develop a stochastic version of a deterministic model.

Models considered include:

*   Cancitis model (Andersen et al., “Mathematical Modelling as a Proof of Concept for MPNs as a Human Inflammation Model for Cancer Development.”)
*   Niche model (Pedersen et al., “Mathematical Modelling of the Hematopoietic Stem Cell-Niche System: Clonal Dominance Based on Stem Cell Fitness.”)

# Introduction

Why mathematical modeling?

Mathematical modeling can help us understand the real world, especially when we have some idea of the mechanisms involved. In medicine in particular, we hope that fitting mathematical models to patient data can help us understand diseases better and design more effective treatments.

Why stochastic models?

> All models are wrong, but some are useful
> 
> \-- George Box

To elaborate on the above quote: all models are approximations of the real world, but if constructed correctly, can capture, predict, or explain certain aspects of the real world. The specific ways that models deviate from the real world can show up in the model as randomness.

**Unresolved variables:** As all models are approximations of the real world, they will always leave certain things out. Especially for living systems, those things that are left out will typically have some significant impact. To take a concrete example, consider the cancitis model. This model considers a person's blood-forming system as being described, at any point in time, by seven scalar quantities: number of wild type/mutant stem cells `x0, y0`; number of wild type/mutant mature cells `x1, y1`; amount of circulating debris from dead cells `a`; immune system activity `s`; and inflammatory load `I` (a summary of all external factors). This ignores, for example: blood cells of any kind with mutation status other than "wild type" or "malignant"; the numbers of blood cells at differentiation stages other than "stem" or "mature", regardless of mutation status; composition of the total blood cell count in terms of different cell types (e.g. red cells, monocytes, platelets, granulocytes, neutrophils, etc.); and so on.

How to address: add a random forcing term

**Continuum limits:** Models will very often also make a continuum approximation for quantities that they do resolve. For example, the cancitis model treats the number of wild type stem cells, `x0`, as a real-valued function of time. In reality, the number of cells is an integer, meaning it can only change by discrete amounts and at discrete points in time. Approximating it as a real number has the advantage of allowing the model to be studied with standard tools of calculus and dynamical systems theory, but does so at the cost of realism. This approximation is more severe the fewer cells there are: an extreme example is a case where `x0` becomes very small but still positive. In such a case, it could theoretically increase again, whereas the real-life scenario corresponding to this model situation is that there are zero wild type stem cells left, and they therefore cannot increase in number (see: the "atto-fox" problem [here](https://hal.science/hal-01235211/))

How to address: rewrite the model with discrete variables