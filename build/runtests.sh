#!/bin/bash
cd /app
py.test --cov calculator --cov-report term-missing /app/tests -v
