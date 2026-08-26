---
aliases:
tags:
source:
desc:
---

Alternative installation of python2.7
```sh
curl https://pyenv.run | bash
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 2.7
pyenv shell 2.7
```

- activate python2 only for this shell (works on htb)
	- `pyenv shell 2.7.18` then `python2 34992.py`