# breseq_specificity

This Python package installs a script and associated functions for testing hypotheses about the specificity of microbial genome evolution. It takes as input lists of mutations predicted in a set of resequenced microbial genomes derived from a common ancestor in GenomeDiff format used by [breseq](https://guides.github.com/features/mastering-markdown/) and metadata that assigns each genome to a treatment.

The main script `breseq_specificity.py` calculates the Dice similarity between the sets of genes that are mutated in different treatments and uses a randomization test to determine if there are significant overall differences in the signature of genome evolution between treatments. It also uses Fisher's exact test to determine if mutations in certain 'signature' genes are concentrated in any one treatment more than would be expected by chance.


## Citation

If you use this package, please cite:

Deatherage, D.E., Kepner, J.L., Bennett, A.F., Lenski, R.E., and Barrick, J.E. (2017). Specificity of genome evolution in experimental populations of *Escherichia coli* evolved at different temperatures. *Proc. Natl. Acad. Sci. U.S.A.* **114**:E1904–E1912. [doi:10.1073/pnas.1616132114](https://doi.org/10.1073/pnas.1616132114)
