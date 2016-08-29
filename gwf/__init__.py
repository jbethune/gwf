from __future__ import absolute_import, print_function

from gwf.backends.base import Backend
from gwf.core import PreparedWorkflow, Target, Workflow


class template(object):

    def __init__(self, **options):
        self.spec = None
        self.options = options

    def __lshift__(self, spec):
        self.spec = spec
        return self

    def __call__(self, **substitutions):
        def substitute(s):
            if type(s) == str:
                return s.format(**substitutions)
            elif hasattr(s, '__iter__'):
                return [substitute(x) for x in s]
            else:
                return s

        formatted_options = [(key, substitute(val))
                             for key, val in self.options.items()]
        options = dict(formatted_options)
        return options, self.spec.format(**substitutions)


__all__ = ('Target', 'Workflow', 'PreparedWorkflow', 'Backend', 'template')
