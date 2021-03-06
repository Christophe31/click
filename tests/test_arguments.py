# -*- coding: utf-8 -*-
import click


def test_nargs_star(runner):
    @click.command()
    @click.argument('src', nargs=-1)
    @click.argument('dst')
    def copy(src, dst):
        click.echo('src=%s' % '|'.join(src))
        click.echo('dst=%s' % dst)

    result = runner.invoke(copy, ['foo.txt', 'bar.txt', 'dir'])
    assert not result.exception
    assert result.output.splitlines() == [
        'src=foo.txt|bar.txt',
        'dst=dir',
    ]


def test_nargs_tup(runner):
    @click.command()
    @click.argument('name', nargs=1)
    @click.argument('point', nargs=2, type=click.INT)
    def copy(name, point):
        click.echo('name=%s' % name)
        click.echo('point=%d/%d' % point)

    result = runner.invoke(copy, ['peter', '1', '2'])
    assert not result.exception
    assert result.output.splitlines() == [
        'name=peter',
        'point=1/2',
    ]


def test_nargs_err(runner):
    @click.command()
    @click.argument('x')
    def copy(x):
        click.echo(x)

    result = runner.invoke(copy, ['foo'])
    assert not result.exception
    assert result.output == 'foo\n'

    result = runner.invoke(copy, ['foo', 'bar'])
    assert result.exit_code == 2
    assert 'Got unexpected extra argument (bar)' in result.output
