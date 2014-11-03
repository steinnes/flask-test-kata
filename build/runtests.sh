#!/bin/bash
cd /app
py.test --color=no --cov calculator --cov-report xml --junit-xml=/testoutput/junit.xml /app/tests -v
mv coverage.xml /testoutput
