import unittest
from json_replacer.json_replacer import json_replacer


class ReplacerTests(unittest.TestCase):
    def test_all_tests(self):
        # Basic usage
        self.assertEqual(
            json_replacer({"greeter": "hello {{name}}"}, {"name": "lorenzo"}),
            {"greeter": "hello lorenzo"}
        )

        # Basic usage with file path
        self.assertEqual(
            json_replacer("data/input.json", "data/tokens.json"),
            {"a": "c"}
        )

        # Nested list support
        self.assertEqual(
            json_replacer({"a": 2, "c": [21, "x{{y}}x"]}, {"y": "z"}),
            {"a": 2, "c": [21, "xzx"]}
        )

        # Nested dict support
        self.assertEqual(
            json_replacer({"a": {"b": "x{{ppp}}z"}}, {"ppp": "y"}),
            {"a": {"b": "xyz"}}
        )

        # Integers support
        self.assertEqual(
            json_replacer({"a": "v{{a}}.{{b}}"}, {"a": 1, "b": 0}),
            {"a": "v1.0"}
        )

        # Super-nested support
        self.assertEqual(
            json_replacer({"a": [{"b": {"c": "{{d}}"}}]}, {"d": "xyz"}),
            {"a": [{"b": {"c": "xyz"}}]}
        )

    # Move the tests in the function above when the feature is implemented
    def future_features(self):
        # TODO support keys replacements
        self.assertEqual(
            json_replacer({"{{a}}": "b"}, {"a": "c"}),
            {"c": "b"}
        )

        # TODO support tuple keys
        self.assertEqual(
            json_replacer({("k1", "k2"): "ab{{ppp}}ef"}, {"ppp": "cd"}),
            {("k1", "k2"): "abcdef"}
        )


if __name__ == '__main__':
    unittest.main()
