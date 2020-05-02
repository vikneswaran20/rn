import click


def validate_range(ctx, param, value):
    if value[0] >= value[1]:
        raise click.BadParameter('The given range should be positive')
    else:
        return value
