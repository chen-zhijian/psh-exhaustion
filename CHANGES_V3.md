# Changes in Version 3

**3 November 2026** · [Version 3](papers/paper_v3.pdf) · [Version 2](papers/paper_v2.pdf)

Version 3 resolves the $C^1$ threshold left open in Version 2 and extends the radius criterion to continuous, Hölder, differentiable, smooth, and real analytic regularity.

## The obstruction improves from $C^2$ to $C^1$

Version 2 constructed threefolds with locally Lipschitz plurisubharmonic (psh) exhaustions but no $C^2$ psh exhaustion. Version 3 proves that they admit **no $C^1$ psh exhaustion**.

The key addition is the first-normal-derivative lemma (Lemma 2.2): if $D\subset\mathbb C$ is a disc and $\varphi$ is a real-valued $C^1$ psh function near $D\times\{0\}$, then

$$
\varphi(z,0)=\mathrm{constant}
\quad\Longrightarrow\quad
b(z)=\partial_w\varphi(z,0)\text{ is holomorphic}.
$$

For holomorphic $f$, restriction to the graphs $w=\pm tf(z)$ gives, locally uniformly as $t\downarrow0$,

$$
\frac{\varphi(z,\pm tf(z))-\varphi(z,0)}{t}
\longrightarrow\pm2\operatorname{Re}(b(z)f(z)).
$$

Both limits are subharmonic, so $\operatorname{Re}(bf)$ is harmonic. Taking $f=1,i$ first makes $b$ smooth and harmonic; taking $f=z,iz$ then gives $\bar\partial b=0$. No second derivatives of $\varphi$ are required.

Applied to metric weights near the negative section $Y$, the lemma yields holomorphic coefficients satisfying

$$
g_{ij}b_j=b_i+c_{ij}.
$$

These coefficients split the chosen nonsplit extension, a contradiction. Proposition 2.3 therefore excludes a $C^1$ semipositive metric on $L$ over **any neighborhood of $Y$**, and likewise on $L^{\otimes m}$ for every positive integer $m$. The generalized criterion transfers this obstruction to arbitrary $C^1$ psh exhaustions of the dual total space; no circle-invariance assumption is imposed on the original exhaustion.

## Corollary 3.4 becomes the regularity criterion

Version 2 established the equivalence only for $C^2$ and $C^\infty$. Theorem 3.4 of Version 3, **Regularity criterion**, states that for a holomorphic line bundle $A\to Z$ over a compact complex manifold,

$$
\begin{gathered}
\operatorname{Tot}(A^{-1})\text{ admits a psh exhaustion of class }\mathcal R
\\\Longleftrightarrow\\
A\text{ admits a Hermitian metric of class }\mathcal R\text{ with psh weights},
\end{gathered}
$$

for every

$$
\begin{aligned}
\mathcal R\in{}&\{C^r:r\in\mathbb Z_{\ge0}\cup\{\infty\}\}\cup\{C^\omega\}\\
&{}\cup\{C^{k,\alpha}_{\mathrm{loc}}:k\in\mathbb Z_{\ge0},\ 0<\alpha\le1\}.
\end{aligned}
$$

No Kähler or projectivity assumption on $Z$ is needed. Below $C^2$, semipositivity means that the local weights are psh, equivalently that their curvature currents are positive.

The extended proof supplies three ingredients beyond the earlier $C^2$ argument:

- Circle averaging preserves every listed class, with uniform power-series estimates for real analyticity.
- For the logarithmic radius defined by $U(z,\sigma(z))=c$, a holomorphic-disc argument proves that $-\sigma$ is psh without differentiating it.
- Positive radial slope permits the implicit-function argument for differentiable and analytic data. A uniform secant estimate gives

  $$
  |\sigma(z)-\sigma(w)|\le\frac{C}{m}|z-w|^\alpha
  $$

  for Hölder data, including the Lipschitz endpoint. Differentiating the level equation then preserves higher Hölder regularity.

The converse uses the dual squared norm $\rho(v)=\|v\|_{h^{-1}}^2$, which is a psh exhaustion of the same class. The theorem is an **existence equivalence at the same regularity**; it does not assert that smooth data have real analytic replacements. In particular, $C^{k,1}_{\mathrm{loc}}$ remains distinct from $C^{k+1}$.

## Broader construction and supporting arguments

The fixed example in Version 2 is replaced by the general Grauert construction

$$
0\longrightarrow F\longrightarrow E\longrightarrow\mathcal O_B\longrightarrow0,
\qquad \deg F>0,\quad 0\ne\xi\in H^1(B,F),
$$

where $B$ is a smooth connected projective curve of genus at least two. Version 3 develops the ruled-surface geometry, locally Lipschitz semipositive metrics with strictly positive curvature away from $Y$, and their minimal-singularity properties. The introductory threefold theorem now states existence; the construction appears in the body.

Modification invariance extends to every $C^r$ class with $r\in\mathbb Z_{\ge0}\cup\{\infty\}$, carrying the $C^1$ obstruction to the non-Kähler example.

The principal surface and curve-fibering conclusions remain unchanged. The Enoki argument now includes a direct check of the 1981 paper. In the Enoki case, let $S_0$ be the minimal class VII surface, $n=b_2(S_0)>0$, and $Q$ the linearization of the affine-line bundle complement $\mathcal A$. The infinity section $Y_\infty$ of its ruled compactification satisfies

$$
\deg Q=-n,\qquad
N_{Y_\infty/\overline{\mathcal A}}\simeq Q^{-1},\qquad
Y_\infty^2=n>0,
$$

which supplies the positive boundary collar. The general regularization problem for noncompact complex surfaces remains open.

See Sections 2–3 of the [manuscript](papers/paper_v3.pdf) for the two main advances, the [supporting notes](supporting_notes/) for the revision inputs, and the [dated review](prompts_and_logs/review_notes/revision-2026-11-03.txt) for the mathematical audit and editorial checks.
