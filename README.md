# EVD
# QuickPrint — PyScript Business Website

A local academic website prototype for QuickPrint Printing Services. The business concept proposes convenient near-campus printing, photocopying, scanning, basic document formatting, binding, lamination, computer stations, and advance file hand-off.

## Run locally

Python 3.8+ is enough to serve the static files. From this folder, start a simple HTTP server:

```bash
python3 -m http.server 3000 --bind 127.0.0.1
```

Open `http://127.0.0.1:3000/` in a modern browser. Do not open `index.html` directly as a `file://` URL; the browser needs the local HTTP server to load the Python module. PyScript 2026.7.3 and the web fonts are loaded from their public CDNs, so the first run requires an internet connection.

In the Manus Preview runtime, the server should listen on port 3000 and bind to `0.0.0.0`; in the terminal, use:

```bash
python3 -m http.server 3000 --bind 0.0.0.0
```

The README’s `127.0.0.1` command is the normal local-computer option. The `0.0.0.0` command exposes the service to the project runtime network; it does not create a public GitHub repository.

## Interactions to demonstrate

The service selector changes the form fields and estimate rules. Page counts, number of copies, paper size, and hand-off selection update the estimate in response to input/change events. “Try a 5-page sample” and “Clear form” demonstrate click events. Submitting the form demonstrates validation and a Python-generated on-screen summary. The file picker reports its filename only; the contents stay untouched.

The estimate uses proposal figures only: black-and-white printing ₱1 per short-bond page; color printing ₱4 per short-bond page; photocopying ₱5 per short-bond page; lamination ₱20 per item; computer station ₱1 per 5 minutes. Scanning, binding, formatting, and unlisted paper sizes display “Request a quote.” These are academic sample rates, not confirmed prices.

## Important demo limitation

This is a browser-only demo. It does not send a real order, transmit the selected document, connect to Messenger/Drive/email, contact a live shop, save customer data, or promise a pickup time. The form confirmation is a local presentation state, not an order receipt.

## Files

`index.html` contains the semantic page, `styles.css` holds the responsive style system, `main.py` registers PyScript DOM events, and `pricing.py` contains the testable proposal-based price rules. `pyscript.json` copies that module into PyScript’s browser filesystem. `manus-routes.json` declares the one page route. `test_pricing.py` checks the amount and quote rules. `assets/quickprint-concept.svg` preserves the Figma-importable layout concept.

Run the price-rule tests with:

```bash
python3 -m unittest -v test_pricing
```

## Group and eventual repository requirements

The proposal names Alex Aristoteles, Josh Benedict Bariquit, Christopher Diaz, Rose Ela Marie Mundin, and Steven Villacorta. This local build does not create or publish a GitHub repository, invite collaborators, or claim that any member has already made a commit. When the group is ready to satisfy the repository requirement, create a public repository only with the group’s approval, add the correct GitHub usernames, and have each member make and push a meaningful change under their own account. Use `PRESENTATION_GUIDE.md` as a planning aid for the required 10-minute recorded presentation; the actual recording must show every member participating and must describe only work they really completed.

## PyScript references

The page pins the official PyScript 2026.7.3 browser runtime. See the [PyScript quick start](https://docs.pyscript.net/2026.7.3/) and [event guide](https://docs.pyscript.net/2026.7.3/user-guide/events/) for the external runtime and `@when` event-handler pattern.
