from setuptools import setup

setup(
    name='pygments-lean3-plugin',
    version='0.1',
    packages=['pygments_lean3',],
    entry_points="""
    [pygments.lexers]
    leanlexer = pygments_lean3.lexer:LeanLexer
    """,
)
