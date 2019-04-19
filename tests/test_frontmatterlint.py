from os import listdir
from os.path import isfile, join, isdir, splitext

import frontmatter
import pytest
from slugify import slugify

post = frontmatter.load('_photography/avlanche-release-party.md')

DEFAULT_RULES = 'default'


class TestFrontMatterLint:
    @pytest.fixture(autouse=True)
    def init(self, jekyll_config, frontlint_config):
        self.jekyll_config = jekyll_config
        self.collections = jekyll_config['collections']
        self.lint_rules = frontlint_config['rules']

    def test_all_files(self):
        for collection in self.collections:
            folder = "_{}".format(collection)
            if not isdir(folder):
                continue

            all_files = [f for f in listdir(folder) if isfile(join(folder, f))]

            rules = self._get_rules_for(collection)

            for file in all_files:
                self._test_file_format(file)

                post = frontmatter.load(join(folder, file))
                self._test_file_rules(post, rules)

    def test_file_extension(self):
        with pytest.raises(AssertionError):
            self._test_file_format("file-name.txt")

    def test_file_name(self):
        with pytest.raises(AssertionError):
            self._test_file_format("file name Wrong.md")

    def test_file_metadata(self, fixture_musique_post):
        post = frontmatter.loads(fixture_musique_post)
        with pytest.raises(AssertionError):
            self._test_file_rules(post, self._get_rules_for('musique'))

    @staticmethod
    def _test_file_rules(post, rules):
        for rule in rules:
            assert rule in post.keys(), "Missing metadata value: {}".format(rule)

    @staticmethod
    def _test_file_format(file: str):
        filename, extension = splitext(file)

        if slugify(filename) != filename:
            raise AssertionError(
                "'{}' is not in slug format. Should probably be '{}'".format(filename, slugify(filename)))

        if not extension == ".md":
            raise AssertionError("{} is not im 'md' format".format(file))

    def _get_rules_for(self, collection: str):
        return self.lint_rules[collection] + self.lint_rules[DEFAULT_RULES]
