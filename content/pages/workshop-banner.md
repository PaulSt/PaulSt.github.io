Title: Workshop Banner
Layout: noblock
Order: -1

<style>
.workshop-marquee {
  overflow: hidden;
  white-space: nowrap;
  border: 3px double currentColor;
  padding: 0.45rem 0;
  margin: 0;
  font-family: "Courier New", monospace;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.workshop-marquee a {
  display: inline-block;
  padding-left: 100%;
  animation: workshop-scroll 20s linear infinite;
  text-decoration: none;
}

.workshop-marquee a:hover {
  animation-play-state: paused;
}

@keyframes workshop-scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-100%); }
}

@media (prefers-reduced-motion: reduce) {
  .workshop-marquee a {
    animation: none;
    padding-left: 0;
  }
}
</style>

<div class="workshop-marquee" aria-label="Workshop announcement">
  <a href="https://trefftz2026.univie.ac.at/">
    *** TREFFTZ WORKSHOP 2026 *** 7-9 SEPTEMBER 2026 *** VIENNA *** A CENTURY OF TREFFTZ METHODS *** REGISTRATION OPEN ***
  </a>
</div>
