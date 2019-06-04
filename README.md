# Infrastructure

## Dependencies

### System Requirements

- Python 3.7
- [Pipenv][]

### External Playbooks

- [cloudalchemy.node-exporter][]
- [geerlingguy.docker][]
- [geerlingguy.kubernetes][]

## Setup

1.  Put the `.ansible-password` file in `ansible/`.

2.  Install Python dependencies:

        pipenv install
        pipenv shell

3.  Install Ansible dependencies:

        ansible-galaxy install -r requirements.yml

## Running

### Bootstrapping

Given a new host `new_host` at `192.168.1.1` and accessible over SSH as `root`:

1.  Add the new host to the correct group(s) in the appropriate inventory file
    with an `ansible_host` property:

    ```yml
    new_host:
      ansible_host: 192.168.1.1
    ```

2.  Install `sshpass`:

        brew install https://raw.githubusercontent.com/hannah-family/infrastructure/master/Library/Formula/sshpass.rb

3.  Provision the new host with the `--bootstrap` option:

        ./make.py --bootstrap new_host all

### Applying Playbooks

    ./make.py --help

## Copyright

Copyright © 2019 hannahs.family. Licenesed under the terms of the [MIT
License](LICENSE).

[cloudalchemy.node-exporter]: https://galaxy.ansible.com/cloudalchemy/node-exporter
[geerlingguy.docker]: https://galaxy.ansible.com/geerlingguy/docker
[geerlingguy.kubernetes]: https://galaxy.ansible.com/geerlingguy/kubernetes
[pipenv]: https://pipenv.readthedocs.io/en/latest/
