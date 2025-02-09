from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='flaskread',
      version='0.1',
      description='The flask the unlock PDFs',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='flask pdf remove upack lock ',
      url='https://github.com/Fairvinay/flaskreader/.',
      author='Store Admin',
      author_email='fairvinay@gmail.com',
      license='MIT',
      packages=['src'],
      install_requires=[
          'markdown',
      ],
#      test_suite='nose.collector',
#      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['app=src.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
 