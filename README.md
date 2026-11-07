# TT13's Fantasy Challenge — Hall of Records

A permanent, public record of a twelve-manager fantasy football league. Six seasons,
six championship rings, and every game ever played.

**→ [View the Hall](https://tt1013.github.io/fantasy-football-league/)**

Fantasy platforms record outcomes. They don't confer status. A championship is a
trophy icon on a standings page nobody reopens after January. This is the companion
site that makes the win permanent: a ring per season, a lineage of rule changes, and
lifetime records for every manager.

## The chapters

Each chapter's ring is modeled on the real Super Bowl ring of **that same NFL season** —
its silhouette, metal, stone colour and signature mechanism — with the league's own
monogram where the team mark would be. Rings are rendered in WebGL; drag to rotate,
tap to trigger each ring's mechanism.

| Chapter | Season | Name | Champion | Ring modeled after |
|:--|:--|:--|:--|:--|
| I | 2021 | The Beginning: Any Given Sunday | Binh Nguyen — *Flemish Giant* | SB LV · Buccaneers |
| II | 2022 | The Road to Glory | Tommy Tran — *TT13* | SB LVI · Rams |
| III | 2023 | The Longest Yard | Mandy Liao & Dan Dacey — *maniel* | SB LVII · Chiefs |
| IV | 2024 | The Madden Curse | Binh Nguyen — *Flemish Giant* | SB LVIII · Chiefs |
| V | 2025 | The Flemish Giant Invitational | Matt Foley — *I Can Buy Myself Bowers* | SB LIX · Eagles |
| VI | 2026 | The Mandu Memorial | Dan Holmqvist — *Dan's Dazzling Team* | SB LX · Seahawks |

Seasons are named for the January they end in. The champion wins two powers: to amend
the previous year's rule and/or add a new one, and to name the chapter that follows.

## The data

Assembled from league bylaws and platform screenshots, then verified rather than trusted.

- **491 regular-season games** across six seasons
- Every team's weekly scores reconcile **exactly** to its season points-for and
  points-against, and every win-loss record matches the published standings
- Every week contains exactly six games with all twelve teams appearing once
- Head-to-head records are built from **350 games** between current managers

Two findings came out of that verification: one chapter's published points-against was
overstated by 0.98 (the game log disproved the standings page, not the reverse), and a
"never lost to him" claim collapsed once the founding season was recovered — it was
8-1, not 7-0.

| File | Contents |
|:--|:--|
| `index.html` | The Hall — self-contained, no build step, no dependencies |
| `data/matchups.py` | All 491 games, by chapter, with the team→manager map |
| `data/league-records.md` | Canonical season-by-season record, standings, brackets, notes |
| `data/head-to-head.json` | Computed best/worst matchup per active manager |
| `data/league-seed.json` | League config, champions ledger, rule lineage |
| `data/sleeper-history-entry.md` | Entry sheet for Sleeper's manual league-history editor |

### Known gaps

- **Chapter I playoffs.** The founding season's bracket was never captured, so its title
  game score is unknown. Final placements survive; the games don't.
- **Seven Chapter I games** between departed managers are missing. Every game involving a
  current manager is present, so head-to-head is unaffected.
- One Chapter I team's season total runs 2.00 high against the published standings,
  isolated to a game against a departed manager. Flagged, not silently corrected.

## Running it

It's one static file. Open `index.html`, or serve the folder:

```bash
python3 -m http.server 8000
```

`tools/make-artifact.py` strips the document wrapper for publishing as a claude.ai Artifact.

## Tech

Plain HTML, CSS and JavaScript — no framework, no build, no dependencies. Rings are real
3D geometry (tapered torus shank, extruded head with a domed face) rendered in WebGL with
two-light specular shading and environment reflection, with an SVG renderer as fallback.
