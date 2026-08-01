Title: Helmholtz DD preconditioners
Date:  2026-08-01

DG methods for Helmholtz can naturally encorporate Robin-type transmisson conditions. 
This is a key ingredient here, that allows us to build a domain decomposition preconditioner by restricting the global matrix.


# ![METIS partition and sorted TDG DoFs](/images/helmholtz-dd-metis.png) *METIS subdomains and the sorted TDG matrix*

Split the mesh into subdomains, get the (Trefftz)-DG dofs of the subdomains, then sweep through the local blocks.
CG then uses these multiplicative Schwarz sweeps as a preconditioner, so each iteration combines local subdomain corrections with the global Krylov iteration.

# ![CG with multiplicative Schwarz](/images/helmholtz-dd-iter.gif) *CG + multiplicative Schwarz convergence on a trapping geometry*

Nice convergence and a remarkable, sudden appearance of the trapped mode.
After a few iterations where the wave field still behaves stubbornly, the residual drops rapidly.

# ![Submarine](/images/helmholtz-dd-sub.gif) *Submarine scattering*

The same idea also scales to a larger scattering example around a submarine, with almost 10 million DoFs split over 100 subdomains.
