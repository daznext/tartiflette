import pytest

from tartiflette import TartifletteError
from tartiflette.types.exceptions.tartiflette import GraphQLError
from tartiflette.types.location import Location


@pytest.mark.parametrize(
    "message,init_kwargs,coerce_value_kwargs,expected",
    [
        (
            "Init GraphQLError",
            {},
            {},
            {"message": "Init GraphQLError", "path": None, "locations": []},
        ),
        (
            "Init GraphQLError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User GraphQLError",
            },
            {},
            {
                "message": "User GraphQLError",
                "path": ["init", "path"],
                "locations": [{"line": 1, "column": 1}],
            },
        ),
        (
            "Init GraphQLError",
            {},
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "Init GraphQLError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
            },
        ),
        (
            "Init GraphQLError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User GraphQLError",
            },
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "User GraphQLError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
            },
        ),
        (
            "Init GraphQLError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User GraphQLError",
                "extensions": {"code": 123},
            },
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "User GraphQLError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
                "extensions": {"code": 123},
            },
        ),
    ],
)
def test_graphqlerror_coerce_value(
    message, init_kwargs, coerce_value_kwargs, expected
):
    graphql_error = GraphQLError(message, **init_kwargs)
    assert graphql_error.coerce_value(**coerce_value_kwargs) == expected


@pytest.mark.parametrize(
    "message,init_kwargs,coerce_value_kwargs,expected",
    [
        (
            "Init TartifletteError",
            {},
            {},
            {
                "message": "Init TartifletteError",
                "path": None,
                "locations": [],
            },
        ),
        (
            "Init TartifletteError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User TartifletteError",
            },
            {},
            {
                "message": "User TartifletteError",
                "path": ["init", "path"],
                "locations": [{"line": 1, "column": 1}],
            },
        ),
        (
            "Init TartifletteError",
            {},
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "Init TartifletteError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
            },
        ),
        (
            "Init TartifletteError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User TartifletteError",
            },
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "User TartifletteError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
            },
        ),
        (
            "Init TartifletteError",
            {
                "path": ["init", "path"],
                "locations": [Location(line=1, column=1)],
                "user_message": "User TartifletteError",
                "extensions": {"code": 123},
            },
            {
                "path": ["coerce", "value", "path"],
                "locations": [Location(line=2, column=2)],
            },
            {
                "message": "User TartifletteError",
                "path": ["coerce", "value", "path"],
                "locations": [{"line": 2, "column": 2}],
                "extensions": {"code": 123},
            },
        ),
    ],
)
def test_tartifletteerror_coerce_value(
    message, init_kwargs, coerce_value_kwargs, expected
):
    graphql_error = TartifletteError(message, **init_kwargs)
    assert graphql_error.coerce_value(**coerce_value_kwargs) == expected
