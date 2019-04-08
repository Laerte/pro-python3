try:
    # Use the new library if available. Added in Python 2.5]
    from hashlib import md5
except ImportError:
    from md5 import new as md5  # Compatible functionality provided prior to Python 2.5
