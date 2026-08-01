Title: Trefftz for Navier-Stokes 
Date:  2026-01-11


In our recent two-part effort to finally ride the tiger of embedded Trefftz DG methods for non-linear PDEs, we have successfully applied and analyzed the method for incompressible steady Navier-Stokes.

<h2 style="text-align: center;">
  <a href="https://arxiv.org/abs/2606.13229"><img style="display: inline-block; margin: 0 0.2em; width: auto;" src="https://img.shields.io/badge/arXiv-2606.13229-b31b1b.svg" alt="arXiv 2606.13229"></a>
  <a href="https://arxiv.org/abs/2606.13219"><img style="display: inline-block; margin: 0 0.2em; width: auto;" src="https://img.shields.io/badge/arXiv-2606.13219-b31b1b.svg" alt="arXiv 2606.13219"></a>
</h2>

## Linearization and Picard iteration

The nonlinear problem is handled by a Picard iteration.
In each step we freeze the convection field, build the Oseen Trefftz space and solve the corresponding embedded Trefftz-DG Oseen problem:

$$
\begin{array}{rll}
1 & w^0 \leftarrow \mathrm{None},\\
2 & \mathbf{for}\ n=0,\ldots,N_{\max}-1\ \mathbf{do}\\
3 & \quad \mathsf{ComputeTrefftzSpace}(w^{n})
    \quad \text{for the Oseen linearization}\\
4 & \quad (u_h^{n+1},p_h^{n+1})
  \leftarrow \mathsf{OseenTrefftzSolve}(\mathcal{T}_h,\nu;w^n),\\
5 & \quad \mathbf{if}\ w^n \neq \mathrm{None}\ \mathbf{and}\ 
        \lVert u_h^{n+1}-w^n\rVert < \mathrm{tol}\ \mathbf{then}\\
6 & \quad\quad \mathbf{break},\\
7 & \quad w^{n+1} \leftarrow u_h^{n+1},\\
8 & \mathbf{end\ for.}
\end{array}
$$

## Oseen Trefftz space

On one element $K$, start with the discontinuous polynomial trial space

$$
V_h^k(K)=[\mathbb{P}_k(K)]^d \times \mathbb{P}_{k-1}(K)
$$

for velocity and pressure. The residual is tested in

$$
Q_h^k(K)=[\mathbb{P}_{k-2}(K)]^d \times \mathbb{P}_{k-1}(K).
$$

For fixed convection $w$, the embedded Oseen Trefftz space is

$$
\begin{align*}
\mathbb{T}_{w,h}^k(K)=
\big\{(u_h,p_h)\in V_h^k(K):\;&
(-\nu\Delta u_h+(w\cdot\nabla)u_h+\nabla p_h,v_h)_K=0,\\
&(\nabla\cdot u_h,q_h)_K=0
\quad \forall (v_h,q_h)\in Q_h^k(K)\big\}.
\end{align*}
$$


# ![st](/images/navier-stokes-st.gif) *Steady state solution of the Navier-Stokes equations Schäfer-Turek benchmark problem*


Source code and examples are available in the [NGSTrefftz docs](https://paulst.github.io/NGSTrefftz/notebooks/embTrefftz-ns.html).
