Deepred-Mt: Deep Representation Learning for Predicting C-to-U RNA Editing in Plant Mitochondria
================================================================================================

Deepred-Mt is a novel method for predicting RNA editing in plant
mitochondria using deep neural networks.

This repository contains scripts that were used to build and train
Deepred-Mt, along with other utilities.

Dependencies
============

The code was developed and tested using python 3.7.4 and TensorFlow
2.3.0.

RNA read alignments
===============

C-to-U editing sites were identified by aligning publicly available RNA-seq
data on protein-coding sequences. A compiled version of Bowtie 2.3.4.3
optimized for AMD64 was used for alignment. The following command was used:


`bowtie2 -x <index-file> --local --very-sensitive-local --no-discordant --no-mixed -R 1 --mm --no-unal --seed 1234 -1 <fastq1> -2 <fastq2> -S <output.sam>`

The index file was built with bowtie2-build.
