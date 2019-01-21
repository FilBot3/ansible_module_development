# Getting Started

## Libraries to download

Ubuntu

```bash
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python-dev
```

Fedora

```bash
```

## Common Environment setup

1. Clone the Ansible repository
2. Change directories into the repository
3. Create a virtual environment
4. Activate the environment
5. Install development requirements
6. Run the environment setup script for ech new dev shell process

```bash
git clone https://github.com/ansible/ansible.git
cd ansible
# You'll need to have Python's virtualenv installed.
# python3 -m pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
source hacking/env-setup
```