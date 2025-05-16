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

Tonalogy is composed of two layers:

Tonalogy Core (backend):

- Inference engine using modal logic and Kripke semantics
- REST API for submitting progressions and receiving analysis

Tonalogy Interface (frontend, planned):

- Web interface (Rails or React)
- Allows users to enter progressions, view tonal paths, cadences, and explanations
- Visual representations of modulation graphs and modal truth spaces

## Tech Stack

Backend (Core):

- Python 3.11+
- FastAPI (RESTful API)
- Pydantic (data modeling)
- Custom logic engine (Kripke semantics)
- Pytest (testing)

CLI (Planned):

- Lightweight command-line interface in Python
- Allows offline or quick local analysis of chord progressions

Frontend (Planned):

- Rails with Hotwire (or React)
- SVG/Canvas rendering of harmonic paths
- Visualization of tonal worlds, modulations, and modal truth values

## References

- ARAGÃO, F. E. F. (2021). Tonal Progressions Identification Through Kripke Semantics.
Revista Música em Contexto, 5(1), 80–88. <https://doi.org/10.46926/musmat.2021v5n1.80-88>
- MORAIS, Antônio. (in progress).
Uma Implementação Computacional para Análise de Tonalidade
em Progressões Harmônicas via Semântica de Mundos Possíveis.
Universidade Federal do Ceará – Campus Quixadá.
