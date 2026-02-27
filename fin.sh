#!/bin/bash

TODAY=$(date +%Y-%m-%d)

git add .
git commit -m "$TODAY"
git push

echo "강후야 오늘 수고 많았다 내일도 꼭해라 핑계대지 말고"
