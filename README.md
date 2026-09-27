# whyline-demo-shop

A small shop backend written with IBM Bob (IBM's AI coding assistant), with [Whyline](https://github.com/SAL-Sovereign-AI-Labs/whyline) set up. Every line Bob wrote here keeps the request that produced it, saved in the git history.

The story in this repository: Bob wrote a mock payment gateway "so checkout works until payments-v2 lands". payments-v2 has now landed, nothing uses the mock any more, and Whyline says it is ready to delete.

## See it yourself

```sh
git clone https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop && cd whyline-demo-shop
git fetch origin 'refs/notes/*:refs/notes/*'     # Whyline's history travels as git notes
npm install -g @sal-sovereign-ai-labs/whyline
whyline why src/payments/mock_gateway.py:3       # the request that created the mock
whyline check                                    # temporary code, and what is ready to delete
```

## Two pull requests

- [PR 1](https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop/pull/1): payments-v2 lands and the mock is deleted. [The check passes.](https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop/actions/runs/36303214774)
- [PR 2](https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop/pull/2): payments-v2 lands but the mock stays. [The check fails and points at the file](https://github.com/SAL-Sovereign-AI-Labs/whyline-demo-shop/actions/runs/36303836900), with the reason Bob recorded when it wrote the mock.

The check is `.github/workflows/whyline.yml`. It runs `whyline check --gate`, which fails while any temporary code is ready to delete.

This repository and its requests were made by the Whyline team to show the whole story end to end.
