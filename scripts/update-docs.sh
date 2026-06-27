#!/bin/bash

# exit when any command fails
set -e

if [ -z "$1" ]; then
  ARG=-r
else
  ARG=$1
fi

if [ "$ARG" != "--check" ]; then
  tail -1000 ~/.codeloom/analytics.jsonl > codeloom/website/assets/sample-analytics.jsonl
  cog -r codeloom/website/docs/faq.md
fi

# README.md before index.md, because index.md uses cog to include README.md
cog $ARG \
    README.md \
    codeloom/website/index.html \
    codeloom/website/HISTORY.md \
    codeloom/website/docs/usage/commands.md \
    codeloom/website/docs/languages.md \
    codeloom/website/docs/config/dotenv.md \
    codeloom/website/docs/config/options.md \
    codeloom/website/docs/config/codeloom_conf.md \
    codeloom/website/docs/config/adv-model-settings.md \
    codeloom/website/docs/config/model-aliases.md \
    codeloom/website/docs/leaderboards/index.md \
    codeloom/website/docs/leaderboards/edit.md \
    codeloom/website/docs/leaderboards/refactor.md \
    codeloom/website/docs/llms/other.md \
    codeloom/website/docs/more/infinite-output.md \
    codeloom/website/docs/legal/privacy.md
