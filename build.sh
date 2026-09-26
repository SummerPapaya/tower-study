#!/bin/sh
# Assemble the website in dist/ with only the files the page needs.
# Cloudflare Pages: build command "sh build.sh", build output directory "dist".
set -eu
cd "$(dirname "$0")"

rm -rf dist
mkdir -p dist
cp tower-study.html dist/index.html
cp -R static dist/static
cp static/favicon.ico dist/favicon.ico
cp _headers dist/_headers

echo "dist/ ready: $(find dist -type f | wc -l | tr -d ' ') files, $(du -sh dist | cut -f1)"
