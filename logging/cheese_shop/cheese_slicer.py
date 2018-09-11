"""main app"""

import click
from cheese_shop.cheese_slicer import CheeseSlicer


@click.command()
@click.option('--thickness', default=3, help='slice thickness')
@click.argument('cheese')
def main(thickness, cheese):
    slicer = CheeseSlicer(thickness=thickness)
    click.echo(slicer.slice(cheese))


if __name__ == '__main__':
    main()
