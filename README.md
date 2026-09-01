# ip-class-pub

CS330 public repository

## Set up

1. Install `uv`
   - `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Create an environment and install dependencies
   - `uv sync`
3. Activate the environment
    - `source .venv/bin/activate`
4. Implement project *hello*
   - `vi projects/hello/index.html`
5. Test project *hello*
   - `pytest tests/hello`
6. Install `playwright`, if necessary
   - `playwright install`

## References

- [uv](https://docs.astral.sh/uv/)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Installation | Playwright Python](https://playwright.dev/python/docs/intro)
