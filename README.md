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

        ansible-galaxy install -r ansible/requirements.yml

## Running

### Bootstrapping

Given a new host `new_host` at `192.168.1.1` and accessible over SSH as `root`:

1.  Add the new host to the correct group(s) in the appropriate inventory file
    under `ansible/inventory/`.

2.  Create a file for the new host in `ansible/inventory/host_vars/`:

    ```yml
    ---
    ansible_host: 192.168.1.1
    ```

3.  Run the `bootstrap` playbook against the new host:

        ansible-playbook -k -i new_host ansible/bootstrap.yml

### Applying Playbooks

    ansible-playbook ansible/all.yml

## Copyright

Copyright © 2019 hannahs.family. Licenesed under the terms of the [MIT
License](LICENSE).

[cloudalchemy.node-exporter]: https://galaxy.ansible.com/cloudalchemy/node-exporter
[geerlingguy.docker]: https://galaxy.ansible.com/geerlingguy/docker
[geerlingguy.kubernetes]: https://galaxy.ansible.com/geerlingguy/kubernetes
[pipenv]: https://pipenv.readthedocs.io/en/latest/
