import click


def validate_range(ctx, param, value):
    if value[0] >= value[1]:
        raise click.BadParameter('The given range should be positive')
    else:
        return value


def validate_precision(ctx, param, value):
    if value is not None and value > 10:
        raise click.BadParameter('The precision should be less than 10')
    else:
        return value
