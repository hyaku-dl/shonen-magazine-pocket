from setuptools import find_packages, setup

setup(
    name="shonen-magazine-pocket",
    author="whinee",
    author_email="whinyaan@pm.me",
    version='0.0.0.0-alpha.1',
    description='A Basic Shonen Magazine Pocket Scraper',
    long_description='''A no-nonsense, simple and easy to use scraper for <a target="_blank" href="https://pocket.shonenmagazine.com">Shonen Magazine Pocket Scraper</a>.
    For full information, visit https://smp.hyaku.download''',
    long_description_content_type="text/markdown",
    url="https://github.com/hyaku-dl/shonen-magazine-pocket",
    project_urls={
        'Documentation': 'https://smp.hyaku.download',
        'Source': 'https://github.com/hyaku-dl/shonen-magazine-pocket',
        'Tracker': 'https://github.com/hyaku-dl/shonen-magazine-pocket/issues',
    },
    license="MIT",
    keywords='python windows macos linux cli scraper downloader manga python3 urasunday',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=['rich', 'aiofiles', 'arrow', 'bs4', 'click', 'httpx', 'inquirer', 'lxml', 'msgpack', 'patool', 'pyyaml', 'tabulate', 'toml', 'tqdm', 'yachalk', 'yarl'],
    entry_points = {
        'console_scripts': ['smp=smp.cli:cli'],
    },
)