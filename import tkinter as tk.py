name: Build Flet APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install Flet
        run: pip install flet
      - name: Build APK
        env:
          # Flet'in soru sormasını engellemek için otomatik değerler
          FLET_PROJECT_NAME: "KaosApp"
        run: |
          flet build apk --project KaosApp --module main.py --yes
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: app-release
          path: build/apk/app-release.apk
