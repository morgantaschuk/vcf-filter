## Remove adjacent variants

Remove variants from a VCF file that overlap with one another for testing purposes.

```
remove-adjacent-variants.py <file>
 use -v to print discarded variants to stderr
 use -h to print this message
```

Can also pipe from stdin instead of providing the file to the script.

Requires:
* Python 2.7


### Examples:

Remove overlapping variants from VCF file:

    python remove-adjacent-variants.py NA12878.vcf > good.vcf

Open gzipped file, remove overlapping variants and print to good.vcf

    zcat NA12878.vcf.gz | python remove-adjacent-variants.py > good.vcf

Open gzipped file, grep out the header and the PASS variants, remove overlapping variants, gzip out to good.vcf.gz

    zcat NA12878.vcf.gz | grep -E "^#|PASS" | python remove-adjacent-variants.py | gzip -c > good.vcf.gz


