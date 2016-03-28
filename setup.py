from distutils.core import setup

setup(
    name='webcrawler',
    version='1.0.0',
    description='A simple webcrawler.',
    long_description='Webcrawler to find what information there is out there on me.',
    author='Keith Rooney',
    author_email='keithrooney93@gmail.com',
    url='https://github.com/keithrooney/webcrawler',
    packages=['webcrawler'],
    maintainer='Keith Rooney',
    maintainer_email='keithrooney93@gmail.com',
    requires=['beautifulsoup4', 'funcsigs', 'pbr', 'requests', 'six']
)
