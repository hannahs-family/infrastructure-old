# firewall

Enables and configures the system firewall and security:

- Installs and enables firewalld on RPM-based systems.
- Allows specified ports and services through the firewall.
- Applies specified firewalld direct rules.
- Installs and enables fail2ban with the sshd jail enabled.

## Variables

### `firewalld_allowed_ports`

Dictionary of unique identifiers and firewalld port specifiers to allow. e.g.:

```yml
firewalld_allowed_ports:
  ssh: 22/tcp
```

All definitions of this variable in computed playbooks are combined into a
single dictionary and applied when this playbook runs.

### `firewalld_allowed_services`

Dictionary of unique identifiers and firewalld service names to allow. e.g.:

```yml
firewalld_allowed_services:
  ssh: ssh
```

All definitions of this variable in computed playbooks are combined into a
single dictionary and applied when this playbook runs.

### `firewalld_direct_rules`

Dictionary of unique identifiers and firewalld direct rules to apply. e.g.:

```yml
firewalld_direct_rules:
  flanneld_subnet: --add-rule ipv4 filter FORWARD 1 -i flannel.1 -j ACCEPT
```
