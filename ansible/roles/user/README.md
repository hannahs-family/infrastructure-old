# user

Configures user accounts and authentication methods.

- Creates an `ansible` user with a random password on the remote system.
- Locks the password for the `ansible` user.
- Configures the `ansible` user with an SSH public key.
- Enables passwordless `sudo` for the `ansible` user.
- Disables `root` and password-authenticated login over SSH.
