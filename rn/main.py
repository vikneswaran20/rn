"""
main class for rn library

"""
import click
from . import __version__
from .numbers import Numbers
from .uuids import UUID
from . import validation


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.command('number', help='generate random numbers')
@click.option(
    '--range',
    '-r',
    default=(1, 1000),
    nargs=2,
    type=float,
    callback=validation.validate_range,
    help='output range',
    show_default=True
)
@click.option(
    '--iteration',
    '-i',
    default=1,
    type=int,
    help='number of iterations',
    show_default=True
)
@click.option(
    '--delimiter',
    '-d',
    default='\n',
    type=str,
    help='delimiter for generated numbers'
)
@click.option(
    '--unique',
    '-u',
    is_flag=True,
    help='generate unique numbers'
)
@click.option(
    '--sort',
    '-s',
    default=None,
    type=click.Choice(['asc', 'desc'], case_sensitive=False),
    help='sort the values'
)
@click.option(
    '--precision',
    '-p',
    default=None,
    type=int,
    callback=validation.validate_precision,
    help='number of decimal places'
)
def random_number(iteration, range, delimiter, unique, sort, precision):
    numbers = Numbers(range, iteration, delimiter, unique, sort, precision)
    click.echo(numbers.generate_random())


@cli.command('uuid', help='generate random uuid')
@click.option(
    '--iteration',
    '-i',
    default=1,
    type=int,
    help='number of iterations',
    show_default=True
)
@click.option(
    '--delimiter',
    '-d',
    default='\n',
    type=str,
    help='delimiter for generated uuids'
)
def random_uuid(iteration, delimiter):
    uuids = UUID(iteration, delimiter)
    click.echo(uuids.genrate_random())
