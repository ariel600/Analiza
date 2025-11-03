## Copilot / AI agent instructions for this repository

Purpose
- Short goal: help an AI code agent be productive in this small Blackjack project by documenting the architecture, data shapes, run/debug workflow, and observable quirks.

Big picture
- Tiny, single-process Blackjack implementation. Main entry is `main.py` which builds and shuffles a deck then calls `run_full_game`.
- Core logic lives under `core/`:
  - `core/deck.py` — deck builder and shuffle helper
  - `core/game_logic.py` — game flow, dealing, dealer logic, hand-value calculations
  - `core/player_io.py` — minimal console I/O for player action

Key invariants & data shapes
- Deck: list[dict], each card is a dict with keys `rank` (string) and `suite` (string). Example: `{"rank":"Q","suite":"H"}`.
- Player/dealer: plain dicts containing a `hand` key whose value is a list of card dicts, e.g. `player = {"hand": []}`.
- Functions typically mutate these objects in-place (pop from deck, append to `hand`).

Common call pattern (example)
- `main.py`:
  - `package = build_standard_deck()`
  - `shuffle_by_suit(package)`
  - `player = {"hand": []}; dealer = {"hand": []}`
  - `run_full_game(package, player, dealer)`

Developer workflow (how to run / debug)
- Run locally: from repository root run Python on `main.py` (Windows PowerShell):
  - `python .\main.py`
- The program uses console input (asks `H` or `S`) and prints to stdout. When debugging in VS Code, set breakpoints in `core/*` and run `main.py`.

Project-specific conventions & patterns
- No class-based OOP; the project uses simple functions + plain dicts/lists. Prefer small, pure-ish helpers in `core/`.
- Mutating collections in-place is the norm (deck pops, hand appends) — agents should preserve that style when editing.
- Minimal/no tests or CI present — be conservative and add small unit tests if changing behavior.

Integration points & external dependencies
- No external packages — only Python stdlib (`random`). Nothing else to install.

Observable issues & gotchas (useful for an agent to know)
- `build_standard_deck()` does not include Aces (`"A"`) but `calculate_hand_value` has an `elif i['rank'] == 'A'` branch. This mismatch is a real bug to be mindful of when changing card logic.
- In `core/game_logic.py`, the end-of-game sums are computed incorrectly: both `sum_player` and `sum_dealer` are assigned from `dealer["hand"]`. Expect a bug if you try to change result logic.
- `deal_two_each` uses trailing commas after append calls (e.g. `player["hand"].append(deck.pop()),`) — these are harmless but unusual; avoid introducing further stray commas.

How to edit safely (advice for an AI)
- Preserve the simple function shapes and in-place mutation unless you refactor the whole module and update all call-sites (`main.py` and tests).
- When changing hand-value logic, update both `core/deck.py` (card ranks present) and `core/game_logic.py` (value calculation and ace handling). Include unit tests for edge cases (Aces, face cards, bust logic).
- Keep CLI behavior stable: `player_io.ask_player_action()` expects exact `H` or `S` inputs (case-sensitive).

Files to inspect for related changes
- `main.py` — example run usage and how objects are wired
- `core/deck.py` — card representation and shuffle
- `core/game_logic.py` — dealing, scoring, dealer-play logic
- `core/player_io.py` — input loop; used by `game_logic`

What I will ask you after edits
- Run me the failing scenario and show output (or failing tests) so we can iterate. If you want code fixes, say whether to focus on correctness (fixing Ace handling and end-of-game totals) or to keep behavior minimal and just document.

If anything here is unclear or you want different priorities (e.g., add tests first, or refactor to OO), tell me which and I'll update the instructions.
