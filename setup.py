from setuptools import setup, find_packages

from calculator import __version__

setup(
    name='flask_test_kata',
    version=__version__,

    description='Flask Testing Kata',
    long_description='This kata is an exercise in writing unit tests, '
                     'integration tests against Flask webapps.',
    author='Plain Vanilla Games',
    author_email='ops@plainvanilla.is',
    license='Copyright',
    url='http://www.quizup.com/',

    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    include_package_data=True
)
