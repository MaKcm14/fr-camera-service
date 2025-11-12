#/bin/bash

python -m venv venv
source venv/bin/activate
python ../main.py &
python ../extra/main.py &
