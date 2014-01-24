from setuptools import setup, find_packages

setup( name='publica',
    version = '0.0.1',
    description = 'Publica for Django',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/publica',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    setup_requires = [
        'pip',
    ],
    install_requires = [
        'entropy',
        'menus',
        'pages',
        'platforms',
        'posts',
    ],
    dependency_links = [
        'http://github.com/commoncode/entropy/tarball/master#egg=entropy',
        'http://github.com/commoncode/menus/tarball/master#egg=menus',
        'http://github.com/commoncode/pages/tarball/master#egg=pages',
        'http://github.com/commoncode/platforms/tarball/master#egg=platforms',
        'http://github.com/commoncode/posts/tarball/master#egg=posts',
    ]
)