#!/usr/bin/env python3
# Author: Francois Aguet

import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='Combine covariates into a single matrix')
parser.add_argument('genotype_pcs', help='')
parser.add_argument('expression_covariates', help='')
parser.add_argument('prefix', help='')
parser.add_argument('--add_covariates', default=[], nargs='+', help='')
parser.add_argument('-o', '--output_dir', default='.', help='Output directory')
args = parser.parse_args()

print('Combining covariates ... ', end='', flush=True)
expression_df = pd.read_csv(args.expression_covariates, sep='\t', index_col=0, dtype=str)
genotype_df = pd.read_csv(args.genotype_pcs, sep='\t', index_col=0, dtype=str)
combined_df = pd.concat([genotype_df[expression_df.columns], expression_df], axis=0)
for c in args.add_covariates:
    additional_df = pd.read_csv(c, sep='\t', index_col=0, dtype=str)
    combined_df = pd.concat([combined_df, additional_df[expression_df.columns]], axis=0)

combined_df.to_csv(os.path.join(args.output_dir, args.prefix+'.combined_covariates.txt'), sep='\t')#, float_format='%.6g')
print('done.')