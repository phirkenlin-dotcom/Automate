name: Keep Streamlit App Awake

on:
  schedule:
    - cron: '0 */6 * * *'   # runs every 6 hours
  workflow_dispatch:        # lets you trigger it manually from the Actions tab

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping the app
        run: curl --fail --silent --show-error https://transitproject-research-vuatgshygv8a6bpv3pu6vm.streamlit.app/ || true
