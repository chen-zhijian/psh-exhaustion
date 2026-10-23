# Contents

This collection contains one manuscript on the regularity of plurisubharmonic exhaustions. Its principal constructions are in complex dimension three; its dimension-two results have additional geometric hypotheses.

## 001 — Continuous and smooth plurisubharmonic exhaustions

**Title:** *Continuous and Smooth Plurisubharmonic Exhaustions: Threefold Counterexamples and Partial Results for Surfaces*.

[Paper](preprints/001-psh-exhaustion/psh_exhaustion_refereed.pdf) · [LaTeX](preprints/001-psh-exhaustion/psh_exhaustion_refereed.tex) · [Scope and status](reviews/scope-and-status.md) · [Open directions](notes/open-directions.md)

**Snapshot:** supplied surface-section revision dated 23 October 2026; 27-page PDF. The manuscript's author and date fields are empty. It is catalogued as a supplied research draft. The original filename `psh_exhaustion_refereed` does not establish external peer review; no standalone referee report or formal verification was supplied.

Here **psh** means plurisubharmonic; **smooth** means $C^\infty$. An exhaustion is a continuous real-valued function whose sublevel sets are compact. Existence of a locally Lipschitz psh exhaustion is distinguished from existence of **any** $C^2$ psh exhaustion.

### Principal constructions and general criteria

| Manuscript result | Statement | Scope and attribution |
| --- | --- | --- |
| **Theorem 1.1 — Kähler threefold counterexample** | A smooth quasi-projective Kähler threefold $M=\operatorname{Tot}(L^{-1})$ admits a locally Lipschitz psh exhaustion but no $C^2$ psh exhaustion. The underlying line bundle has a locally Lipschitz semipositive metric in the current sense but no $C^2$ semipositive metric. | The base is Koike's modified Grauert ruled surface over a genus-two curve. The known non-semipositivity obstruction is credited to prior work. No claim is made about $C^1$ exhaustions or minimal possible dimension. |
| **Theorem 1.2 — Non-Kähler threefold counterexample** | For every point $x\in M$, a smooth non-Kähler threefold $N$ admits a proper modification $N\to M$ that is an isomorphism away from the fiber over $x$. It has the same locally Lipschitz versus $C^2$ exhaustion gap. | Complex dimension remains three. The construction uses Hironaka's opposite-order blowups; it is a modification over a point, not a small deformation of a fixed complex structure. |
| **Proposition 3.3 and Corollary 3.4 — Radius criterion** | For a holomorphic line bundle $A$ over a compact complex manifold, $\operatorname{Tot}(A^{-1})$ has a $C^r$ psh exhaustion if and only if $A$ has a $C^r$ semipositive Hermitian metric, for $r=2$ or $r=\infty$. | The compact base can have any complex dimension. This is not stated as an equivalence at continuous or $C^1$ regularity. |
| **Proposition 4.1 — Compactly supported modifications** | Existence of a $C^r$ psh exhaustion is preserved in both directions by a proper surjective holomorphic map that is biholomorphic outside a compact set, for $r\in\{0,2,\infty\}$. | The map and compact-support hypotheses matter. This does not justify arbitrary changes of a boundary compactification. |
| **Proposition 4.4 and Corollary 4.5 — Compact products** | Taking a product with a nonempty compact connected complex manifold preserves existence of $C^r$ psh exhaustions for $r\in\{0,2,\infty\}$. A Hopf-surface factor gives an explicit non-Kähler fivefold with no $C^2$ psh exhaustion. | The stated fivefold corollary records local $C^{0,\gamma}$ regularity for $0<\gamma<1$. These are higher-dimensional consequences of the threefold example. |

The cusp correction is Lemma 2.2, and the global continuous semipositive metric is Proposition 2.4. At the Lipschitz endpoint a sufficiently large cusp coefficient is essential. Remark 2.5 discusses bounded potentials and minimal singularities **for the specified modified Grauert line bundle**, without extending the claim to arbitrary nef and big bundles or to Grauert's original example.

### Surface results and their hypotheses

The surface section does **not** prove continuous-to-$C^2$ regularization for arbitrary complex surfaces, construct a surface counterexample, or classify all noncompact surfaces.

| Manuscript result | Hypotheses and conclusion |
| --- | --- |
| **Proposition 5.1 — Holomorphic-convexity consequence** | A connected noncompact complex surface with a continuous psh exhaustion and a nonconstant holomorphic function has a smooth psh exhaustion. This is explicitly a consequence of Vâjâitu's theorem and Remmert reduction, not a new holomorphic-convexity result. |
| **Proposition 5.2 — Line-bundle total spaces over curves** | For a line bundle $A$ over a compact connected Riemann surface, continuous exhaustion of $\operatorname{Tot}(A^{-1})$, the inequality $\deg A\ge0$, and smooth exhaustion are equivalent. This excludes one curve-base construction of a counterexample, not every surface construction. |
| **Lemma 5.3 — Boundary tools** | A negative definite connected boundary component obstructs even a continuous psh exhaustion. Smooth divergent collars can be glued. The largest intersection eigenvalue separates positive-collar and weighted square-zero cases. |
| **Theorem 5.4 — Nonprojective boundary criterion** | For a smooth compact connected **nonprojective** surface $S$ and nonzero effective divisor $D$, continuous and smooth psh exhaustions of $S\setminus\operatorname{supp}D$ are equivalent to the absence of a negative definite connected boundary component. No Kähler or SNC hypothesis is required. The Hopf branch invokes a 2026 elliptic-neighborhood preprint. |
| **Theorem 5.5 — Smooth ruling criterion** | For an actual smooth $\mathbf P^1$-bundle over a compact connected curve and a nonempty reduced SNC boundary, the same equivalence holds. There is no restriction on intersection with a fiber. Birational ruledness or a singular rational fibration is not the stated hypothesis. |
| **Proposition 5.6 — Projective affirmative cases** | For smooth projective $S$, reduced SNC $D\ne0$, and a continuous psh exhaustion on the complement, a smooth exhaustion follows in four cases: disconnected boundary; the stated moving or canonical-negative square-zero condition on every zero-eigenvalue component; torsion canonical bundle; or entirely vertical boundary for a morphism to a curve with connected fibers. The torsion-canonical case is a consequence of surface log abundance. |
| **Corollary 5.7 — Residual projective pairs** | A hypothetical continuous-but-not-smooth divisor complement must, after boundary resolution, have connected SNC boundary supporting an effective nef divisor $A$ with positive coefficients, $A\cdot D_i=0$, $A^2=0$, $\kappa(S,A)=0$, and $K_S\cdot A\ge0$. These are necessary conditions, not existence or counterexample claims. |
| **Proposition 5.8 — Smooth-boundary sufficient conditions** | For a smooth connected square-zero curve $C$ in a compact Kähler surface, a smooth exhaustion of $S\setminus C$ follows from any listed condition: finite Ueda type; a unitary flat neighborhood; torsion or Diophantine normal bundle; finite image of the specified kernel character; $q(S)\ge g(C)$; or $g(C)=1$. No continuous exhaustion is assumed. The elliptic case uses the 2026 preprint. |

**Table 1** concerns compact **minimal** smooth surfaces with nonempty reduced SNC boundary and an assumed continuous psh exhaustion of the complement. Its affirmative projective rows for Kodaira dimensions $-\infty$ and $0$ do not automatically apply to every birationally equivalent compactifier. The projective Kodaira-dimension $1$ and $2$ rows are partial. The nonprojective Kähler algebraic-dimension-zero row is **excluded**, not a surface counterexample. “Partial” means untreated by the manuscript's arguments, not verified to be open throughout the literature.

### Verification and literature status

The supplied change summary and manifest document a surface-section revision and state that Sections 2–4 were unchanged. They are inherited revision evidence, not an independent proof certificate. This repository preparation checks organization and statement consistency; it does not establish a new exhaustive literature review or external mathematical validation.

The surface section explicitly depends on Chen–Filip–Sun–Tosatti–Zhang's 2026 preprint, Theorem 1.6, in its elliptic-neighborhood branches. The supplied report also records that Vâjâitu's full published article was not obtained in that earlier revision. These dependencies have not all been freshly reverified while preparing this repository. See [Scope and status](reviews/scope-and-status.md).
