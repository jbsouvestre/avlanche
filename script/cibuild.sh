#!/usr/bin/env bash

set -e

JEKYLL_ENV=production
bundle exec jekyll build
touch ./_site/.nojekyll

