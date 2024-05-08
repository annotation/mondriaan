import sys

from tf.convert.makewatm import MakeWATM


if __name__ == "__main__":
    Mk = MakeWATM(__file__)
    sys.exit(Mk.main())
