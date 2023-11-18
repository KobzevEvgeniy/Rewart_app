
from Fabrics.amber_generator import AmberGenerator
from Fabrics.emerald_generator import EmeraldGenerator
from Fabrics.gem_generator import GemGenerator
from Fabrics.gold_generator import GoldGenerator
from Fabrics.onyx_generator import OnyxGenerator
from Fabrics.perl_generator import PerlGenerator
from Fabrics.platinum_generator import PlatinumGenerator
from Fabrics.ruby_generator import RubyGenerator
from Fabrics.silver_generator import SilverGenerator
from Fabrics.vibranium_generator import VibraniumGenerator

if __name__ == '__main__':

    generators = [GemGenerator(),
                  GoldGenerator(),
                  SilverGenerator(),
                  PlatinumGenerator(),
                  AmberGenerator(),
                  EmeraldGenerator(),
                  PerlGenerator(),
                  RubyGenerator(),
                  OnyxGenerator(),
                  VibraniumGenerator()]
    for i in range(1):
        generators[0].create_item().open()
    for i in range(3):
        generators[1].create_item().open()
    for i in range(10):
        generators[2].create_item().open()
    for i in range(10):
        generators[3].create_item().open()
    for i in range(10):
        generators[4].create_item().open()
    for i in range(10):
        generators[5].create_item().open()
    for i in range(10):
        generators[6].create_item().open()
    for i in range(10):
        generators[7].create_item().open()
    for i in range(10):
        generators[8].create_item().open()
    for i in range(10):
        generators[9].create_item().open()


