from os.path import join

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('utils', parent_package, top_path)

    config.add_data_dir('tests')

    try:
        # If the user has IPython installed, this will install the
        # nipype profile under their '~/.ipython' directory so they
        # can launch ipython with 'ipython -p nipype' and the traits
        # completer will be enabled by default.
        from IPython.genutils import get_ipython_dir
        pth = get_ipython_dir()
        config.data_files = [(pth, ['ipy_profile_nipype.py'])]
    except ImportError:
        # Don't do anything if they haven't installed IPython
        pass

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
