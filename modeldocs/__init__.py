'''
modeldocs

Documentation generator for your model subclasses.
'''

__title__ = 'modeldocs'
__version__ = '0.0.1'
__all__ = ()
__author__ = 'Johan Nestaas <johannestaas@gmail.com>'
__license__ = 'GPLv3+'
__copyright__ = 'Copyright 2017 Johan Nestaas'


def main():
    import json
    import argparse
    from .document import Document
    parser = argparse.ArgumentParser(prog='modeldocs')
    parser.add_argument('--config', '-c', default='modeldocs.json')
    parser.add_argument('--output', '-o', default='docs')
    args = parser.parse_args()
    with open(args.config) as f:
        config = json.load(f)
    doc = Document(**config)
    doc.generate_docs(config['module_path'], config['base_class'],
                      config['paths'])
    doc.output(args.output)


if __name__ == '__main__':
    main()
