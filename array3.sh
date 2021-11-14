PROGDIOR=$(dirname "$0")
cd "${PROGDIOR}" || exit
source ./venv/bin/activate
python3 main.py
deactivate
