from confluencli import cli
import fire


def main():
    fire.Fire(cli.Cli)
