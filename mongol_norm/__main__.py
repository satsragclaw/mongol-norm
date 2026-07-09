"""Enable `python -m mongol_norm` as a CLI entry point.

Kept as its own module so `python -m mongol_norm` does not re-import the
package under __main__ (which is what `python -m mongol_norm.shaper` does,
triggering a RuntimeWarning about a double import).
"""
from .shaper import main

if __name__ == "__main__":
    main()
