import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    from . import __version__
    click.echo('cfb-python {}'.format(__version__))
    ctx.exit()


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True,
              help='Print the current version and exit.')
def cli():
    pass


@cli.command()
@click.argument('text', type=str)
def write(text: str):
    """
    Print out given text to the console.
    :param text: given text
    """
    print(text)


if __name__ == '__main__':
    cli()
