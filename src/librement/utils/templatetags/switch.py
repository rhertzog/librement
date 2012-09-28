# Copyright 2012 The Librement Developers
#
# See the AUTHORS file at the top-level directory of this distribution
# and at http://librement.net/copyright/
#
# This file is part of Librement. It is subject to the license terms in
# the LICENSE file found in the top-level directory of this distribution
# and at http://librement.net/license/. No part of Librement, including
# this file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE file.

from django import template

register = template.Library()

# Based on http://www.djangosnippets.org/snippets/300/
@register.tag
def switch(parser, token):
    """
    Switch tag.  Usage::

        {% switch meal %}
            {% case "spam" %}...{% endcase %}
            {% case "eggs" %}...{% endcase %}
            {% default %}
              No case matched.
        {% endswitch %}

    Note that ``{% case %}`` arguments can be variables if you like (as can
    switch arguments, buts that's a bit silly).

    The default case is optional.
    """
    # Parse out the arguments.
    args = token.split_contents()
    if len(args) != 2:
        raise template.TemplateSyntaxError(
            "%s tag tags exactly 2 arguments." % args[0]
        )

    # Pull out all the children of the switch tag (until {% endswitch %}).
    childnodes = parser.parse(('endswitch', 'default'))

    token = parser.next_token()
    default = template.NodeList()
    if token.contents == 'default':
        default = parser.parse(('endswitch',))
        parser.delete_first_token()

    # We just care about case children; all other direct children get ignored.
    casenodes = childnodes.get_nodes_by_type(CaseNode)

    return SwitchNode(args[1], casenodes, default)

@register.tag
def case(parser, token):
    """
    Case tag. Used only inside ``{% switch %}`` tags, so see above for those docs.
    """
    args = token.split_contents()
    assert len(args) >= 2

    # Same dance as above, except this time we care about all the child nodes
    children = parser.parse(("endcase",))

    parser.delete_first_token()
    return CaseNode(args[1:], children)

class SwitchNode(template.Node):
    def __init__(self, value, cases, default):
        self.value = value
        self.cases = cases
        self.default = default

    def render(self, context):
        # Resolve the value; if it's a non-existant variable don't even bother
        # checking the values of the cases since they'll never match.
        try:
            value = template.resolve_variable(self.value, context)
        except template.VariableDoesNotExist:
            return self.default.render(context)

        # Check each case, and if it matches return the rendered content
        # of that case (short-circuit).
        for case in self.cases:
            if case.equals(value, context):
                return case.render(context)

        # No matches; render the default
        return self.default.render(context)

class CaseNode(template.Node):
    def __init__(self, values, childnodes):
        self.values = values
        self.childnodes = childnodes

    def equals(self, otherval, context):
        """
        Check to see if any of this case's values equals some other value. This
        is called from ``SwitchNode.render()``, above.
        """

        for value in self.values:
            try:
                if template.resolve_variable(value, context) == otherval:
                    return True
            except template.VariableDoesNotExist:
                # If the variable doesn't exist, it doesn't equal anything.
                pass

        return False

    def render(self, context):
        """
        Render this particular case, which means rendering its child nodes.
        """
        return self.childnodes.render(context)

class HideOnErrorNode(template.Node):
    def __init__(self, childnodes):
        self.childnodes = childnodes

    def render(self, context):
        """
        Render the child nodes, checking for TemplateSyntaxError.
        """
        try:
            return self.childnodes.render(context)
        except template.TemplateSyntaxError:
            return u''
