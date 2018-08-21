# -*- coding: utf-8 -*-
"""A Pygments lexer for version 3 of the Lean theorem proving language.

Extracted from the file pygments/lexers/theorem.py in the fork of
Pygments maintained by Gabriel Ebner at
https://bitbucket.org/gebner/pygments-main/.

"""

import re

from pygments.lexer import RegexLexer, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number

__all__ = ['LeanLexer']


class LeanLexer(RegexLexer):
    """
    For the `Lean <https://github.com/leanprover/lean>`_
    theorem prover, version 3.
    """


    name = 'Lean'
    aliases = ['lean']
    filenames = ['*.lean']
    mimetypes = ['text/x-lean']

    flags = re.MULTILINE | re.UNICODE

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'/--', String.Doc, 'docstring'),
            (r'/-', Comment, 'comment'),
            (r'--.*?$', Comment.Single),
            (words((
                'import', 'renaming', 'hiding',
                'namespace',
                'local',
                'private', 'protected', 'section',
                'include', 'omit', 'section',
                'protected', 'export',
                'open',
                'attribute',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Namespace),
            (words((
                'lemma', 'theorem', 'def', 'definition', 'example',
                'axiom', 'axioms', 'constant', 'constants',
                'universe', 'universes',
                'inductive', 'coinductive', 'structure', 'extends',
                'class', 'instance',

                'noncomputable theory',

                'noncomputable', 'mutual', 'meta',

                'attribute',

                'parameter', 'parameters',
                'variable', 'variables',

                'reserve', 'precedence',
                'postfix', 'prefix', 'notation', 'infix', 'infixl', 'infixr',

                'begin', 'by', 'end',

                'set_option',
                'run_cmd',
            ), prefix=r'\b', suffix=r'\b'), Keyword.Declaration),
            (r'@\[[^\]]*\]', Keyword.Declaration),
            (words((
                'forall', 'fun', 'Pi', 'from', 'have', 'show', 'assume', 'suffices',
                'let', 'if', 'else', 'then', 'in', 'with', 'calc', 'match',
                'do'
            ), prefix=r'\b', suffix=r'\b'), Keyword),
            (words(('Sort', 'Prop', 'Type'), prefix=r'\b', suffix=r'\b'), Keyword.Type),
            (words((
                '#eval', '#check', '#reduce', '#exit',
                '#print', '#help',
            ), suffix=r'\b'), Keyword),
            (words((
                '(', ')', ':', '{', '}', '[', ']', u'⟨', u'⟩', u'‹', u'›', u'⦃', u'⦄', ':=', ',',
            )), Operator),
            (u"[A-Za-z_\u03b1-\u03ba\u03bc-\u03fb\u1f00-\u1ffe\u2100-\u214f]"
             u"[.A-Za-z_'\u03b1-\u03ba\u03bc-\u03fb\u1f00-\u1ffe\u2070-\u2079"
             u"\u207f-\u2089\u2090-\u209c\u2100-\u214f0-9]*", Name),
            (r'0x[A-Za-z0-9]+', Number.Integer),
            (r'0b[01]+', Number.Integer),
            (r'\d+', Number.Integer),
            (r'"', String.Double, 'string'),
            (r"'(?:(\\[\\\"'ntbr ])|(\\x[0-9a-fA-F]{2})|.)'", String.Char),
            (r'[~?][a-z][\w\']*:', Name.Variable),
            (r'\S', Name.Builtin.Pseudo),
        ],
        'comment': [
            (r'[^/-]', Comment.Multiline),
            (r'/-', Comment.Multiline, '#push'),
            (r'-/', Comment.Multiline, '#pop'),
            (r'[/-]', Comment.Multiline)
        ],
        'docstring': [
            (r'[^/-]', String.Doc),
            (r'-/', String.Doc, '#pop'),
            (r'[/-]', String.Doc)
        ],
        'string': [
            (r'[^\\"]+', String.Double),
            (r'\\[n"\\]', String.Escape),
            ('"', String.Double, '#pop'),
        ],
    }
