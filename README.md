# LEGO MINDSTORM Turbine

## Setup

* Get the repository from github
    * Download zip
    * Alternatively `git clone https://github.com/pblml/lego_cashflow` to clone repository

* Set up virtual environment
    * In a terminal navigate into the repository directory
    * `python -m venv env` -> `./env/Scripts/activate` -> `pip install -r requirements.txt`

* Run the script
    * connect the EVBrick via USB
    * `python ./main_lab.py`; if connected successfully, you should see the System Information in the terminal
    * Control the motor power by turning the gear
    * Every 50 turns the message "SENDING 1ETH" gets printed