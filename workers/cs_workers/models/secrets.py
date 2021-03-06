import argparse
import json
import os

from cs_workers.utils import clean
import cs_secrets


class ModelSecrets(cs_secrets.Secrets):
    def __init__(self, owner=None, title=None, name=None, project=None):
        if owner and title:
            self.owner = owner
            self.title = title
        else:
            self.owner, self.title = name.split("/")
        self.project = project
        self.safe_owner = clean(self.owner)
        self.safe_title = clean(self.title)
        super().__init__(project)

    def set(self, name, value):
        secret_name = f"{self.safe_owner}_{self.safe_title}"
        try:
            secret_val = self.get()
        except cs_secrets.SecretNotFound:
            secret_val = {name: value}
            return super().set(secret_name, json.dumps(secret_val))
        else:
            if secret_val is not None:
                secret_val[name] = value
            else:
                secret_val = {name: value}
            if value is None:
                secret_val.pop(name)

        return super().set(secret_name, json.dumps(secret_val))

    def get(self, name=None):
        secret_name = f"{self.safe_owner}_{self.safe_title}"
        try:
            secret = json.loads(super().get(secret_name))
        except cs_secrets.SecretNotFound:
            return {}

        if name and name in secret:
            return secret[name]
        elif name:
            return None
        else:
            return secret

    def list(self):
        return self.get()

    def delete(self, name):
        return self.set(name, None)


def get_secret(args: argparse.Namespace):
    secrets = ModelSecrets(args.owner, args.title, args.names, args.project)
    print(secrets.get(args.secret_name))


def set_secret(args: argparse.Namespace):
    secrets = ModelSecrets(args.owner, args.title, args.names, args.project)
    secrets.set(args.secret_name, args.secret_value)


def list_secrets(args: argparse.Namespace):
    secrets = ModelSecrets(args.owner, args.title, args.names, args.project)
    print(json.dumps(secrets.list(), indent=2))


def delete_secret(args: argparse.Namespace):
    secrets = ModelSecrets(args.owner, args.title, args.names, args.project)
    secrets.delete(args.delete)


def cli(subparsers: argparse._SubParsersAction):
    parser = subparsers.add_parser("secrets", description="CLI for model secrets.")
    parser.add_argument("--owner", required=False)
    parser.add_argument("--title", required=False)

    secrets_subparsers = parser.add_subparsers()

    get_parser = secrets_subparsers.add_parser("get")
    get_parser.add_argument("secret_name")
    get_parser.set_defaults(func=get_secret)

    set_parser = secrets_subparsers.add_parser("set")
    set_parser.add_argument("secret_name")
    set_parser.add_argument("secret_value")
    set_parser.set_defaults(func=set_secret)

    list_parser = secrets_subparsers.add_parser("list")
    list_parser.add_argument("--secret-name", "-s", required=False)
    list_parser.set_defaults(func=list_secrets)

    delete_parser = secrets_subparsers.add_parser("delete")
    delete_parser.add_argument("delete")
    delete_parser.set_defaults(func=delete_secret)
