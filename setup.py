from setuptools import setup

setup(name='merida',
      version='0.1.1',
      description='MERIDA: MOA9yr Exploration and Research Interface for Dataset Analysis Resources',
      url='https://github.com/stelais/merida',
      author='Stela IS',
      author_email='stela.ishitanisilva@nasa.gov',
      license='MIT',
      packages=['merida'],
      zip_safe=False,
      install_requires=["pyarrow==14.0.1",
                        "bokeh==3.1.0",
                        "numpy==1.26.2",
                        "pandas==2.1.4",
                        "tqdm==4.66.1",
                        "requests==2.31.0",
                        "lxml==4.9.3",
                        "html5lib==1.1"])
