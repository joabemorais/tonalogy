# Tonalogy

A formal system for tonal analysis through modal logic and possible worlds semantics.

Tonalogy is a system for analyzing harmonic progressions in tonal music
using the theoretical framework of modal logic and Kripke semantics.
Inspired by the work
"Tonal Progressions Identification Through Kripke Semantics" (Aragão, 2021),
it implements an interpretative model for determining
whether a chord sequence is tonal or not — and why.

This system is also being developed as part of the undergraduate thesis entitled:

> “Uma Implementação Computacional para Análise de Tonalidade
em Progressões Harmônicas via Semântica de Mundos Possíveis”
>
> [A Computational Implementation for Tonality Analysis in Harmonic Progressions via Possible Worlds Semantics]
>
> Universidade Federal do Ceará – Campus Quixadá
>
> Author: Antônio Joabe Alves Morais

It constitutes the applied component of that research —
transforming the theoretical model into a working software solution
for tonal inference and musical interpretation.

## Concept

Each tonal center (key) is interpreted as a “possible world”.
A chord progression is parsed into a modal formula $\phi$,
and the system builds a Kripke structure ($K$)
to evaluate whether the formula holds
($K \models_\pi \phi$) over any tonal path $\pi$.

The system reveals not only whether a progression is tonal —
but in what ways, under what tonal interpretations (functions $L_i$),
and along which possible tonal transitions.

## Architecture

Tonalogy's architecture is divided into backend components and clients, following the principle of separation of concerns.

### Backend Components
- *Tonalogy Core*: This is the inference engine, responsible for all the music analysis logic. It receives a progression and returns structured data (JSON) with the complete semantic analysis, without concerning itself with visual presentation.
- *Tonalogy Visualizer*: This is the rendering module. It receives the structured data from the Core and translates it into harmonic analysis diagrams, like the ones seen in this chat. It is responsible for all SVG manipulation and final image generation.
- *Tonalogy API*: The web layer (FastAPI) that serves as the gateway to the backend services. It exposes endpoints that clients can consume to get both the raw analysis data (from the Core) and the rendered diagrams (from the Visualizer).

### Clients (API Consumers)
- *Tonalogy Interface* (frontend, planned): A web interface that allows users to input progressions, view detailed analyses, and visualize diagrams of tonal paths, cadences, and modulations.
- *Tonalogy CLI* (in development): A command-line tool for quick tests and obtaining analyses in text format, ideal for development and integration.

## Tech Stack

Backend:
- Core & API:
  - Python 3.11+
  - FastAPI (RESTful API)
  - Pydantic (data modeling)
  - Pytest (testing)

- Visualizer:
  - Python 3.11+
  - Graphviz (graph layout engine)
  - CairoSVG (library for SVG to PNG conversion)

Frontend (Planned):
- Next.js (React) or another modern JavaScript framework
- Rendering of images (PNG) or directly of SVG data
- Visualization of tonal worlds, modulations, and modal truth values

## References

- ARAGÃO, F. E. F. (2021). Tonal Progressions Identification Through Kripke Semantics.
Revista Música em Contexto, 5(1), 80–88. <https://doi.org/10.46926/musmat.2021v5n1.80-88>
- MORAIS, Antônio. (in progress).
Uma Implementação Computacional para Análise de Tonalidade
em Progressões Harmônicas via Semântica de Mundos Possíveis.
Universidade Federal do Ceará – Campus Quixadá.
