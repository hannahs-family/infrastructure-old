#!/usr/bin/env python3
import os
import sys
from subprocess import CalledProcessError, run
from typing import Dict, List

import click

ANSIBLE_ASK_PASS = "ANSIBLE_ASK_PASS"
ANSIBLE_HOST_KEY_CHECKING = "ANSIBLE_HOST_KEY_CHECKING"
ANSIBLE_REMOTE_USER = "ANSIBLE_REMOTE_USER"

BASE_ARGS = ["pipenv", "run", "ansible-playbook"]
DEFAULT_ENV = {
    "OBJC_DISABLE_INITIALIZE_FORK_SAFETY": "YES",
}


@click.command()
@click.option("--bootstrap",
              is_flag=True,
              help="Bootstrap a new host or hosts.")
@click.option("-u",
              "--user",
              type=str,
              help="User on the remote machine to connect as.")
@click.argument("target", default="all")
@click.argument("playbook")
def make(bootstrap: bool, user: str, target: str, playbook: str):
    args: List[str] = BASE_ARGS.copy()
    args.append("--limit={}".format(target))

    env: Dict[str, str] = os.environ.copy()
    env.update(DEFAULT_ENV)

    if user is not None:
        env[ANSIBLE_REMOTE_USER] = user

    if bootstrap:
        bootstrap_env = env.copy()
        bootstrap_env[ANSIBLE_ASK_PASS] = "true"
        bootstrap_env[ANSIBLE_HOST_KEY_CHECKING] = "false"

        if not ANSIBLE_REMOTE_USER in bootstrap_env:
            bootstrap_env[ANSIBLE_REMOTE_USER] = "root"

        run([*args, "ansible/bootstrap.yml"], env=bootstrap_env, check=True)

    run([*args, "ansible/{}.yml".format(playbook)], env=env, check=True)


if __name__ == "__main__":
    try:
        make()
    except CalledProcessError as e:
        print("Could not run: {}".format(e), file=sys.stderr)
        raise
