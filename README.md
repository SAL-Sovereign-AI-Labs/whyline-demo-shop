# whyline-demo-shop

A small shop backend written with IBM Bob, with [Whyline](https://github.com/SAL-Sovereign-AI-Labs/whyline) installed. Every AI-written line keeps the prompt that caused it in git notes (`refs/notes/whyline`).

See it yourself:

```sh
git clone https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop && cd whyline-demo-shop
git fetch origin 'refs/notes/*:refs/notes/*'
npm install -g @sal-sovereign-ai-labs/whyline
whyline why src/payments/mock_gateway.py:3     # the prompt that created the mock
whyline check                                  # temporary code and its lifecycle
git log --notes=whyline -3                     # the raw notes under each commit
```

Two pull requests show the CI gate (`.github/workflows/whyline.yml`):

- **Green:** payments-v2 lands and the mock gateway is removed. Nothing temporary is past its condition.
- **Red:** payments-v2 lands but the mock stays. Its recorded condition ("until payments-v2 lands": no references left) is now true, so `whyline check --gate` fails and marks the file.

The demo repository and its prompts were built by the Whyline team to show the lifecycle end to end.
