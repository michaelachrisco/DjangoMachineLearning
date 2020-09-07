from django.core.management.base import BaseCommand, CommandError
import sys
from plsa import Corpus, Pipeline, Visualize
from plsa.pipeline import DEFAULT_PIPELINE
from plsa.algorithms import PLSA



class Command(BaseCommand):
    help = 'Sample PLSA out of pre-created documents'

    def handle(self, *args, **options):
        csv_file = '../data/Full-Economic-News-DFE-839861.csv'
        directory = 'DjangoMLServer/blogs'
        pipeline = Pipeline(*DEFAULT_PIPELINE)
        corpus = Corpus.from_xml(directory, pipeline)
        n_topics = 5
        plsa = PLSA(corpus, n_topics, True)
        result = plsa.fit()
        result = plsa.best_of(5)

        visualize = Visualize(result)