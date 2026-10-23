# 001 — Mathematical approach

This is an editorial outline of the [current manuscript](../preprints/001-psh-exhaustion/psh_exhaustion_refereed.pdf), not a replacement for its proofs or a separate proof review.

## From a metric obstruction to a threefold

The construction begins with a nonsplit extension of the trivial line bundle by the canonical bundle on the genus-two curve given by the smooth projective completion of $y^2=x^5-x$. Its projectivization is a ruled surface $S$ with a distinguished negative section $Y$. The relevant line bundle is $L=\mathcal O_S(Y)\otimes\pi^*K_C$.

The failure of $C^2$ semipositivity in this modified Grauert example is attributed to prior work. The manuscript needs a further ingredient: a continuous semipositive metric with controlled regularity. Near the negative curve it corrects a smooth weight by a multiple of $q^a$, where $q$ is a squared divisor norm and $0<a\le 1/2$. In scaled tangent coordinates the correction dominates the error in the original Levi form. At the endpoint $a=1/2$, its coefficient must be sufficiently large; the resulting weights are locally Lipschitz. A global maximum construction completes the metric.

The squared dual norm then gives a locally Lipschitz psh exhaustion on $\operatorname{Tot}(L^{-1})$. The remaining issue is to rule out every $C^2$ exhaustion, rather than merely a smoothing of the constructed one.

## The radius argument

Average a hypothetical $C^2$ psh exhaustion over fiberwise circle rotations. On a nonzero fiber, write it as a function of the logarithmic squared radius. Convexity in that variable and properness give a unique sufficiently high level with positive radial derivative. The implicit function theorem produces a $C^2$ radius function on the base.

The Levi identity for this level function gives a psh negative logarithmic radius. Its transformation law is exactly that of a Hermitian metric weight. This would yield a forbidden $C^2$ semipositive metric on $L$. The argument proves the general radius criterion as well as the counterexample's nonexistence assertion.

## Localizing the non-Kähler obstruction

The manuscript establishes invariance of the relevant exhaustion properties under proper modifications supported over a compact set. For descent, a convex composition makes an exhaustion constant near the exceptional region before it is passed to the target. The point modification then inserts a Hironaka configuration with compact rational curves that obstruct a Kähler form. Pullback preserves the locally Lipschitz exhaustion, and descent would contradict the original threefold's $C^2$ obstruction.

## Why the surface discussion is separate

For line bundles over a compact curve, the sign of the degree controls both continuous and smooth exhaustibility of the dual total space. That rules out a direct curve-base version of the threefold construction; it does not rule out every surface counterexample.

For divisor complements in compact surfaces, the manuscript organizes affirmative results using boundary intersection matrices and psh collar constructions, combined with explicitly cited classification, abundance, and neighborhood results. Its nonprojective compactifier theorem allows any nonzero effective divisor. Its smooth-ruling theorem assumes a nonempty reduced SNC boundary. Further projective and smooth-boundary statements are sufficient conditions, and the residual numerical conditions are not a construction of a counterexample.

The [scope notes](../reviews/scope-and-status.md) record the external dependencies and [open directions](../notes/open-directions.md) record what these arguments leave unresolved.
