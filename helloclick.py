#!/usr/bin/env python
import click

@click.command(help="This is just a hello app.  It does nothing")
@click.option('--name', prompt='I need your name!',
              help='This is your proper name')
@click.option('--color', prompt="I need your color", help="This is the color")
def hello(name, color):
    if name == "Thor":
        click.echo("Thor you are always red")
        click.echo(click.style(f'Hello World! {name}', fg="red"))
    else:
        click.echo(click.style(f'Hello World! {name}', fg=color))
    

    

if __name__ == '__main__':
    hello()