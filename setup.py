import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name='markdown-tree',  
        version='0.1.1',
        scripts=['markdown_tree'] ,
        author="Jiaming Lu",
        author_email="jiaminglu@live.com",
        description="Generate file tree in markdown format",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/jiaminglu/markdown-tree",
        classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
        ],
    )
