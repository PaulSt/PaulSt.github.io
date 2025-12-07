Title: Space-time Maxwell-Stefan equation
Date:  2020-10-10

The Maxwell-Stefan system for $N=2$ is given by

$$
\begin{equation*}
\begin{cases}
\partial_t\rho_i=\nabla\cdot \left(\sum_{j=1}^{2}A_{ij}(\rho_1,\rho_2)\nabla\rho_{j}\right)&\mbox{in }\Omega,\ t>0,\\
\sum_{j=1}^2 A_{ij}(\rho_1,\rho_2)\partial_\nu \rho_j = 0&\mbox{on }\partial\Omega,\ t>0,\\
\rho_i(0)=(\rho_0)_i&\mbox{in }\Omega
\end{cases}
\end{equation*}
$$

for $i=1,2$, with

$$
\begin{equation*}
A(\rho_1,\rho_2)=\frac{1}{\delta(\rho_1,\rho_2)}\begin{pmatrix}
d_1+(d_3-d_1)\rho_1 &(d_3-d_2)\rho_1\\
(d_3-d_1)\rho_2 & d_2+(d_3-d_2)\rho_2
\end{pmatrix}
\end{equation*}
$$

Write solution in the entropy variable $w$ and the transformation $u:\mathbb R^N\to\mathcal D$, defined as

$$
\begin{align*}
u_\ell(w)=\frac{e^{w_\ell}}{1+\sum_{i=1}^N e^{w_i}}\quad\mbox{for
}\ell=1,\ldots, N
\end{align*}
$$

Find $w_h^\varepsilon\in V_h$ such that, by setting $\rho_h^\varepsilon := u(w_h^\varepsilon)$, it holds true that

$$
\begin{align*} \begin{split}
\epsilon&(\phi,w_h^\varepsilon)_{H^1(Q_T)^N}
+\int_{\Omega}\phi(T) \cdot\rho_h^\varepsilon(T)dx
-\int_{\Omega}\phi(0) \cdot \rho_0 dx\\
&-\int_0^T\int_{\Omega}\partial_t\phi \cdot\rho_h^\varepsilon dxdt 
+\sum_{i,j=1}^N\int_0^T\int_{\Omega}\nabla\phi_i \cdot A_{ij}(\rho_h^\varepsilon)\nabla (\rho_h^\varepsilon)_j dx dt\\
&\qquad\qquad= \int_0^T\int_{\Omega}\phi \cdot f(\rho_h^\varepsilon) dx dt
 \qquad \forall \phi\in V_h
\end{split} \end{align*}
$$

Applied to the Duncan Toor example: 

# ![Duncan Toor example](/images/duncantoor.gif) *Maxwell-Stefan system solved with space-time DG method*
