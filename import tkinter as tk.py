name: Check Flet Version
on: [push]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install and Check Flet
        run: |
          pip install flet
          flet --version
          pip show flet
