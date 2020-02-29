from distutils.core import setup


setup(
    name='breseq_specificity',
    version='0.0.1',
    packages=['breseq_specificity'],
    url='https://github.com/barricklab/breseq-ext-specificity',
    license='MIT',
    author='Jeffrey Barrick',
    author_email='jbarrick@cm.utexas.edu',
    description='Analyzes specificity of genome evolution to different treatments.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    scripts=['bin/breseq_specificity.py'],
)
